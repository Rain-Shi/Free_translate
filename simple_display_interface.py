"""
Simple Display Interface - Only displays translation results, no editing functionality
"""

import streamlit as st
from docx import Document
from typing import List, Dict, Any
import tempfile
import os

class SimpleDisplayInterface:
    """Simple display interface - only displays translation results"""
    
    def __init__(self):
        self.original_paragraphs = []
        self.translated_paragraphs = []
    
    def load_documents(self, original_path: str, translated_path: str):
        """Load original and translated documents"""
        try:
            # Read original document
            original_doc = Document(original_path)
            self.original_paragraphs = [p.text.strip() for p in original_doc.paragraphs if p.text.strip()]
            
            # Read translated document
            translated_doc = Document(translated_path)
            self.translated_paragraphs = [p.text.strip() for p in translated_doc.paragraphs if p.text.strip()]
            
            st.success("✅ Documents loaded successfully!")
            return True
        except Exception as e:
            st.error(f"❌ Failed to load documents: {str(e)}")
            return False
    
    def display_simple_interface(self):
        """Display simple interface"""
        if not self.original_paragraphs or not self.translated_paragraphs:
            st.warning("⚠️ Please load documents first")
            return
        
        st.markdown("---")
        st.subheader("📄 Translation Results Display")
        
        # Display statistics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Original Paragraphs", len(self.original_paragraphs))
        
        with col2:
            st.metric("Translated Paragraphs", len(self.translated_paragraphs))
        
        with col3:
            st.metric("Translation Completion", "100%")
        
        # Display translation results comparison
        st.markdown("### 📊 Translation Results Comparison")
        
        # Use left-right column layout to display original and translated text
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📝 Original Text")
            for i, paragraph in enumerate(self.original_paragraphs):
                if paragraph.strip():
                    st.markdown(f"**Paragraph {i+1}:**")
                    st.text_area(
                        f"Original Paragraph {i+1}",
                        value=paragraph,
                        height=100,
                        key=f"original_display_{i}",
                        disabled=True
                    )
                    st.markdown(f"Word count: {len(paragraph)}")
                    st.markdown("---")
        
        with col2:
            st.markdown("#### 🌐 Translated Text")
            for i, paragraph in enumerate(self.translated_paragraphs):
                if paragraph.strip():
                    st.markdown(f"**Paragraph {i+1}:**")
                    st.text_area(
                        f"Translated Paragraph {i+1}",
                        value=paragraph,
                        height=100,
                        key=f"translated_display_{i}",
                        disabled=True
                    )
                    st.markdown(f"Word count: {len(paragraph)}")
                    st.markdown("---")
        
        # Display translation statistics
        self._display_translation_stats()
    
    def _display_translation_stats(self):
        """Display translation statistics"""
        st.markdown("### 📈 Translation Statistics")
        
        # Calculate statistics
        total_original_chars = sum(len(p) for p in self.original_paragraphs)
        total_translated_chars = sum(len(p) for p in self.translated_paragraphs)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Original Total Characters", total_original_chars)
        
        with col2:
            st.metric("Translated Total Characters", total_translated_chars)
        
        with col3:
            length_ratio = total_translated_chars / total_original_chars if total_original_chars > 0 else 1
            st.metric("Length Ratio", f"{length_ratio:.2f}")
        
        with col4:
            st.metric("Paragraph Count", len(self.original_paragraphs))
    
    def get_translation_summary(self):
        """Get translation summary"""
        if not self.original_paragraphs or not self.translated_paragraphs:
            return {}
        
        total_original_chars = sum(len(p) for p in self.original_paragraphs)
        total_translated_chars = sum(len(p) for p in self.translated_paragraphs)
        
        return {
            'total_paragraphs': len(self.original_paragraphs),
            'total_original_chars': total_original_chars,
            'total_translated_chars': total_translated_chars,
            'length_ratio': total_translated_chars / total_original_chars if total_original_chars > 0 else 1
        }
    
    def display_translation_summary(self):
        """Display translation summary"""
        summary = self.get_translation_summary()
        
        if summary:
            st.markdown("### 📊 Translation Summary")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Total Paragraphs", summary['total_paragraphs'])
            
            with col2:
                st.metric("Original Total Characters", summary['total_original_chars'])
            
            with col3:
                st.metric("Translated Total Characters", summary['total_translated_chars'])
            
            # Length ratio
            st.markdown(f"**Length Ratio**: {summary['length_ratio']:.2f}")
            
            # Translation quality assessment
            if summary['length_ratio'] > 0.8 and summary['length_ratio'] < 1.2:
                st.success("✅ Translation length is reasonable")
            elif summary['length_ratio'] > 1.2:
                st.warning("⚠️ Translated text is longer, may need adjustment")
            else:
                st.warning("⚠️ Translated text is shorter, may need adjustment")
