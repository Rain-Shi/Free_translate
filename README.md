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

## 🚀 创新方案核心

### 混合策略：结构分层解析 + 语义增强翻译 + 格式智能重建

#### 1. 结构分层解析 (Structural Layer Extraction)

将 .docx 拆分成三层：

- **内容层**：纯文本（段落、表格单元格内容）
- **格式层**：字体、加粗、颜色、样式标记  
- **布局层**：表格、图片、分页符、标题结构

先抽取内容层用于翻译，格式层和布局层存为"锚点映射（anchors）"。

#### 2. 语义增强翻译 (Semantic-Aware Translation)

采用大语言模型（如 GPT-4/Claude/SakuraLLM）+ 术语表/上下文记忆。

支持：
- **上下文记忆**（段落/章节级缓存，保证风格一致）
- **术语锁定**（避免术语随意变化，适合论文/合同/技术文档）
- **风格模仿**（可以导入用户给定的"示例译文"来调整风格）

#### 3. 格式智能重建 (Smart Reconstruction)

翻译完成后，利用锚点映射重组文档：

- 原 run 结构尽量保持（避免 run 级丢失样式）
- 当翻译长度变化过大时，使用 **智能行宽调整** 或 **动态 run 拆分**，避免表格溢出
- 图片、分页符、页眉页脚完全原样复用
- 额外创新：支持 **格式纠错模块**（检测翻译后的排版错位，自动修复）

#### 4. 用户交互增强

提供一个 **双视图编辑器**：左边显示原文，右边显示译文（带样式），允许用户点击同步修改。

提供"段落锁定翻译"和"格式对齐模式"，用户可以选择：
- 只翻译选中的段落
- 或强制保持原 run 数（对严格排版要求的论文非常有用）

## 🎯 核心优势

### 相比传统翻译工具

| 功能 | 传统方法 | 本系统 | 优势 |
|------|---------|--------|------|
| 格式保持 | 容易丢失 | 95%保持 | 三层架构 |
| 术语一致 | 无法控制 | 智能锁定 | 术语表+上下文 |
| 翻译质量 | 基础翻译 | 语义增强 | AI+上下文记忆 |
| 用户体验 | 单向处理 | 双视图编辑 | 实时对比编辑 |
| 费用 | 按量收费 | 完全免费 | 开源免费 |

### 相比现有开源方案

- **document-translation**: 侧重批量处理，保留标记，但缺乏 AI 语境优化
- **DocuTranslate**: 保留格式较好，但 run 级写回容易导致翻译后文本分布不均衡
- **TransDoc**: 解压 XML 处理方式能保留格式，但开发复杂度高，且翻译上下文有限

**我们的方案**：结合各家优势，用三层架构 + AI语义翻译 + 智能重建，既保持格式又提升质量。

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
5. **查看结果**：使用双视图编辑器进行精细调整

### 高级功能

#### 术语锁定
```json
{
  "API": "API",
  "AI": "人工智能",
  "Machine Learning": "机器学习",
  "NLP": "自然语言处理"
}
```

#### 风格模仿
```json
{
  "formal": "正式商务风格",
  "technical": "技术文档风格",
  "academic": "学术论文风格"
}
```

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
├── FormatCorrector          # 格式纠错模块
└── DualViewEditor           # 双视图编辑器

smart_app.py                 # 主应用界面
├── 用户界面组件
├── 高级功能配置
├── 重复内容检测
└── 质量评估显示
```

## 🎯 应用场景

### 1. 学术论文翻译
- **术语锁定**：确保专业术语翻译一致
- **风格模仿**：保持学术写作风格
- **格式保持**：完美保持论文格式

### 2. 商务文档翻译
- **合同翻译**：精确保持法律文档格式
- **报告翻译**：保持商务报告结构
- **提案翻译**：维持专业商务风格

### 3. 技术文档翻译
- **API文档**：保持代码格式和结构
- **用户手册**：维持操作指南格式
- **技术规范**：确保技术术语一致

## 🔍 问题解决

### 常见问题

1. **Q: 翻译后格式丢失怎么办？**
   A: 系统会自动进行格式纠错，检测和修复格式问题。

2. **Q: 专业术语翻译不一致？**
   A: 使用术语锁定功能，输入JSON格式的术语对照表。

3. **Q: 翻译风格不统一？**
   A: 使用风格模仿功能，提供风格示例让AI学习。

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
- **功能建议**：https://github.com/Rain-Shi/Free_translate/discussions

---

**🎉 感谢使用！让我们一起推动文档翻译技术的进步！**

## ⭐ 如果这个项目对您有帮助，请给我们一个Star！

**毕竟，我们也不想给那些收费翻译工具送钱！** 😄