"""
Test script for FAQ Chatbot
Run this to verify that all components are working correctly.
"""

import sys
import os

def test_imports():
    """Test if all required libraries can be imported"""
    print("Testing imports...")
    try:
        import nltk
        import sklearn
        import pandas
        import numpy
        import streamlit
        print("✓ All required libraries imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_nltk_data():
    """Test if NLTK data is downloaded"""
    print("\nTesting NLTK data...")
    try:
        import nltk
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/stopwords')
        print("✓ NLTK data is available")
        return True
    except LookupError as e:
        print(f"✗ NLTK data not found: {e}")
        print("  Run: python -c \"import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')\"")
        return False

def test_text_cleaner():
    """Test the text cleaning functionality"""
    print("\nTesting text cleaner...")
    try:
        from preprocessing.text_cleaner import clean_text
        
        test_text = "What is NLP? It's amazing!"
        cleaned = clean_text(test_text)
        print(f"  Input: '{test_text}'")
        print(f"  Output: '{cleaned}'")
        
        if cleaned:
            print("✓ Text cleaner working correctly")
            return True
        else:
            print("✗ Text cleaner returned empty string")
            return False
    except Exception as e:
        print(f"✗ Text cleaner error: {e}")
        return False

def test_faq_data():
    """Test if FAQ data file exists and is valid"""
    print("\nTesting FAQ data...")
    try:
        import pandas as pd
        
        faq_file = "data/faqs.csv"
        if not os.path.exists(faq_file):
            print(f"✗ FAQ file not found: {faq_file}")
            return False
        
        df = pd.read_csv(faq_file)
        
        if "question" not in df.columns or "answer" not in df.columns:
            print("✗ FAQ file must have 'question' and 'answer' columns")
            return False
        
        print(f"  Found {len(df)} FAQs")
        print(f"✓ FAQ data is valid")
        return True
    except Exception as e:
        print(f"✗ FAQ data error: {e}")
        return False

def test_similarity_model():
    """Test the similarity model"""
    print("\nTesting similarity model...")
    try:
        from models.similarity_model import FAQSimilarityModel
        import pandas as pd
        
        # Create test questions
        test_questions = pd.Series([
            "what is machine learning",
            "how does ai work",
            "tell me about nlp"
        ])
        
        model = FAQSimilarityModel(test_questions)
        
        # Test matching
        test_query = "what is ai"
        index, confidence = model.find_best_match_with_confidence(test_query)
        
        print(f"  Test query: '{test_query}'")
        print(f"  Best match index: {index}")
        print(f"  Confidence: {confidence:.2%}")
        
        if index is not None:
            print("✓ Similarity model working correctly")
            return True
        else:
            print("✗ Similarity model returned None")
            return False
    except Exception as e:
        print(f"✗ Similarity model error: {e}")
        return False

def test_chatbot():
    """Test the complete chatbot"""
    print("\nTesting chatbot...")
    try:
        from chatbot.chatbot import FAQChatbot
        
        bot = FAQChatbot("data/faqs.csv")
        
        test_questions = [
            "What is this chatbot?",
            "How does it work?",
            "Can I use this for free?"
        ]
        
        for question in test_questions:
            answer, confidence = bot.get_response_with_confidence(question)
            print(f"\n  Q: {question}")
            print(f"  A: {answer}")
            print(f"  Confidence: {confidence:.2%}")
        
        print("\n✓ Chatbot working correctly")
        return True
    except Exception as e:
        print(f"✗ Chatbot error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("FAQ Chatbot - Component Test Suite")
    print("=" * 60)
    
    results = []
    
    # Run tests
    results.append(("Imports", test_imports()))
    results.append(("NLTK Data", test_nltk_data()))
    results.append(("Text Cleaner", test_text_cleaner()))
    results.append(("FAQ Data", test_faq_data()))
    results.append(("Similarity Model", test_similarity_model()))
    results.append(("Chatbot", test_chatbot()))
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "PASS" if result else "FAIL"
        symbol = "✓" if result else "✗"
        print(f"{symbol} {name}: {status}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! The chatbot is ready to use.")
        print("Run: streamlit run app.py")
        return 0
    else:
        print("\n⚠️ Some tests failed. Please fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
