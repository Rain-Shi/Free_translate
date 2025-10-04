# 🤖 Intelligent Document Translation and Format Fidelity System

> An open-source project born out of frustration with paid translation services - Based on innovative hybrid strategy: **Structural Layer Extraction + Semantic-Aware Translation + Smart Format Reconstruction**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5--turbo-green.svg)](https://openai.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Rain-Shi/Free_translate.svg)](https://github.com/Rain-Shi/Free_translate/stargazers)

## 📖 Project Origin

This story begins with a professor's translation task...

When I needed to translate a large number of academic documents, I tried various services and found:
- **Baidu Translate**: Requires payment 💰
- **DeepL**: Requires payment 💰  
- **Youdao Translate**: Requires payment 💰

**I was so frustrated that I didn't want to pay!** 😤

So I decided to build my own document translation tool. I referenced excellent cases on GitHub:
- [document-translation](https://github.com/kukas/document-translation) 
- [DocuTranslate](https://github.com/xunbu/docutranslate)
- [TransDoc](https://github.com/abner-wong/transdoc)

But I was too lazy to copy, so I wanted to create something unique 🤔

## 🚀 Core Features

### 1. Intelligent Document Translation
- **OpenAI GPT-3.5-turbo**: Uses advanced AI models for high-quality translation (Implemented)
- **Multi-language Support**: Supports translation to multiple target languages (Implemented)
- **Context Understanding**: Maintains translation coherence and accuracy (Implemented)

### 2. Format Fidelity System
- **Structural Layer Extraction**: Deconstructs Word documents into content, format, and layout layers (Implemented)
- **Smart Format Reconstruction**: Reconstructs documents after translation while preserving original format (Implemented)
- **Font Size and Color Preservation**: Maintains original document's font size and color (Implemented)

### 3. Proper Noun Protection
- **Built-in Protection**: Automatically protects technical terms like GitHub, OpenAI, Python (Implemented)
- **Custom Protection**: Supports user-added custom proper nouns (Implemented)
- **Intelligent Recognition**: Prevents incorrect translation of proper nouns (Implemented)

### 4. Performance Optimization
- **Caching Mechanism**: Caches translation results to avoid repetitive translation (Implemented)
- **Batch Processing**: Optimizes batch translation for short texts (Implemented)
- **Duplicate Content Detection**: Automatically detects and avoids repetitive translation (Implemented)

### 5. Result Display
- **Dual Tab Display**: Separately displays original and translated text (Implemented)
- **Translation Statistics**: Shows word count, length ratio, etc. (Implemented)
- **Basic Quality Assessment**: Provides basic quality assessment based on length ratio (Implemented)
- **Document Download**: Supports downloading translated Word documents (Implemented)
- **Format Preservation**: Maintains original document's font size and color (Implemented)

## 🎯 Core Advantages

### Compared to Traditional Translation Tools

| Feature | Traditional Methods | Our System | Advantage |
|---------|-------------------|------------|-----------|
| Format Preservation | Easy to lose | Smart preservation | Structural layer extraction |
| Proper Nouns | No control | Smart protection | Proper noun protection |
| Translation Quality | Basic translation | AI-enhanced | OpenAI GPT |
| User Experience | One-way processing | Result display | Dual tab display |
| Cost | Pay-per-use | Completely free | Open source free |

### Compared to Existing Open Source Solutions

- **document-translation**: Focuses on batch processing, preserves markup, but lacks AI context optimization
- **DocuTranslate**: Good format preservation, but run-level writing back can cause uneven text distribution after translation
- **TransDoc**: XML extraction approach preserves format, but high development complexity and limited translation context

**Our Solution**: Combines the advantages of each approach, using structural layer extraction + AI semantic translation + smart format reconstruction, maintaining format while improving quality.

## 🚀 Quick Start

### Requirements

- Python 3.8+
- OpenAI API key (or other LLM)
- 8GB+ RAM (recommended)

### Installation Steps

1. **Clone the project**
```bash
git clone https://github.com/Rain-Shi/Free_translate.git
cd Free_translate
```

2. **Create virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Start the application**
```bash
# Windows
start_app.bat
# Linux/Mac
./start_app.sh
# Or run directly
streamlit run smart_app.py
```

5. **Access the application**
Open your browser and visit: http://localhost:8501

## 📖 Usage Guide

### Basic Usage

1. **Set API Key**: Enter OpenAI API key in the sidebar
2. **Select Target Language**: Choose the target language for translation
3. **Upload Word Document**: Select a .docx format Word document
4. **Start Translation**: Click "🚀 Start Intelligent Translation"
5. **View Results**: Use dual tabs to view original and translated text

### Advanced Features

#### Proper Noun Protection
- **Enable Proper Noun Protection**: Check "Enable Proper Noun Protection" in the sidebar
- **Custom Proper Nouns**: Enter custom proper nouns in the text box, one per line
- **Built-in Protection**: Automatically protects technical terms like GitHub, OpenAI, Python

#### Performance Optimization
- **Enable Performance Optimization**: Check "Enable Performance Optimization" in the sidebar
- **Caching Mechanism**: Automatically caches translation results to avoid repetitive translation
- **Batch Processing**: Optimizes batch translation for short texts

## 🔧 Technical Architecture

### Core Technology Stack

- **Frontend Framework**: Streamlit
- **Document Processing**: python-docx, pypandoc
- **AI Translation**: OpenAI GPT-3.5-turbo
- **Format Conversion**: Pandoc
- **Data Processing**: Python 3.8+

### System Components

```
smart_translator.py          # Core translation engine
├── StructuralParser         # Structural layer parser
├── SemanticTranslator       # Semantic-enhanced translator
├── SmartReconstructor       # Smart format reconstructor
└── DualViewEditor           # Dual view editor

smart_app.py                 # Main application interface
├── User interface components
├── Advanced feature configuration
├── Duplicate content detection
└── Quality assessment display

simple_display_interface.py # Simple display interface
├── Dual tab display
├── Translation statistics
└── Quality assessment
```

## 🎯 Application Scenarios

### 1. Academic Paper Translation
- **Proper Noun Protection**: Ensures technical terms are not incorrectly translated
- **Format Preservation**: Perfectly maintains paper formatting
- **AI Translation**: Uses OpenAI GPT for high-quality translation

### 2. Business Document Translation
- **Contract Translation**: Precisely maintains legal document formatting
- **Report Translation**: Preserves business report structure
- **Proposal Translation**: Maintains professional business style

### 3. Technical Document Translation
- **API Documentation**: Maintains code formatting and structure
- **User Manuals**: Preserves operation guide formatting
- **Technical Specifications**: Ensures consistency of technical terms

## ⚠️ Important Notice

**This project was developed solely to fulfill a professor's one-time translation task. The task ended when satisfactory results were achieved. Due to limited data testing, please use with caution!**

- 🎯 **Development Purpose**: Solve professor's translation task, avoid paid translation tools
- ⚠️ **Testing Status**: Limited testing, potential unknown issues
- 🔧 **Usage Recommendation**: Test with small documents first, then process important documents after confirming effectiveness
- 📝 **Disclaimer**: Developer assumes no responsibility for any issues arising from using this tool

## 🔍 Troubleshooting

### Common Issues

1. **Q: What if formatting is lost after translation?**
   A: The system automatically performs intelligent format reconstruction to maintain original formatting.

2. **Q: Inconsistent translation of technical terms?**
   A: Use proper noun protection feature, add custom proper nouns in the sidebar.

3. **Q: Slow translation speed?**
   A: Enable performance optimization feature, the system will automatically cache and batch process.

4. **Q: Duplicate table content display?**
   A: The system has optimized table processing, automatically deduplicating to avoid repetition.

### Troubleshooting Steps

- **API Key Error**: Check if OpenAI API key is correct
- **Document Format Issue**: Ensure using .docx format
- **Insufficient Memory**: For large documents, consider processing in segments
- **Network Issues**: Check network connection and API access

## 🤝 Contributing

We welcome community contributions! Please follow these steps:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to [document-translation](https://github.com/kukas/document-translation) for inspiration
- Thanks to [DocuTranslate](https://github.com/xunbu/docutranslate) for reference
- Thanks to [TransDoc](https://github.com/abner-wong/transdoc) for ideas
- Thanks to OpenAI for providing powerful AI translation capabilities
- Thanks to Streamlit for providing an excellent web framework
- Thanks to all contributors and users for their support

## 📞 Contact Us

- **Project Homepage**: https://github.com/Rain-Shi/Free_translate
- **Issue Reports**: https://github.com/Rain-Shi/Free_translate/issues

---

**🎉 Thank you for using! Let's advance document translation technology together!**

## ⭐ If this project helps you, please give us a Star!

**After all, we don't want to give money to those paid translation tools either!** 😄