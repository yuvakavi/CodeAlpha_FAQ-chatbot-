import pandas as pd
from models.similarity_model import SemanticMatcher

class FAQChatbot:
    def __init__(self, faq_path):
        """Initialize chatbot with FAQ data"""
        try:
            self.data = pd.read_csv(faq_path)
            
            # Validate CSV structure
            if 'question' not in self.data.columns or 'answer' not in self.data.columns:
                raise ValueError("CSV must have 'question' and 'answer' columns")
            
            # Remove any NaN values
            self.data = self.data.dropna(subset=['question', 'answer'])
            
            # Initialize the matcher
            self.matcher = SemanticMatcher(self.data["question"].tolist())
            self.fallback_message = "I'm sorry, I couldn't find a relevant answer to your question. Please try rephrasing or ask something else."
            
        except FileNotFoundError:
            raise FileNotFoundError(f"FAQ file not found at: {faq_path}")
        except Exception as e:
            raise Exception(f"Error loading FAQ data: {str(e)}")

    def get_response(self, user_input, threshold=0.3):
        """Get response for user input with confidence threshold"""
        if not user_input or not user_input.strip():
            return "Please ask a question."
        
        try:
            index, score = self.matcher.find_best_match_with_confidence(user_input, threshold)
            
            if index is None or score < threshold:
                return self.fallback_message
            
            return self.data.iloc[index]["answer"]
            
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def get_response_with_confidence(self, user_input, threshold=0.3):
        """Get response along with confidence score"""
        if not user_input or not user_input.strip():
            return "Please ask a question.", 0.0
        
        try:
            index, score = self.matcher.find_best_match_with_confidence(user_input, threshold)
            
            if index is None or score < threshold:
                return self.fallback_message, 0.0
            
            return self.data.iloc[index]["answer"], score
            
        except Exception as e:
            return f"An error occurred: {str(e)}", 0.0

    def get_top_responses(self, user_input, top_n=3, threshold=0.2):
        """Get top N matching responses"""
        if not user_input or not user_input.strip():
            return []
        
        try:
            matches = self.matcher.get_top_matches(user_input, top_n, threshold)
            
            results = []
            for idx, score in matches:
                question = self.data.iloc[idx]["question"]
                answer = self.data.iloc[idx]["answer"]
                results.append({
                    "question": question,
                    "answer": answer,
                    "confidence": score
                })
            
            return results
            
        except Exception as e:
            return []

