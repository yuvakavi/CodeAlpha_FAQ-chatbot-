# Quick Start Guide - FAQ Chatbot

## ⚡ Quick Setup (5 minutes)

### Step 1: Setup Environment

**On Windows:**
```cmd
setup.bat
```

**On Linux/Mac:**
```bash
chmod +x setup.sh
./setup.sh
```

### Step 2: Run the Chatbot

```bash
# Activate virtual environment first
# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate

# Run the app
streamlit run app.py
```

### Step 3: Test the Chatbot

Open your browser to `http://localhost:8501` and try:
- "What is this chatbot?"
- "How does the chatbot work?"
- "Can I add my own FAQs?"

## 📝 Customizing Your Chatbot

### Adding Your Own FAQs

1. Open `data/faqs.csv`
2. Add your questions and answers:

```csv
question,answer
Your question here?,Your answer here.
Another question?,Another answer.
```

3. Save the file
4. Restart the app (it will reload automatically in Streamlit)

### Adjusting Confidence Threshold

In `chatbot/chatbot.py`, change the threshold:

```python
bot = FAQChatbot("data/faqs.csv", confidence_threshold=0.3)
```

- **0.2** = More lenient (returns answers even if not very confident)
- **0.5** = Very strict (only highly confident matches)

## 🧪 Testing Components

Run the test script to verify everything works:

```bash
python test_chatbot.py
```

This will test:
- All library imports
- NLTK data availability
- Text preprocessing
- FAQ data validity
- Similarity matching
- Complete chatbot functionality

## 🎨 UI Customization

The chatbot UI is built with Streamlit. You can customize:

1. **Colors and styling**: Edit the CSS in `app.py`
2. **Page layout**: Modify the Streamlit components
3. **Example questions**: Update the example_questions list
4. **Sidebar content**: Edit the sidebar section

## 🚀 Deployment Options

### Option 1: Streamlit Cloud (Easiest)

1. Push code to GitHub
2. Go to https://share.streamlit.io
3. Connect your repo and deploy (free!)

### Option 2: Local Network

```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

Access from other devices using your computer's IP address.

### Option 3: Docker

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')"
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
```

Build and run:
```bash
docker build -t faq-chatbot .
docker run -p 8501:8501 faq-chatbot
```

## 🔧 Troubleshooting

### Problem: "ModuleNotFoundError"
**Solution:** Activate virtual environment and install dependencies
```bash
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### Problem: "NLTK data not found"
**Solution:** Download NLTK data manually
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')"
```

### Problem: "No FAQs returned" or low confidence
**Solution:** 
- Add more FAQs to `data/faqs.csv`
- Lower the confidence threshold
- Ensure FAQs are diverse and cover different topics

### Problem: Streamlit won't start
**Solution:** Check if port 8501 is available
```bash
# Use a different port
streamlit run app.py --server.port 8502
```

## 📊 Project Structure

```
faq-chatbot/
├── app.py                    # 🎨 Main UI (Streamlit app)
├── test_chatbot.py          # 🧪 Test all components
├── requirements.txt         # 📦 Dependencies
├── setup.bat / setup.sh     # ⚙️ Setup scripts
│
├── chatbot/
│   └── chatbot.py          # 🤖 Main bot logic
│
├── data/
│   └── faqs.csv            # 📋 Your FAQs (edit this!)
│
├── models/
│   └── similarity_model.py # 🔍 Matching algorithm
│
└── preprocessing/
    └── text_cleaner.py     # 🧹 Text cleaning
```

## 💡 Pro Tips

1. **More FAQs = Better Accuracy**: Add 20-50 FAQs for best results
2. **Use Similar Wording**: Add variations of the same question
3. **Test Your FAQs**: Use the test script to verify matching
4. **Monitor Confidence**: Low confidence? Add more similar FAQs
5. **Update Regularly**: Keep your FAQs up-to-date with new questions

## 🎓 Learning Resources

- **NLTK Tutorial**: https://www.nltk.org/book/
- **TF-IDF Explained**: https://en.wikipedia.org/wiki/Tf%E2%80%93idf
- **Streamlit Docs**: https://docs.streamlit.io
- **Cosine Similarity**: https://en.wikipedia.org/wiki/Cosine_similarity

## 📞 Need Help?

Run the test script to diagnose issues:
```bash
python test_chatbot.py
```

Check the full README.md for detailed documentation.

---

**Happy Chatbotting! 🎉**
