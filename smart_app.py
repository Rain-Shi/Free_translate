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
        
        # 术语锁定
        st.markdown("**术语锁定设置**")
        use_terminology = st.checkbox("启用术语锁定", value=False)
        terminology_text = ""
        if use_terminology:
            terminology_text = st.text_area(
                "术语对照表 (JSON格式)",
                value='{"API": "API", "AI": "人工智能", "ML": "机器学习"}',
                height=100,
                help="输入JSON格式的术语对照表，确保专业术语翻译一致"
            )
        
        # 风格模仿
        st.markdown("**风格模仿设置**")
        use_style_imitation = st.checkbox("启用风格模仿", value=False)
        style_examples = ""
        if use_style_imitation:
            style_examples = st.text_area(
                "风格示例 (JSON格式)",
                value='{"formal": "正式", "technical": "技术性", "academic": "学术性"}',
                height=100,
                help="输入风格示例，让AI模仿特定的翻译风格"
            )
        
        # 专有名词保护
        st.markdown("**专有名词保护设置**")
        use_proper_noun_protection = st.checkbox("启用专有名词保护", value=True)
        custom_proper_nouns = ""
        if use_proper_noun_protection:
            custom_proper_nouns = st.text_area(
                "自定义专有名词 (每行一个)",
                value="GitHub\nOpenAI\nStreamlit\nPython\nJavaScript",
                height=100,
                help="输入需要保护的专有名词，每行一个。系统已内置常见技术专有名词。"
            )
        
        # 格式纠错
        st.markdown("**格式纠错设置**")
        auto_format_correction = st.checkbox("自动格式纠错", value=True)
        show_dual_view = st.checkbox("显示双视图编辑器", value=True)
    
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
        
        # 设置术语锁定
        if use_terminology and terminology_text:
            try:
                terminology_dict = json.loads(terminology_text)
                translator_system.translator.set_terminology(terminology_dict)
                st.success("✅ 术语锁定已设置")
            except json.JSONDecodeError:
                st.error("❌ 术语对照表格式错误，请使用正确的JSON格式")
        
        # 设置风格模仿
        if use_style_imitation and style_examples:
            try:
                style_dict = json.loads(style_examples)
                translator_system.translator.set_style_examples(style_dict)
                st.success("✅ 风格模仿已设置")
            except json.JSONDecodeError:
                st.error("❌ 风格示例格式错误，请使用正确的JSON格式")
        
        # 设置专有名词保护
        if use_proper_noun_protection and custom_proper_nouns:
            try:
                # 解析自定义专有名词
                custom_nouns = [noun.strip() for noun in custom_proper_nouns.split('\n') if noun.strip()]
                translator_system.translator.add_proper_nouns(custom_nouns)
                st.success(f"✅ 专有名词保护已设置，共保护 {len(custom_nouns)} 个自定义专有名词")
            except Exception as e:
                st.error(f"❌ 专有名词设置失败: {str(e)}")
        elif use_proper_noun_protection:
            st.info("ℹ️ 使用内置专有名词保护（GitHub、OpenAI、Python等）")
        
        # 处理按钮
        if st.button("🚀 开始智能翻译", type="primary"):
            with st.spinner("正在进行智能文档翻译..."):
                # 创建输出文件路径
                output_filename = f"smart_translated_{uploaded_file.name}"
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
                    
                    # 显示双视图编辑器
                    if show_dual_view:
                        st.markdown("---")
                        st.subheader("📖 双视图编辑器")
                        
                        # 解析原文档和翻译后的文档
                        parser = StructuralParser()
                        original_parsed = parser.parse_document(tmp_file_path)
                        translated_parsed = parser.parse_document(output_path)
                        
                        if original_parsed and translated_parsed:
                            # 检测重复内容
                            st.info("🔍 正在检测重复内容...")
                            
                            # 统计重复内容
                            original_texts = [item['text'] for item in original_parsed['content_layer'] if item['text'].strip()]
                            translated_texts = [item['text'] for item in translated_parsed['content_layer'] if item['text'].strip()]
                            
                            # 检测重复
                            original_duplicates = len(original_texts) - len(set(original_texts))
                            translated_duplicates = len(translated_texts) - len(set(translated_texts))
                            
                            if original_duplicates > 0 or translated_duplicates > 0:
                                st.warning(f"⚠️ 检测到重复内容: 原文 {original_duplicates} 处，译文 {translated_duplicates} 处")
                                
                                # 显示重复内容统计
                                col1, col2 = st.columns(2)
                                with col1:
                                    st.metric("原文重复", original_duplicates)
                                with col2:
                                    st.metric("译文重复", translated_duplicates)
                            
                            # 创建双视图编辑器
                            editor = DualViewEditor()
                            editor.display_dual_view(
                                original_parsed['content_layer'],
                                translated_parsed['content_layer']
                            )
                    
                    # 格式纠错报告
                    if auto_format_correction:
                        st.markdown("---")
                        st.subheader("🔍 格式纠错报告")
                        
                        corrector = FormatCorrector()
                        issues = corrector.detect_format_issues(output_path)
                        
                        if issues:
                            st.warning(f"发现 {len(issues)} 个格式问题:")
                            for i, issue in enumerate(issues, 1):
                                st.write(f"{i}. **{issue['type']}**: {issue['description']}")
                                st.write(f"   建议: {issue['suggestion']}")
                        else:
                            st.success("✅ 未发现格式问题，文档格式完美！")
                    
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
    st.subheader("🤖 系统特性")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🔍 结构分层解析**
        - 内容层：纯文本提取
        - 格式层：样式信息保持
        - 布局层：结构信息维护
        """)
    
    with col2:
        st.markdown("""
        **🤖 语义增强翻译**
        - 上下文记忆
        - 术语锁定
        - 风格模仿
        """)
    
    with col3:
        st.markdown("""
        **🔧 格式智能重建**
        - 锚点映射
        - 智能行宽调整
        - 自动格式纠错
        """)
    
    # 使用说明
    st.markdown("---")
    st.subheader("📖 使用说明")
    
    st.markdown("""
    ### 🚀 创新特性
    
    1. **结构分层解析**: 将Word文档分解为内容层、格式层、布局层，确保翻译时格式不丢失
    
    2. **语义增强翻译**: 使用大语言模型进行上下文感知翻译，支持术语锁定和风格模仿
    
    3. **格式智能重建**: 利用锚点映射技术，智能重建文档结构，处理翻译长度变化
    
    4. **双视图编辑器**: 左右对比显示原文和译文，支持实时编辑和同步
    
    5. **自动格式纠错**: 检测和修复翻译后的排版问题，确保文档质量
    
    ### 💡 使用技巧
    
    - **术语锁定**: 输入JSON格式的术语对照表，确保专业术语翻译一致
    - **风格模仿**: 提供风格示例，让AI模仿特定的翻译风格
    - **双视图编辑**: 使用双视图编辑器进行精细调整
    - **格式纠错**: 启用自动格式纠错，确保最终文档质量
    """)

if __name__ == "__main__":
    main()
