import os
import streamlit as st
import anthropic
from typing import Optional

class ClaudeHandler:
    """Handler for Anthropic Claude API integration"""
    
    def __init__(self):
        self.api_key = self._get_api_key()
        self.client = None
        if self.api_key:
            self.client = anthropic.Anthropic(api_key=self.api_key)
    
    def _get_api_key(self) -> Optional[str]:
        """Get Claude API key from environment or Streamlit secrets"""
        # Try to get from environment variable
        api_key = os.getenv('ANTHROPIC_API_KEY')
        
        # If not in environment, try Streamlit secrets
        if not api_key:
            try:
                api_key = st.secrets["anthropic"]["api_key"]
            except:
                pass
        
        return api_key
    
    def get_review(self, prompt: str) -> str:
        """Get code review from Claude AI"""
        if not self.api_key:
            return self._get_mock_response("Claude API key not configured. Please set ANTHROPIC_API_KEY environment variable or configure in Streamlit secrets.")
        
        if not self.client:
            return self._get_mock_response("Claude client not initialized. Please check your API key.")
        
        try:
            response = self.client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=4000,
                temperature=0.7,
                messages=[
                    {"role": "system", "content": "You are a professional Python code reviewer. Provide detailed, constructive feedback."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.content[0].text
            
        except Exception as e:
            error_message = str(e)
            if "authentication" in error_message.lower() or "api key" in error_message.lower():
                return self._get_mock_response("❌ Authentication failed. Please check your Claude API key.")
            elif "rate limit" in error_message.lower() or "quota" in error_message.lower() or "exceeded" in error_message.lower():
                return self._get_mock_response("❌ Claude API quota exceeded. Please try using another model instead, or wait until your quota resets.")
            elif "api" in error_message.lower():
                return self._get_mock_response(f"❌ Claude API error: {error_message}")
            else:
                return self._get_mock_response(f"❌ Unexpected error: {error_message}")
    
    def _get_mock_response(self, error_message: str) -> str:
        """Return a mock response when API is not available"""
        return f"""
# Code Review Report

{error_message}


Since the API is paid, here's an example of what a code review might look like:

### ✅ Strengths
- Code structure is well-organized
- Variable names are descriptive
- Comments provide good context## Mock Review Example


### 🔧 Areas for Improvement
- Consider adding type hints
- Some functions could be more modular
- Error handling could be improved

### 🚀 Performance Considerations
- Algorithm complexity is appropriate
- Memory usage is efficient
- Consider caching for expensive operations
"""