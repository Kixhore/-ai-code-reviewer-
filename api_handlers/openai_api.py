import os
import streamlit as st
from openai import OpenAI
from typing import Optional

class OpenAIHandler:
    """Handler for OpenAI GPT-4 API integration"""
    
    def __init__(self):
        self.api_key = self._get_api_key()
        self.client = None
        if self.api_key:
            self.client = OpenAI(api_key=self.api_key)
    
    def _get_api_key(self) -> Optional[str]:
        """Get OpenAI API key from environment or Streamlit secrets"""
        # Try to get from environment variable
        api_key = os.getenv('OPENAI_API_KEY')
        
        # If not in environment, try Streamlit secrets
        if not api_key:
            try:
                api_key = st.secrets["openai"]["api_key"]
            except:
                pass
        
        return api_key
    
    def get_review(self, prompt: str) -> str:
        """Get code review from OpenAI GPT-4"""
        if not self.api_key:
            return self._get_mock_response("OpenAI API key not configured. Please set OPENAI_API_KEY environment variable or configure in Streamlit secrets.")
        
        if not self.client:
            return self._get_mock_response("OpenAI client not initialized. Please check your API key.")
        
        try:
            # Try with gpt-4o first
            try:
                response = self.client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a professional Python code reviewer. Provide detailed, constructive feedback."},
                        {"role": "user", "content": prompt}
                    ]
                )
                return response.choices[0].message.content
            except Exception as e:
                # Check if it's a rate limit error
                if "quota" in str(e).lower() or "exceeded" in str(e).lower() or "insufficient_quota" in str(e).lower() or "rate limit" in str(e).lower():
                    # Add a prefix to the response that the app can detect
                    fallback_prefix = "⚠️ GPT-4 quota exceeded. Falling back to GPT-3.5-Turbo...\n\n"
                    try:
                        response = self.client.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content": "You are a professional Python code reviewer. Provide detailed, constructive feedback."},
                                {"role": "user", "content": prompt}
                            ]
                        )
                        return fallback_prefix + response.choices[0].message.content
                    except Exception as fallback_error:
                        # If fallback also fails, return a more specific error message
                        error_msg = str(fallback_error)
                        if "quota" in error_msg.lower() or "exceeded" in error_msg.lower() or "insufficient_quota" in error_msg.lower():
                            return self._get_mock_response("❌ GPT-4 quota exceeded and GPT-3.5 fallback failed: OpenAI API quota exceeded. Please try using the Gemini model instead, or wait until your quota resets.")
                        else:
                            return self._get_mock_response(f"❌ GPT-4 quota exceeded and GPT-3.5 fallback failed: {error_msg}")
                else:
                    # Re-raise the exception if it's not a quota issue
                    raise e
            
        except Exception as e:
            error_message = str(e)
            if "authentication" in error_message.lower() or "api key" in error_message.lower():
                return self._get_mock_response("❌ Authentication failed. Please check your OpenAI API key.")
            elif "rate limit" in error_message.lower() or "quota" in error_message.lower() or "exceeded" in error_message.lower() or "insufficient_quota" in error_message.lower():
                return self._get_mock_response("❌ OpenAI API quota exceeded. Please try using the Gemini model instead, or wait until your quota resets.")
            elif "api" in error_message.lower():
                return self._get_mock_response(f"❌ OpenAI API error: {error_message}")
            else:
                return self._get_mock_response(f"❌ Unexpected error: {error_message}")
    
    def _get_mock_response(self, error_message: str) -> str:
        """Return a mock response when API is not available"""
        return f"""
# Code Review Report

{error_message}

## Mock Review Example

Since the API is not configured, here's an example of what a code review might look like:

### ✅ Strengths
- Code structure is well-organized
- Variable names are descriptive
- Comments provide good context

### 🔧 Areas for Improvement
- Consider adding more error handling
- Some functions could be broken down further
- Add type hints for better code documentation

### 📝 Recommendations
1. Implement comprehensive error handling
2. Add docstrings to all functions
3. Consider using dataclasses for complex data structures
4. Add unit tests for critical functions

### 🎯 Next Steps
- Review and implement the suggestions above
- Test the code with various edge cases
- Consider code formatting with tools like black or autopep8
        """