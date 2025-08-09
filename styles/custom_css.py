import streamlit as st

def load_css():
    """Load custom CSS for modern styling"""
    
    css = """
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* Header Styling */
    .header-container {
        text-align: center;
        margin-bottom: 3rem;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .main-title {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        font-size: 3rem;
        color: white;
        margin: 0;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .subtitle {
        font-family: 'Inter', sans-serif;
        font-weight: 400;
        font-size: 1.2rem;
        color: rgba(255, 255, 255, 0.9);
        margin: 0.5rem 0 0 0;
    }
    

    
    /* Section Headers */
    .section-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .section-header h2 {
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 2rem;
        color: #2d3748;
        margin: 0 0 0.5rem 0;
    }
    
    .section-header p {
        font-family: 'Inter', sans-serif;
        font-weight: 400;
        font-size: 1rem;
        color: #718096;
        margin: 0;
    }
    
   
    }
    
    /* Review Container */
    .review-container {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin: 1rem 0;
    }
    
    /* Button Styling */
    .stButton > button {
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        transition: all 0.3s ease;
        border: none;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
    }
    
    /* File Uploader Styling */
    .stFileUploader > div > div {
        border-radius: 12px;
        border: 2px dashed rgba(102, 126, 234, 0.3);
        background: rgba(255, 255, 255, 0.05);
        transition: all 0.3s ease;
    }
    
    .stFileUploader > div > div:hover {
        border-color: rgba(102, 126, 234, 0.6);
        background: rgba(255, 255, 255, 0.1);
    }
    
    /* Radio Button Styling */
    .stRadio > div {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Success/Error Messages */
    .stSuccess {
        background: rgba(72, 187, 120, 0.1);
        border: 1px solid rgba(72, 187, 120, 0.3);
        border-radius: 8px;
        padding: 0.75rem;
        margin: 0.5rem 0;
    }
    
    .stError {
        background: rgba(245, 101, 101, 0.1);
        border: 1px solid rgba(245, 101, 101, 0.3);
        border-radius: 8px;
        padding: 0.75rem;
        margin: 0.5rem 0;
    }
    
    /* Code Block Styling */
    .stMarkdown code {
        background: rgba(45, 55, 72, 0.1);
        border-radius: 6px;
        padding: 0.25rem 0.5rem;
        font-family: 'Fira Code', monospace;
        font-size: 0.9rem;
    }
    
    .stMarkdown pre {
        background: rgba(45, 55, 72, 0.05);
        border-radius: 8px;
        padding: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Spinner Styling */
    .stSpinner > div {
        border-color: #667eea;
    }
    
    /* Download Button Styling */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stDownloadButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2rem;
        }
        
        .subtitle {
            font-size: 1rem;
        }
        
        .glass-container {
            padding: 1rem;
            margin: 0.5rem 0;
        }
        
        .section-header h2 {
            font-size: 1.5rem;
        }
    }
    
    /* Dark mode support */
    @media (prefers-color-scheme: dark) {
        .glass-container {
            background: rgba(0, 0, 0, 0.2);
            border-color: rgba(255, 255, 255, 0.1);
        }
        
        .section-header h2 {
            color: #e2e8f0;
        }
        
        .section-header p {
            color: #a0aec0;
        }
    }
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: rgba(102, 126, 234, 0.5);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(102, 126, 234, 0.7);
    }
    
    /* Animation for loading states */
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    
    .loading {
        animation: pulse 2s infinite;
    }
    
    /* Custom focus styles */
    .stButton > button:focus,
    .stFileUploader > div > div:focus-within {
        outline: 2px solid rgba(102, 126, 234, 0.5);
        outline-offset: 2px;
    }
    
    /* Enhanced typography */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        color: #2d3748;
    }
    
    .stMarkdown p, .stMarkdown li {
        font-family: 'Inter', sans-serif;
        line-height: 1.6;
        color: #4a5568;
    }
    
    /* Table styling */
    .stMarkdown table {
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    
    .stMarkdown th {
        background: rgba(102, 126, 234, 0.1);
        font-weight: 600;
        color: #2d3748;
    }
    
    .stMarkdown td {
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    </style>
    """
    
    st.markdown(css, unsafe_allow_html=True) 