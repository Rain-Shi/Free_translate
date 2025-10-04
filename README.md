# 🤖 智能文档翻译与格式保真系统

> 一个被收费翻译逼出来的开源项目 - 基于创新的混合策略：**结构分层解析 + 语义增强翻译 + 格式智能重建**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5--turbo-green.svg)](https://openai.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Rain-Shi/Free_translate.svg)](https://github.com/Rain-Shi/Free_translate/stargazers)

## 📖 项目起源

这个故事要从一个教授的翻译任务说起...

当时需要翻译大量学术文档，试了一圈发现：
- **百度翻译**：要钱 💰
- **DeepL**：要钱 💰  
- **有道翻译**：要钱 💰

**我气不过就是不想给！** 😤

于是决定手搓一个文档翻译工具。参考了GitHub上的优秀案例：
- [document-translation](https://github.com/kukas/document-translation) 
- [DocuTranslate](https://github.com/xunbu/docutranslate)
- [TransDoc](https://github.com/abner-wong/transdoc)

但是实在太懒了，抄都不想抄，想搞点自己的名堂 🤔

## 🚀 核心功能

### 1. 智能文档翻译
- **OpenAI GPT-3.5-turbo**：使用先进的AI模型进行高质量翻译
- **多语言支持**：支持多种目标语言翻译
- **上下文理解**：保持翻译的连贯性和准确性

### 2. 格式保真系统
- **结构分层解析**：将Word文档拆分为内容层、格式层、布局层
- **格式智能重建**：翻译后重建文档，保持原有格式
- **字体统一**：自动提取原文档字体并应用到翻译结果

### 3. 专有名词保护
- **内置保护**：自动保护GitHub、OpenAI、Python等技术术语
- **自定义保护**：支持用户添加自定义专有名词
- **智能识别**：避免专有名词被错误翻译

### 4. 性能优化
- **缓存机制**：缓存翻译结果，避免重复翻译
- **批量处理**：优化短文本的批量翻译
- **重复内容检测**：自动检测和避免重复翻译

### 5. 结果展示
- **双标签页展示**：分别展示原文和译文
- **翻译统计**：显示字数统计、长度比例等
- **质量评估**：自动评估翻译质量

## 🎯 核心优势

### 相比传统翻译工具

| 功能 | 传统方法 | 本系统 | 优势 |
|------|---------|--------|------|
| 格式保持 | 容易丢失 | 智能保持 | 结构分层解析 |
| 专有名词 | 无法控制 | 智能保护 | 专有名词保护 |
| 翻译质量 | 基础翻译 | AI增强 | OpenAI GPT |
| 用户体验 | 单向处理 | 结果展示 | 双标签页展示 |
| 费用 | 按量收费 | 完全免费 | 开源免费 |

### 相比现有开源方案

- **document-translation**: 侧重批量处理，保留标记，但缺乏 AI 语境优化
- **DocuTranslate**: 保留格式较好，但 run 级写回容易导致翻译后文本分布不均衡
- **TransDoc**: 解压 XML 处理方式能保留格式，但开发复杂度高，且翻译上下文有限

**我们的方案**：结合各家优势，用结构分层解析 + AI语义翻译 + 格式智能重建，既保持格式又提升质量。

## 🚀 快速开始

### 环境要求

- Python 3.8+
- OpenAI API密钥（或者用其他LLM）
- 8GB+ RAM (推荐)

### 安装步骤

1. **克隆项目**
```bash
git clone https://github.com/Rain-Shi/Free_translate.git
cd Free_translate
```

2. **创建虚拟环境**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **安装依赖**
```bash
pip install -r requirements.txt
```

4. **启动应用**
```bash
# Windows
start_app.bat
# Linux/Mac
./start_app.sh
# 或直接运行
streamlit run smart_app.py
```

5. **访问应用**
打开浏览器访问：http://localhost:8501

## 📖 使用指南

### 基础使用

1. **设置API密钥**：在侧边栏输入OpenAI API密钥
2. **选择目标语言**：选择要翻译的目标语言
3. **上传Word文档**：选择.docx格式的Word文档
4. **开始翻译**：点击"🚀 开始智能翻译"
5. **查看结果**：使用双标签页查看原文和译文

### 高级功能

#### 专有名词保护
- **启用专有名词保护**：在侧边栏勾选"启用专有名词保护"
- **自定义专有名词**：在文本框中输入自定义专有名词，每行一个
- **内置保护**：自动保护GitHub、OpenAI、Python等技术术语

#### 性能优化
- **启用性能优化**：在侧边栏勾选"启用性能优化"
- **缓存机制**：自动缓存翻译结果，避免重复翻译
- **批量处理**：优化短文本的批量翻译

## 🔧 技术架构

### 核心技术栈

- **前端框架**：Streamlit
- **文档处理**：python-docx, pypandoc
- **AI翻译**：OpenAI GPT-3.5-turbo
- **格式转换**：Pandoc
- **数据处理**：Python 3.8+

### 系统组件

```
smart_translator.py          # 核心翻译引擎
├── StructuralParser         # 结构分层解析器
├── SemanticTranslator       # 语义增强翻译器
├── SmartReconstructor       # 格式智能重建器
└── DualViewEditor           # 双视图编辑器

smart_app.py                 # 主应用界面
├── 用户界面组件
├── 高级功能配置
├── 重复内容检测
└── 质量评估显示

simple_display_interface.py # 简单展示界面
├── 双标签页展示
├── 翻译统计
└── 质量评估
```

## 🎯 应用场景

### 1. 学术论文翻译
- **专有名词保护**：确保专业术语不被错误翻译
- **格式保持**：完美保持论文格式
- **AI翻译**：使用OpenAI GPT进行高质量翻译

### 2. 商务文档翻译
- **合同翻译**：精确保持法律文档格式
- **报告翻译**：保持商务报告结构
- **提案翻译**：维持专业商务风格

### 3. 技术文档翻译
- **API文档**：保持代码格式和结构
- **用户手册**：维持操作指南格式
- **技术规范**：确保技术术语一致

## ⚠️ 重要说明

**本项目仅为满足教授一次性翻译任务而开发，当生成结果效果不错时任务就结束了。由于缺乏充分的数据测试，使用请谨慎！**

- 🎯 **开发目的**：解决教授翻译任务，避免付费翻译工具
- ⚠️ **测试状态**：缺乏充分测试，可能存在未知问题
- 🔧 **使用建议**：建议先在小文档上测试，确认效果后再处理重要文档
- 📝 **免责声明**：使用本工具产生的任何问题，开发者不承担责任

## 🔍 问题解决

### 常见问题

1. **Q: 翻译后格式丢失怎么办？**
   A: 系统会自动进行格式智能重建，保持原有格式。

2. **Q: 专业术语翻译不一致？**
   A: 使用专有名词保护功能，在侧边栏添加自定义专有名词。

3. **Q: 翻译速度慢？**
   A: 启用性能优化功能，系统会自动缓存和批量处理。

4. **Q: 表格内容重复显示？**
   A: 系统已优化表格处理，自动去重避免重复。

### 故障排除

- **API密钥错误**：检查OpenAI API密钥是否正确
- **文档格式问题**：确保使用.docx格式
- **内存不足**：大文档建议分段处理
- **网络问题**：检查网络连接和API访问

## 🤝 贡献指南

我们欢迎社区贡献！请遵循以下步骤：

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- 感谢 [document-translation](https://github.com/kukas/document-translation) 的启发
- 感谢 [DocuTranslate](https://github.com/xunbu/docutranslate) 的参考
- 感谢 [TransDoc](https://github.com/abner-wong/transdoc) 的思路
- 感谢 OpenAI 提供的强大AI翻译能力
- 感谢 Streamlit 提供的优秀Web框架
- 感谢所有贡献者和用户的支持

## 📞 联系我们

- **项目主页**：https://github.com/Rain-Shi/Free_translate
- **问题反馈**：https://github.com/Rain-Shi/Free_translate/issues

---

**🎉 感谢使用！让我们一起推动文档翻译技术的进步！**

## ⭐ 如果这个项目对您有帮助，请给我们一个Star！

**毕竟，我们也不想给那些收费翻译工具送钱！** 😄