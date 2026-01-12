#!/bin/bash
# Setup script for FAQ Chatbot

echo "Setting up FAQ Chatbot..."

# Create virtual environment
echo "Creating virtual environment..."
python -m venv venv

# Activate virtual environment (platform-specific)
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows
    source venv/Scripts/activate
else
    # Linux/Mac
    source venv/bin/activate
fi

# Upgrade pip
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Install requirements
echo "Installing dependencies..."
pip install -r requirements.txt

# Download NLTK data
echo "Downloading NLTK data..."
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')"

echo "Setup complete! Run 'streamlit run app.py' to start the chatbot."
