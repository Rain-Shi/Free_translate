"""
Intelligent Document Translation and Format Fidelity System - Main Application
Based on innovative hybrid strategy: Structural Layer Extraction + Semantic-Aware Translation + Smart Format Reconstruction
"""

import streamlit as st
import tempfile
import os
from smart_translator import SmartDocumentTranslator, StructuralParser, SemanticTranslator, SmartReconstructor, FormatCorrector, DualViewEditor
import json

def main():
    st.set_page_config(
        page_title="Intelligent Document Translation and Format Fidelity System",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for advanced styling
    st.markdown("""
    <style>
    /* Main container styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    .main-title {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-subtitle {
        color: rgba(255,255,255,0.9);
        font-size: 1.2rem;
        margin-top: 0.5rem;
        font-weight: 300;
    }
    
    /* Feature cards */
    .feature-card {
        background: linear-gradient(145deg, #ffffff, #f0f0f0);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    }
    
    .feature-icon {
        font-size: 2rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    .feature-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 0.5rem;
    }
    
    .feature-desc {
        color: #7f8c8d;
        line-height: 1.6;
    }
    
    /* Upload area styling */
    .upload-area {
        background: linear-gradient(145deg, #f8f9fa, #e9ecef);
        border: 2px dashed #6c757d;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
        margin: 1rem 0;
    }
    
    .upload-area:hover {
        border-color: #007bff;
        background: linear-gradient(145deg, #e3f2fd, #bbdefb);
    }
    
    /* Status indicators */
    .status-success {
        background: linear-gradient(135deg, #28a745, #20c997);
        color: white;
        padding: 0.8rem 1.5rem;
        border-radius: 25px;
        font-weight: 500;
        box-shadow: 0 4px 15px rgba(40, 167, 69, 0.3);
    }
    
    .status-info {
        background: linear-gradient(135deg, #17a2b8, #6f42c1);
        color: white;
        padding: 0.8rem 1.5rem;
        border-radius: 25px;
        font-weight: 500;
        box-shadow: 0 4px 15px rgba(23, 162, 184, 0.3);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.8rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        box-shadow: 0 6px 20px rgba(255, 107, 107, 0.4);
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.6);
    }
    
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #2c3e50, #34495e);
    }
    
    /* Metrics styling */
    .metric-card {
        background: linear-gradient(145deg, #ffffff, #f8f9fa);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        border: 1px solid rgba(0,0,0,0.05);
    }
    
    /* Animation keyframes */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in-up {
        animation: fadeInUp 0.6s ease-out;
    }
    
    /* Gradient text */
    .gradient-text {
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Main header with gradient background
    st.markdown("""
    <div class="main-header fade-in-up">
        <h1 class="main-title">🤖 Intelligent Document Translation</h1>
        <p class="main-subtitle">Advanced Format Fidelity System with AI-Powered Translation</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar configuration
    with st.sidebar:
        st.header("⚙️ System Configuration")
        
        # API key settings
        api_key = st.text_input(
            "OpenAI API Key",
            type="password",
            help="Please enter your OpenAI API key"
        )
        
        if not api_key:
            st.warning("⚠️ Please set OpenAI API key first")
            st.stop()
        
        # Target language selection
        st.subheader("🌐 Translation Settings")
        target_languages = {
            'Chinese': 'Chinese',
            'English': 'English',
            'Japanese': 'Japanese',
            'Korean': 'Korean',
            'French': 'French',
            'German': 'German',
            'Spanish': 'Spanish',
            'Russian': 'Russian'
        }
        
        target_lang = st.selectbox(
            "Select Target Language",
            options=list(target_languages.keys()),
            index=0
        )
        target_lang_code = target_languages[target_lang]
        
        # Advanced features settings
        st.subheader("🔧 Advanced Features")
        
        # Proper noun protection
        use_proper_noun_protection = st.checkbox("Enable Proper Noun Protection", value=True)
        
        if use_proper_noun_protection:
            custom_proper_nouns = st.text_area(
                "Custom Proper Nouns (one per line)",
                value="GitHub\nOpenAI\nStreamlit\nPython\nJavaScript",
                height=100,
                help="Enter proper nouns to protect, one per line. The system has built-in common technical proper nouns."
            )
            st.info("ℹ️ Using built-in proper noun protection (GitHub, OpenAI, Python, etc.)")
        
        # Performance optimization
        use_performance_optimization = st.checkbox("Enable Performance Optimization", value=True, help="Use caching and batch processing to improve translation speed")
        if use_performance_optimization:
            st.info("🚀 Performance optimization enabled: Cache translation results, batch process short texts")
        
        # Display settings
        show_dual_view = st.checkbox("Show Left-Right Edit Interface", value=True, help="Show left-right split edit interface, can modify translated text and output final document")
    
    # Simplified main interface
    st.markdown('<div class="fade-in-up">', unsafe_allow_html=True)
    
    # Clean upload section
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("### 📄 Document Upload")
        uploaded_file = st.file_uploader(
            "Choose a Word document",
            type=['docx'],
            help="Upload a .docx file to translate",
            label_visibility="collapsed"
        )
        
        if uploaded_file:
            st.success(f"✅ {uploaded_file.name} uploaded successfully")
            st.info(f"📏 File size: {len(uploaded_file.getvalue())} bytes")
    
    with col2:
        st.markdown("### 📊 Status")
        if uploaded_file:
            st.success("🟢 Ready")
        else:
            st.warning("🟡 Upload document")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if uploaded_file is not None:
        # Save uploaded file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name
        
        # Initialize intelligent translation system
        translator_system = SmartDocumentTranslator()
        translator_system.set_translator(api_key)
        
        # Set proper noun protection
        if use_proper_noun_protection:
            if custom_proper_nouns:
                try:
                    # Parse custom proper nouns
                    custom_nouns = [noun.strip() for noun in custom_proper_nouns.split('\n') if noun.strip()]
                    translator_system.translator.add_proper_nouns(custom_nouns)
                    st.success(f"✅ Proper noun protection set, protecting {len(custom_nouns)} custom proper nouns")
                except Exception as e:
                    st.error(f"❌ Failed to set proper nouns: {str(e)}")
            else:
                st.info("ℹ️ Using built-in proper noun protection (GitHub, OpenAI, Python, etc.)")
        
        # Simple translation button
        if st.button("🚀 Start Translation", type="primary"):
            st.info("🔄 Processing document...")
            
            with st.spinner("Performing intelligent document translation..."):
                # Create output file path
                output_filename = f"translated_{uploaded_file.name}"
                with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as output_file:
                    output_path = output_file.name
                
                # Execute intelligent translation
                success = translator_system.process_document(
                    tmp_file_path, target_lang_code, output_path
                )
                
                if success:
                    st.success("🎉 Translation completed!")
                    
                    # Read generated file
                    with open(output_path, 'rb') as f:
                        file_data = f.read()
                    
                    st.download_button(
                        label="📥 Download Translated Document",
                        data=file_data,
                        file_name=output_filename,
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
                    
                    # Display translation completion information and paragraph comparison
                    if show_dual_view:
                        st.markdown("---")
                        st.subheader("📊 Translation Completed")
                        
                        # Display translation statistics
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            st.metric("Translation Status", "✅ Completed")
                        
                        with col2:
                            st.metric("Target Language", target_lang)
                        
                        with col3:
                            st.metric("File Size", f"{len(file_data)} bytes")
                        
                        # Display success message
                        st.success("🎉 Document translation completed! You can download the translated document.")
                        
                        # Simple display interface
                        st.markdown("---")
                        st.subheader("📄 Translation Results Display")
                        
                        # Initialize simple display interface
                        from simple_display_interface import SimpleDisplayInterface
                        display_interface = SimpleDisplayInterface()
                        
                        # Load documents for display
                        if display_interface.load_documents(tmp_file_path, output_path):
                            # Display translation summary
                            display_interface.display_translation_summary()
                            
                            # Display simple display interface
                            display_interface.display_simple_interface()
                            
                            # Final output
                            st.markdown("---")
                            st.subheader("📤 Final Output")
                            
                            if st.button("📄 Generate Final Document", type="primary"):
                                with st.spinner("Generating final document..."):
                                    final_output_path = tempfile.mktemp(suffix='.docx')
                                    
                                    if edit_interface.create_final_document(final_output_path):
                                        st.success("✅ Final document generated successfully!")
                                        
                                        # Read final document
                                        with open(final_output_path, 'rb') as f:
                                            final_data = f.read()
                                        
                                        # Provide download
                                        st.download_button(
                                            label="📥 Download Final Document",
                                            data=final_data,
                                            file_name=f"final_{uploaded_file.name}",
                                            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                                        )
                                        
                                        # Clean up temporary files
                                        try:
                                            os.unlink(final_output_path)
                                        except:
                                            pass
                                    else:
                                        st.error("❌ Final document generation failed")
                        else:
                            st.warning("⚠️ Unable to load documents for editing")
                        
                        # Display usage tips
                        st.info("💡 Tip: The translated document has maintained the original format and can be used directly.")
                    
                    # Clean up temporary files
                    try:
                        os.unlink(tmp_file_path)
                        os.unlink(output_path)
                    except:
                        pass
                
                else:
                    st.error("❌ 智能翻译失败，请检查文档格式和API密钥")
    
    # Simple usage instructions
    with st.expander("📖 How to Use", expanded=False):
        st.markdown("""
        **Quick Start:**
        1. Set your OpenAI API key in the sidebar
        2. Select target language
        3. Upload a .docx document
        4. Click "Start Translation"
        5. Download the translated document
        
        **Features:**
        - 🤖 AI-powered translation with OpenAI GPT
        - 🎨 Preserves original formatting
        - 🛡️ Protects proper nouns from translation
        - ⚡ Fast processing with caching
        """)

if __name__ == "__main__":
    main()
