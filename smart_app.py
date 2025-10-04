"""
智能文档翻译与格式保真系统 - 主应用
基于创新的混合策略：结构分层解析 + 语义增强翻译 + 格式智能重建
"""

import streamlit as st
import tempfile
import os
from smart_translator import SmartDocumentTranslator, StructuralParser, SemanticTranslator, SmartReconstructor, FormatCorrector, DualViewEditor
import json

def main():
    st.set_page_config(
        page_title="智能文档翻译与格式保真系统",
        page_icon="🤖",
        layout="wide"
    )
    
    st.title("🤖 智能文档翻译与格式保真系统")
    st.markdown("---")
    
    # 侧边栏配置
    with st.sidebar:
        st.header("⚙️ 系统配置")
        
        # API密钥设置
        api_key = st.text_input(
            "OpenAI API密钥",
            type="password",
            help="请输入您的OpenAI API密钥"
        )
        
        if not api_key:
            st.warning("⚠️ 请先设置OpenAI API密钥")
            st.stop()
        
        # 目标语言选择
        st.subheader("🌐 翻译设置")
        target_languages = {
            '中文': 'Chinese',
            '英文': 'English',
            '日文': 'Japanese',
            '韩文': 'Korean',
            '法文': 'French',
            '德文': 'German',
            '西班牙文': 'Spanish',
            '俄文': 'Russian'
        }
        
        target_lang = st.selectbox(
            "选择目标语言",
            options=list(target_languages.keys()),
            index=0
        )
        target_lang_code = target_languages[target_lang]
        
        # 高级功能设置
        st.subheader("🔧 高级功能")
        
        # 专有名词保护
        use_proper_noun_protection = st.checkbox("启用专有名词保护", value=True)
        
        if use_proper_noun_protection:
            custom_proper_nouns = st.text_area(
                "自定义专有名词 (每行一个)",
                value="GitHub\nOpenAI\nStreamlit\nPython\nJavaScript",
                height=100,
                help="输入需要保护的专有名词，每行一个。系统已内置常见技术专有名词。"
            )
            st.info("ℹ️ 使用内置专有名词保护（GitHub、OpenAI、Python等）")
        
        # 性能优化
        use_performance_optimization = st.checkbox("启用性能优化", value=True, help="使用缓存和批量处理提升翻译速度")
        if use_performance_optimization:
            st.info("🚀 性能优化已启用：缓存翻译结果，批量处理短文本")
        
        # 显示设置
        show_dual_view = st.checkbox("显示翻译统计", value=True)
    
    # 主界面
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📁 文档上传")
        uploaded_file = st.file_uploader(
            "选择Word文档",
            type=['docx'],
            help="支持.docx格式的Word文档"
        )
    
    with col2:
        st.subheader("📊 系统状态")
        if uploaded_file:
            st.success("✅ 文档已上传")
            st.info(f"📄 文件名: {uploaded_file.name}")
            st.info(f"📏 文件大小: {len(uploaded_file.getvalue())} bytes")
        else:
            st.warning("⚠️ 请上传Word文档")
    
    if uploaded_file is not None:
        # 保存上传的文件
        with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name
        
        # 初始化智能翻译系统
        translator_system = SmartDocumentTranslator()
        translator_system.set_translator(api_key)
        
        # 设置专有名词保护
        if use_proper_noun_protection:
            if custom_proper_nouns:
                try:
                    # 解析自定义专有名词
                    custom_nouns = [noun.strip() for noun in custom_proper_nouns.split('\n') if noun.strip()]
                    translator_system.translator.add_proper_nouns(custom_nouns)
                    st.success(f"✅ 专有名词保护已设置，共保护 {len(custom_nouns)} 个自定义专有名词")
                except Exception as e:
                    st.error(f"❌ 专有名词设置失败: {str(e)}")
            else:
                st.info("ℹ️ 使用内置专有名词保护（GitHub、OpenAI、Python等）")
        
        # 处理按钮
        if st.button("🚀 开始智能翻译", type="primary"):
            with st.spinner("正在进行智能文档翻译..."):
                # 创建输出文件路径
                output_filename = f"translated_{uploaded_file.name}"
                with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as output_file:
                    output_path = output_file.name
                
                # 执行智能翻译
                success = translator_system.process_document(
                    tmp_file_path, target_lang_code, output_path
                )
                
                if success:
                    st.success("🎉 智能翻译完成！")
                    
                    # 显示处理结果
                    st.subheader("📊 处理结果")
                    
                    # 读取生成的文件
                    with open(output_path, 'rb') as f:
                        file_data = f.read()
                    
                    # 提供下载
                    st.download_button(
                        label="📥 下载翻译后的文档",
                        data=file_data,
                        file_name=output_filename,
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
                    
                    # 显示翻译完成信息
                    if show_dual_view:
                        st.markdown("---")
                        st.subheader("📊 翻译完成")
                        
                        # 显示翻译统计
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            st.metric("翻译状态", "✅ 完成")
                        
                        with col2:
                            st.metric("目标语言", target_lang)
                        
                        with col3:
                            st.metric("文件大小", f"{len(file_data)} bytes")
                        
                        # 显示成功信息
                        st.success("🎉 文档翻译完成！您可以下载翻译后的文档。")
                        
                        # 显示使用提示
                        st.info("💡 提示：翻译后的文档已保持原有格式，可以直接使用。")
                    
                    # 清理临时文件
                    try:
                        os.unlink(tmp_file_path)
                        os.unlink(output_path)
                    except:
                        pass
                
                else:
                    st.error("❌ 智能翻译失败，请检查文档格式和API密钥")
    
    # 系统说明
    st.markdown("---")
    st.subheader("📖 使用说明")
    
    st.markdown("""
    ### 🚀 功能特性
    
    1. **智能翻译**: 使用OpenAI GPT模型进行高质量翻译
    2. **格式保持**: 保持原文档的格式、样式和布局
    3. **专有名词保护**: 自动保护技术术语和专有名词不被翻译
    4. **性能优化**: 支持缓存和批量处理，提升翻译速度
    
    ### 📝 使用步骤
    
    1. **设置API密钥**: 在侧边栏输入OpenAI API密钥
    2. **选择目标语言**: 选择要翻译成的目标语言
    3. **上传文档**: 上传.docx格式的Word文档
    4. **开始翻译**: 点击"开始智能翻译"按钮
    5. **下载结果**: 下载翻译后的文档
    
    ### ⚠️ 注意事项
    
    - 仅支持.docx格式的Word文档
    - 需要有效的OpenAI API密钥
    - 翻译质量取决于文档复杂度和API配额
    - 建议先测试小文档，确认效果后再处理大文档
    """)

if __name__ == "__main__":
    main()
