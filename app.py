import streamlit as st
import os
import tempfile
from datetime import datetime
import json
from pathlib import Path

# Import custom modules
from api_handlers.openai_api import OpenAIHandler
from api_handlers.gemini_api import GeminiHandler
from api_handlers.claude_api import ClaudeHandler
from utils.file_parser import FileParser
from utils.prompt_builder import PromptBuilder
from styles.custom_css import load_css

# Page configuration
st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
load_css()

def main():
    # Header with modern styling
    st.markdown("""
    <div class="header-container">
        <h1 class="main-title">🔧 AI Code Reviewer</h1>
        <p class="subtitle">Professional code review powered by AI</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if 'uploaded_files' not in st.session_state:
        st.session_state.uploaded_files = {'problem': None, 'solution': None}
    if 'review_comments' not in st.session_state:
        st.session_state.review_comments = None
    if 'selected_model' not in st.session_state:
        st.session_state.selected_model = 'Gemini'
    
    # Main container with glassmorphism effect
    with st.container():
        st.markdown('<div class="glass-container">', unsafe_allow_html=True)
        
        # Upload Section
        st.markdown("""
        <div class="section-header">
            <h2>📁 Upload Files</h2>
            <p>Upload your problem statement and Python solution</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="upload-card">', unsafe_allow_html=True)
            problem_file = st.file_uploader(
                "Select Problem Statement",
                type=['pdf', 'txt', 'doc', 'docx'],
                key="problem_uploader",
                help="Upload problem statement in PDF, TXT, or DOC format"
            )
            
            if problem_file:
                st.session_state.uploaded_files['problem'] = problem_file
                st.success(f"✅ Uploaded: {problem_file.name}")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="upload-card">', unsafe_allow_html=True)
            solution_file = st.file_uploader(
                "Select Python Solution",
                type=['py'],
                key="solution_uploader",
                help="Upload your Python solution file"
            )
            
            if solution_file:
                st.session_state.uploaded_files['solution'] = solution_file
                st.success(f"✅ Uploaded: {solution_file.name}")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Submit button
        submit_col1, submit_col2, submit_col3 = st.columns([1, 2, 1])
        with submit_col2:
            submit_button = st.button(
                "🚀 Submit for Review",
                type="primary",
                disabled=not (st.session_state.uploaded_files['problem'] and st.session_state.uploaded_files['solution']),
                use_container_width=True
            )
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Model Selection Section
    with st.container():
        st.markdown('<div class="glass-container">', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="section-header">
            <h2>🤖 AI Model Selection</h2>
            <p>Choose your preferred AI model for code review</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Model selection with radio buttons
        model_col1, model_col2, model_col3 = st.columns([1, 2, 1])
        with model_col2:
            selected_model = st.radio(
                "Select AI Model:",
                ["Gemini", "GPT-4", "Claude", "Copilot/Grok"],
                horizontal=True,
                key="model_selector"
            )
            st.session_state.selected_model = selected_model
        
        # Fetch comments button
        fetch_col1, fetch_col2, fetch_col3 = st.columns([1, 2, 1])
        with fetch_col2:
            if submit_button and st.session_state.uploaded_files['problem'] and st.session_state.uploaded_files['solution']:
                with st.spinner("🤖 AI is analyzing your code..."):
                    try:
                        # Parse files
                        file_parser = FileParser()
                        problem_text = file_parser.parse_file(st.session_state.uploaded_files['problem'])
                        solution_code = file_parser.parse_file(st.session_state.uploaded_files['solution'])
                        
                        # Build prompt
                        prompt_builder = PromptBuilder()
                        prompt = prompt_builder.build_review_prompt(problem_text, solution_code)
                        
                        # Get AI review based on selected model
                        if selected_model == "Gemini":
                            handler = GeminiHandler()
                            st.info("🤖 Using Gemini model for code review...")
                        elif selected_model == "GPT-4":
                            handler = OpenAIHandler()
                            st.info("🤖 Using OpenAI GPT model for code review...")
                        else:  # Claude
                            handler = ClaudeHandler()
                            st.info("🤖 Using Claude AI model for code review...")
                        
                        review_comments = handler.get_review(prompt)
                        
                        # Check for quota exceeded fallback message
                        if "⚠️ GPT-4 quota exceeded. Falling back to GPT-3.5-Turbo..." in review_comments:
                            st.warning("⚠️ GPT-4 quota exceeded. Falling back to GPT-3.5-Turbo...")
                            st.success("✅ Code review completed using GPT-3.5-Turbo!")
                        # Check if both GPT-4 and GPT-3.5 failed due to quota issues
                        elif "❌ GPT-4 quota exceeded and GPT-3.5 fallback failed" in review_comments:
                            st.error("OpenAI API quota exceeded. Please try using the Gemini model instead, or wait until your quota resets.")
                            # Add a button to switch to Gemini
                            if st.button("Switch to Gemini Model"):
                                st.session_state.selected_model = "Gemini"
                                st.experimental_rerun()
                        # Check if the response contains other error messages
                        elif "❌" in review_comments and ("API error" in review_comments or "quota exceeded" in review_comments or "insufficient_quota" in review_comments):
                            st.error("There was an issue with the selected AI model. Consider trying a different model.")
                        else:
                            st.success("✅ Code review completed!")
                            
                        st.session_state.review_comments = review_comments
                        
                    except Exception as e:
                        st.error(f"❌ Error during review: {str(e)}")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Output Section
    if st.session_state.review_comments:
        with st.container():
            st.markdown('<div class="glass-container">', unsafe_allow_html=True)
            
            st.markdown("""
            <div class="section-header">
                <h2>📝 AI Review Comments</h2>
                <p>Professional code review feedback</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Review comments display
            st.markdown('<div class="review-container">', unsafe_allow_html=True)
            
            # Display review with syntax highlighting
            st.markdown(st.session_state.review_comments)
            
            # Export options
            export_col1, export_col2, export_col3 = st.columns([1, 2, 1])
            with export_col2:
                col_export1, col_export2 = st.columns(2)
                with col_export1:
                    if st.button("📄 Export as TXT", use_container_width=True):
                        export_review_as_txt(st.session_state.review_comments)
                
                with col_export2:
                    if st.button("📊 Export as PDF", use_container_width=True):
                        export_review_as_pdf(st.session_state.review_comments)
            
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

def export_review_as_txt(review_text):
    """Export review comments as TXT file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"code_review_{timestamp}.txt"
    
    # Create download link
    st.download_button(
        label="📥 Download TXT",
        data=review_text,
        file_name=filename,
        mime="text/plain",
        use_container_width=True
    )

def export_review_as_pdf(review_text):
    """Export review comments as PDF file"""
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
        from reportlab.lib.styles import getSampleStyleSheet
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"code_review_{timestamp}.pdf"
        
        # Create PDF
        doc = SimpleDocTemplate(filename, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []
        
        # Add title
        title = Paragraph("AI Code Review Report", styles['Title'])
        story.append(title)
        story.append(Spacer(1, 12))
        
        # Add review content
        review_paragraph = Paragraph(review_text, styles['Normal'])
        story.append(review_paragraph)
        
        doc.build(story)
        
        # Read the generated PDF
        with open(filename, "rb") as f:
            pdf_data = f.read()
        
        # Create download link
        st.download_button(
            label="📥 Download PDF",
            data=pdf_data,
            file_name=filename,
            mime="application/pdf",
            use_container_width=True
        )
        
        # Clean up temporary file
        os.remove(filename)
        
    except ImportError:
        st.error("PDF export requires reportlab library. Install with: pip install reportlab")
    except Exception as e:
        st.error(f"Error creating PDF: {str(e)}")

if __name__ == "__main__":
    main()