@echo off
cd /d "%~dp0"
echo Запуск Streamlit...
echo.
echo После запуска откройте браузер по адресу: http://localhost:8501
echo.
.venv_trade\Scripts\streamlit run app.py --server.headless true
pause

