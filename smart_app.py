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
        layout="wide"
    )
    
    st.title("🤖 Intelligent Document Translation and Format Fidelity System")
    st.markdown("---")
    
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
    
    # Main interface
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📁 Document Upload")
        uploaded_file = st.file_uploader(
            "Select Word Document",
            type=['docx'],
            help="Supports .docx format Word documents"
        )
    
    with col2:
        st.subheader("📊 System Status")
        if uploaded_file:
            st.success("✅ Document uploaded")
            st.info(f"📄 File name: {uploaded_file.name}")
            st.info(f"📏 File size: {len(uploaded_file.getvalue())} bytes")
        else:
            st.warning("⚠️ Please upload Word document")
    
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
        
        # Process button
        if st.button("🚀 Start Intelligent Translation", type="primary"):
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
                    st.success("🎉 Intelligent translation completed!")
                    
                    # Display processing results
                    st.subheader("📊 Processing Results")
                    
                    # Read generated file
                    with open(output_path, 'rb') as f:
                        file_data = f.read()
                    
                    # Provide download
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
    
    # System description
    st.markdown("---")
    st.subheader("📖 Usage Instructions")
    
    st.markdown("""
    ### 🚀 Feature Characteristics
    
    1. **Intelligent Translation**: Uses OpenAI GPT models for high-quality translation
    2. **Format Preservation**: Maintains original document format, styles and layout
    3. **Proper Noun Protection**: Automatically protects technical terms and proper nouns from translation
    4. **Performance Optimization**: Supports caching and batch processing to improve translation speed
    
    ### 📝 Usage Steps
    
    1. **Set API Key**: Enter OpenAI API key in the sidebar
    2. **Select Target Language**: Choose the target language for translation
    3. **Upload Document**: Upload .docx format Word document
    4. **Start Translation**: Click "Start Intelligent Translation" button
    5. **Download Results**: Download the translated document
    
    ### ⚠️ Notes
    
    - Only supports .docx format Word documents
    - Requires valid OpenAI API key
    - Translation quality depends on document complexity and API quota
    - Recommend testing with small documents first, then process larger documents after confirming effectiveness
    """)

if __name__ == "__main__":
    main()
