import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required resources with error handling
try:
    nltk.download("punkt", quiet=True)
    nltk.download("punkt_tab", quiet=True)
    nltk.download("stopwords", quiet=True)
except Exception as e:
    print(f"Warning: Error downloading NLTK data: {e}")

try:
    stop_words = set(stopwords.words("english"))
except LookupError:
    print("Warning: Using default stopwords")
    stop_words = set()

def clean_text(text):
    """
    Clean and preprocess text for NLP analysis.
    
    Args:
        text (str): Raw text to clean
        
    Returns:
        str: Cleaned and tokenized text
    """
    if not text or not isinstance(text, str):
        return ""
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters and digits, keep only letters and spaces
    text = re.sub(r"[^a-zA-Z ]", "", text)
    
    # Tokenize
    try:
        tokens = word_tokenize(text)
    except LookupError:
        # Fallback to simple split if punkt is not available
        tokens = text.split()
    
    # Remove stopwords
    tokens = [word for word in tokens if word and word not in stop_words]
    
    return " ".join(tokens)
