# FAQ Chatbot 🤖

An intelligent FAQ chatbot built using Natural Language Processing (NLP) and Machine Learning to answer user questions by matching them with the most similar FAQ entries.

## 🌟 Features

- **NLP-based Text Preprocessing**: Uses NLTK for tokenization, stopword removal, and text cleaning
- **TF-IDF Vectorization**: Converts text into numerical features for similarity computation
- **Cosine Similarity Matching**: Finds the most relevant FAQ based on semantic similarity
- **Confidence Scoring**: Shows how confident the chatbot is in its answer
- **Interactive UI**: Built with Streamlit for an intuitive chat interface
- **Conversation History**: Tracks questions and answers in the session
- **Easy to Extend**: Simple CSV-based FAQ storage

## 🛠️ Technologies Used

- **Python 3.7+**
- **NLTK**: Natural Language Toolkit for text preprocessing
- **scikit-learn**: Machine learning library for TF-IDF and cosine similarity
- **Pandas**: Data manipulation and CSV handling
- **Streamlit**: Web framework for the chat UI
- **NumPy**: Numerical computing

## 📁 Project Structure

```
faq-chatbot/
│
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── setup.sh                    # Setup script for Linux/Mac
├── setup.bat                   # Setup script for Windows
├── README.md                   # Project documentation
│
├── chatbot/
│   └── chatbot.py             # Main chatbot logic and FAQ matching
│
├── data/
│   └── faqs.csv               # FAQ database (questions and answers)
│
├── models/
│   └── similarity_model.py    # TF-IDF and cosine similarity model
│
└── preprocessing/
    └── text_cleaner.py        # Text preprocessing and cleaning functions
```

## 🚀 How It Works

1. **Data Loading**: FAQs are loaded from a CSV file containing questions and answers
2. **Text Preprocessing**: 
   - Convert to lowercase
   - Remove special characters and numbers
   - Tokenize into words
   - Remove stopwords (common words like "the", "is", etc.)
3. **Vectorization**: Questions are converted to TF-IDF vectors
4. **Similarity Matching**: User input is compared with FAQ vectors using cosine similarity
5. **Response Generation**: The answer from the most similar FAQ is returned

## 📦 Installation

### Windows

1. **Clone or download this repository**

2. **Run the setup script**:
   ```cmd
   setup.bat
   ```

   Or manually:
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')"
   ```

### Linux/Mac

1. **Clone or download this repository**

2. **Make the setup script executable**:
   ```bash
   chmod +x setup.sh
   ```

3. **Run the setup script**:
   ```bash
   ./setup.sh
   ```

   Or manually:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')"
   ```

## 🎮 Usage

### Running the Chatbot

1. **Activate the virtual environment**:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

2. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

3. **Open your browser** to the URL shown (usually `http://localhost:8501`)

4. **Start asking questions!**

### Adding Your Own FAQs

Edit the [data/faqs.csv](data/faqs.csv) file:

```csv
question,answer
What is your product?,Our product is an AI-powered solution that helps businesses automate customer support.
How much does it cost?,We offer flexible pricing starting at $99/month.
```

**Important**: Ensure the CSV has two columns: `question` and `answer`

## 🎯 Example Questions

Try asking:
- "What is this chatbot?"
- "How does the chatbot work?"
- "Can I add my own FAQs?"
- "What is NLP?"
- "How do I deploy this?"
- "What is cosine similarity?"

## ⚙️ Configuration

### Adjusting Confidence Threshold

Edit [chatbot/chatbot.py](chatbot/chatbot.py):

```python
bot = FAQChatbot("data/faqs.csv", confidence_threshold=0.3)  # Range: 0.0 to 1.0
```

- **Lower threshold** (e.g., 0.2): More lenient, returns answers even with low confidence
- **Higher threshold** (e.g., 0.5): More strict, only returns highly confident matches

### Customizing the Fallback Message

Edit [chatbot/chatbot.py](chatbot/chatbot.py):

```python
self.fallback_message = "Your custom message when no good match is found"
```

## 🚢 Deployment

### Streamlit Cloud (Free)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Deploy!

### Heroku

1. Create a `Procfile`:
   ```
   web: streamlit run app.py --server.port=$PORT
   ```

2. Deploy using Heroku CLI:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

## 🧪 Testing

Test the chatbot components:

```python
from chatbot.chatbot import FAQChatbot

# Initialize chatbot
bot = FAQChatbot("data/faqs.csv")

# Get response
answer = bot.get_response("What is this chatbot?")
print(answer)

# Get response with confidence
answer, confidence = bot.get_response_with_confidence("How does it work?")
print(f"Answer: {answer}")
print(f"Confidence: {confidence:.2%}")
```

## 🔧 Troubleshooting

### NLTK Download Errors

If you encounter NLTK download errors, manually download the data:

```python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
```

### Module Not Found Errors

Ensure you're in the virtual environment and all dependencies are installed:

```bash
pip install -r requirements.txt
```

### CSV File Errors

Ensure [data/faqs.csv](data/faqs.csv) has:
- Proper CSV format with headers
- Two columns: `question` and `answer`
- At least one FAQ entry

## 📈 Future Enhancements

- [ ] Add intent classification for better understanding
- [ ] Support for multiple languages
- [ ] Integration with databases (PostgreSQL, MongoDB)
- [ ] Add voice input/output
- [ ] Implement feedback mechanism for continuous learning
- [ ] Add authentication and user management
- [ ] Export conversation history
- [ ] Analytics dashboard

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add more FAQs
- Improve the NLP preprocessing
- Enhance the UI
- Fix bugs
- Add new features

## 📧 Contact

For questions or suggestions, please open an issue in the repository.

---

**Built with ❤️ using Python, NLTK, scikit-learn, and Streamlit**
