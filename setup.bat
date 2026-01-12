@echo off
REM Setup script for FAQ Chatbot on Windows

echo Setting up FAQ Chatbot...

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo Installing dependencies...
pip install -r requirements.txt

REM Download NLTK data
echo Downloading NLTK data...
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')"

echo.
echo Setup complete!
echo.
echo To run the chatbot:
echo 1. Activate virtual environment: venv\Scripts\activate
echo 2. Run: streamlit run app.py
echo.
pause
