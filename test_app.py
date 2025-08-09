#!/usr/bin/env python3
"""
Test script for AI Code Reviewer application
"""

import sys
import os

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all modules can be imported"""
    print("Testing imports...")
    
    try:
        from api_handlers.openai_api import OpenAIHandler
        print("✅ OpenAI handler imported successfully")
    except ImportError as e:
        print(f"❌ OpenAI handler import failed: {e}")
    
    try:
        from api_handlers.gemini_api import GeminiHandler
        print("✅ Gemini handler imported successfully")
    except ImportError as e:
        print(f"❌ Gemini handler import failed: {e}")
    
    try:
        from api_handlers.copilot_placeholder import CopilotHandler
        print("✅ Copilot handler imported successfully")
    except ImportError as e:
        print(f"❌ Copilot handler import failed: {e}")
    
    try:
        from utils.file_parser import FileParser
        print("✅ File parser imported successfully")
    except ImportError as e:
        print(f"❌ File parser import failed: {e}")
    
    try:
        from utils.prompt_builder import PromptBuilder
        print("✅ Prompt builder imported successfully")
    except ImportError as e:
        print(f"❌ Prompt builder import failed: {e}")
    
    try:
        from styles.custom_css import load_css
        print("✅ Custom CSS imported successfully")
    except ImportError as e:
        print(f"❌ Custom CSS import failed: {e}")

def test_file_parser():
    """Test file parser functionality"""
    print("\nTesting file parser...")
    
    from utils.file_parser import FileParser
    
    parser = FileParser()
    
    # Test supported formats
    supported_formats = ['pdf', 'txt', 'doc', 'docx', 'py']
    for fmt in supported_formats:
        if fmt in parser.supported_formats:
            print(f"✅ {fmt.upper()} format supported")
        else:
            print(f"❌ {fmt.upper()} format not supported")

def test_prompt_builder():
    """Test prompt builder functionality"""
    print("\nTesting prompt builder...")
    
    from utils.prompt_builder import PromptBuilder
    
    builder = PromptBuilder()
    
    # Test prompt building
    problem = "Test problem statement"
    code = "def test(): pass"
    
    try:
        prompt = builder.build_review_prompt(problem, code)
        if "Test problem statement" in prompt and "def test(): pass" in prompt:
            print("✅ Prompt builder working correctly")
        else:
            print("❌ Prompt builder not working correctly")
    except Exception as e:
        print(f"❌ Prompt builder failed: {e}")

def test_api_handlers():
    """Test API handlers functionality"""
    print("\nTesting API handlers...")
    
    from api_handlers.openai_api import OpenAIHandler
    from api_handlers.gemini_api import GeminiHandler
    from api_handlers.copilot_placeholder import CopilotHandler
    
    # Test OpenAI handler
    try:
        openai_handler = OpenAIHandler()
        print("✅ OpenAI handler initialized")
    except Exception as e:
        print(f"❌ OpenAI handler failed: {e}")
    
    # Test Gemini handler
    try:
        gemini_handler = GeminiHandler()
        print("✅ Gemini handler initialized")
    except Exception as e:
        print(f"❌ Gemini handler failed: {e}")
    
    # Test Copilot handler
    try:
        copilot_handler = CopilotHandler()
        print("✅ Copilot handler initialized")
    except Exception as e:
        print(f"❌ Copilot handler failed: {e}")

def test_mock_reviews():
    """Test mock review functionality"""
    print("\nTesting mock reviews...")
    
    from api_handlers.copilot_placeholder import CopilotHandler
    
    handler = CopilotHandler()
    test_prompt = "Test prompt for code review"
    
    try:
        review = handler.get_review(test_prompt)
        if review and len(review) > 100:  # Should return substantial content
            print("✅ Mock review working correctly")
        else:
            print("❌ Mock review not working correctly")
    except Exception as e:
        print(f"❌ Mock review failed: {e}")

def main():
    """Run all tests"""
    print("🧪 Testing AI Code Reviewer Application")
    print("=" * 50)
    
    test_imports()
    test_file_parser()
    test_prompt_builder()
    test_api_handlers()
    test_mock_reviews()
    
    print("\n" + "=" * 50)
    print("✅ All tests completed!")
    print("\nTo run the application:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Run the app: streamlit run app.py")
    print("3. Open browser: http://localhost:8501")

if __name__ == "__main__":
    main() 