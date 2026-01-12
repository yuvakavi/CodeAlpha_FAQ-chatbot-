# 🚀 FAQ Chatbot - Run Checklist

Use this checklist to ensure everything is set up correctly before running your chatbot.

## ☑️ Pre-Flight Checklist

### 1. Environment Setup
- [ ] Python 3.7+ is installed
  ```bash
  python --version
  ```
- [ ] Virtual environment is created
  ```bash
  # Check if venv folder exists
  dir venv  # Windows
  ls venv   # Linux/Mac
  ```

### 2. Dependencies Installation
- [ ] Virtual environment is activated
  ```bash
  # You should see (venv) in your terminal prompt
  # Windows: venv\Scripts\activate
  # Linux/Mac: source venv/bin/activate
  ```
- [ ] All packages are installed
  ```bash
  pip list
  # Should show: nltk, scikit-learn, pandas, numpy, streamlit
  ```
- [ ] NLTK data is downloaded
  ```bash
  python -c "import nltk; print(nltk.data.find('tokenizers/punkt'))"
  ```

### 3. Project Files
- [ ] All core files exist:
  - [ ] app.py
  - [ ] chatbot/chatbot.py
  - [ ] models/similarity_model.py
  - [ ] preprocessing/text_cleaner.py
  - [ ] data/faqs.csv
  - [ ] requirements.txt

### 4. Data Validation
- [ ] faqs.csv has correct format (question, answer columns)
- [ ] faqs.csv has at least 5 FAQs
- [ ] No empty rows in faqs.csv

### 5. Component Testing
- [ ] Run the test script
  ```bash
  python test_chatbot.py
  ```
- [ ] All tests pass (6/6)

### 6. Ready to Launch! 🎉
- [ ] Run the chatbot
  ```bash
  streamlit run app.py
  ```
- [ ] Browser opens to http://localhost:8501
- [ ] UI loads without errors
- [ ] Can type questions and get responses

---

## 🔧 Quick Fix Commands

### If setup.bat/setup.sh didn't work:

```bash
# Manual setup
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

pip install --upgrade pip
pip install -r requirements.txt

python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')"
```

### If modules are missing:

```bash
pip install nltk scikit-learn pandas numpy streamlit
```

### If NLTK data is missing:

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')"
```

### If port 8501 is in use:

```bash
streamlit run app.py --server.port 8502
```

---

## 📋 Troubleshooting Checklist

### Problem: "Command 'python' not found"
- [ ] Try `python3` instead of `python`
- [ ] Check Python is in your system PATH
- [ ] Reinstall Python with "Add to PATH" option

### Problem: "Cannot activate virtual environment"
**Windows:**
- [ ] Run PowerShell as Administrator
- [ ] Run: `Set-ExecutionPolicy RemoteSigned`
- [ ] Try again: `venv\Scripts\activate`

**Linux/Mac:**
- [ ] Make sure script is executable: `chmod +x venv/bin/activate`
- [ ] Source it: `source venv/bin/activate`

### Problem: "ModuleNotFoundError"
- [ ] Check virtual environment is activated (you should see `(venv)`)
- [ ] Run: `pip install -r requirements.txt`
- [ ] Check pip is installing in venv: `which pip` or `where pip`

### Problem: "NLTK data not found"
- [ ] Run: `python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')"`
- [ ] Check download location: `python -c "import nltk; print(nltk.data.path)"`

### Problem: "Streamlit won't start"
- [ ] Check if another app is using port 8501
- [ ] Try different port: `streamlit run app.py --server.port 8502`
- [ ] Check firewall settings

### Problem: "No FAQs returned" or "Low confidence"
- [ ] Add more FAQs to data/faqs.csv
- [ ] Lower confidence threshold in chatbot/chatbot.py
- [ ] Make sure FAQs cover diverse topics

---

## ✅ First-Time Run

If this is your first time running the project:

1. **Run Setup Script**
   ```bash
   # Windows
   setup.bat
   
   # Linux/Mac
   chmod +x setup.sh
   ./setup.sh
   ```

2. **Test Components**
   ```bash
   python test_chatbot.py
   ```

3. **Launch Chatbot**
   ```bash
   streamlit run app.py
   ```

4. **Try Example Questions**
   - Click the example question buttons
   - Or type: "What is this chatbot?"

---

## 🎯 Success Indicators

You'll know everything is working when:
- ✅ No errors in terminal
- ✅ Browser opens automatically
- ✅ Chatbot UI is displayed
- ✅ You can type questions and get answers
- ✅ Confidence scores are shown
- ✅ Chat history updates

---

## 📞 Still Having Issues?

1. Run the test script to identify the problem:
   ```bash
   python test_chatbot.py
   ```

2. Check the terminal for error messages

3. Review the README.md troubleshooting section

4. Ensure you're in the correct directory:
   ```bash
   pwd  # Linux/Mac
   cd   # Windows
   # Should show: .../faq-chatbot
   ```

---

## 🎉 Ready to Go!

Once all items are checked:
- ✅ Your FAQ chatbot is ready to use!
- ✅ Start adding your own FAQs to data/faqs.csv
- ✅ Customize the UI in app.py
- ✅ Share with others!

**Happy chatting! 🤖**
