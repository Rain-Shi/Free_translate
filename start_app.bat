@echo off
echo 启动Word文档翻译工具...
cd /d "%~dp0"
call venv\Scripts\activate.bat
streamlit run app.py
pause
