# 🔧 AI Code Reviewer - Streamlit Web App

A modern, aesthetic Streamlit web application that provides professional code review using AI models like GPT-4, Gemini, and Copilot/Grok.

## ✨ Features

### 🎨 Modern UI/UX
- **Glassmorphism Design**: Beautiful glass-like containers with blur effects
- **Google Fonts**: Inter and Poppins for modern typography
- **Responsive Layout**: Works perfectly on desktop and mobile
- **Dark Mode Support**: Automatic dark mode detection
- **Smooth Animations**: Hover effects and transitions

### 📁 File Upload Support
- **Problem Statement**: PDF, TXT, DOC, DOCX formats
- **Python Solutions**: .py files with syntax highlighting
- **File Validation**: Size and type checking
- **Progress Indicators**: Real-time upload status

### 🤖 AI Model Integration
- **GPT-4**: OpenAI's latest model for comprehensive reviews
- **Gemini**: Google's advanced AI for detailed analysis
- **Copilot/Grok**: Simulated reviews (no public API available)

### 📝 Review Features
- **Comprehensive Analysis**: Accuracy, style, efficiency, readability
- **Structured Output**: Organized feedback with actionable recommendations
- **Export Options**: Download as TXT or PDF
- **Code Highlighting**: Syntax-highlighted code snippets

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-code-reviewer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys** (optional)
   
   Create a `.streamlit/secrets.toml` file:
   ```toml
   [openai]
   api_key = "your-openai-api-key"
   
   [gemini]
   api_key = "your-gemini-api-key"
   ```
   
   Or set environment variables:
   ```bash
   export OPENAI_API_KEY="your-openai-api-key"
   export GEMINI_API_KEY="your-gemini-api-key"
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501`

## 📋 Usage Guide

### Step 1: Upload Files
1. **Problem Statement**: Upload a PDF, TXT, or DOC file containing the problem description
2. **Python Solution**: Upload your .py file with the solution code
3. **Validation**: The app will validate file types and sizes

### Step 2: Select AI Model
- **Gemini**: Best for detailed technical analysis
- **GPT-4**: Comprehensive reviews with code examples
- **Copilot/Grok**: Simulated reviews (no API required)

### Step 3: Get Review
1. Click "Submit for Review" to process your files
2. Wait for AI analysis (usually 10-30 seconds)
3. View structured feedback in the output section

### Step 4: Export Results
- **TXT Export**: Download as plain text file
- **PDF Export**: Download as formatted PDF report

## 🏗️ Project Structure

```
ai-code-reviewer/
├── app.py                          # Main Streamlit application
├── requirements.txt                 # Python dependencies
├── README.md                       # Project documentation
├── api_handlers/                   # AI model integrations
│   ├── __init__.py
│   ├── openai_api.py              # GPT-4 handler
│   ├── gemini_api.py              # Gemini handler
│   └── copilot_placeholder.py     # Copilot/Grok placeholder
├── utils/                          # Utility functions
│   ├── __init__.py
│   ├── file_parser.py             # File parsing utilities
│   └── prompt_builder.py          # AI prompt construction
└── styles/                         # Custom styling
    ├── __init__.py
    └── custom_css.py              # Modern CSS styles
```

## 🔧 Configuration

### API Keys Setup

#### OpenAI (GPT-4)
1. Get API key from [OpenAI Platform](https://platform.openai.com/)
2. Add to environment: `export OPENAI_API_KEY="your-key"`
3. Or add to Streamlit secrets

#### Google Gemini
1. Get API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Add to environment: `export GEMINI_API_KEY="your-key"`
3. Or add to Streamlit secrets

### Customization

#### Styling
Edit `styles/custom_css.py` to modify:
- Color schemes
- Fonts
- Animations
- Layout spacing

#### Prompts
Modify `utils/prompt_builder.py` to customize:
- Review criteria
- Output format
- Model-specific prompts

## 🎯 Review Criteria

The AI analyzes code based on:

### ✅ Accuracy & Correctness
- Problem solution accuracy
- Logical error detection
- Edge case handling

### 📝 Code Style & PEP 8
- Formatting compliance
- Naming conventions
- Readability standards

### ⚡ Efficiency & Performance
- Algorithm optimization
- Memory usage
- Time complexity

### 🔍 Readability & Maintainability
- Code structure
- Documentation
- Modularity

### 🛡️ Error Handling & Robustness
- Exception handling
- Input validation
- Security considerations

## 🚀 Advanced Features

### Custom Prompts
```python
from utils.prompt_builder import PromptBuilder

builder = PromptBuilder()
custom_prompt = builder.build_review_prompt(problem, code)
```

### File Parsing
```python
from utils.file_parser import FileParser

parser = FileParser()
content = parser.parse_file(uploaded_file)
```

### API Integration
```python
from api_handlers.openai_api import OpenAIHandler

handler = OpenAIHandler()
review = handler.get_review(prompt)
```

## 🐛 Troubleshooting

### Common Issues

#### API Key Errors
- **Problem**: "API key not configured"
- **Solution**: Set environment variables or configure Streamlit secrets

#### File Upload Errors
- **Problem**: "Unsupported file format"
- **Solution**: Ensure file is PDF, TXT, DOC, DOCX, or PY

#### Import Errors
- **Problem**: Missing dependencies
- **Solution**: Run `pip install -r requirements.txt`

#### PDF Parsing Issues
- **Problem**: "PyMuPDF not installed"
- **Solution**: Install with `pip install PyMuPDF`

### Performance Tips

1. **File Size**: Keep files under 10MB for optimal performance
2. **API Limits**: Be mindful of API rate limits
3. **Caching**: Reviews are cached in session state
4. **Network**: Stable internet connection for API calls

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Streamlit**: For the amazing web app framework
- **OpenAI**: For GPT-4 API access
- **Google**: For Gemini AI integration
- **Google Fonts**: For beautiful typography
- **CSS Glassmorphism**: For modern design inspiration

## 📞 Support

- **Issues**: Create an issue on GitHub
- **Discussions**: Use GitHub Discussions
- **Email**: Contact the maintainer

---

**Made with ❤️ for the developer community** 