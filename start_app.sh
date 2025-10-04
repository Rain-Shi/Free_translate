#!/bin/bash
echo "启动Word文档翻译工具..."
cd "$(dirname "$0")"
source venv/bin/activate
streamlit run app.py
