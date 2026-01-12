from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class SemanticMatcher:
    def __init__(self, questions):
        self.questions = questions
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=1000)
        self.question_vectors = self.vectorizer.fit_transform(questions)

    def find_best_match(self, user_question):
        user_vector = self.vectorizer.transform([user_question])
        similarities = cosine_similarity(user_vector, self.question_vectors)
        best_index = np.argmax(similarities)
        best_score = similarities[0][best_index]
        return best_index, best_score

    def find_best_match_with_confidence(self, user_question, threshold=0.3):
        """Find best match and return with confidence score"""
        user_vector = self.vectorizer.transform([user_question])
        similarities = cosine_similarity(user_vector, self.question_vectors)[0]
        best_index = np.argmax(similarities)
        best_score = similarities[best_index]
        
        if best_score < threshold:
            return None, 0.0
        
        return best_index, float(best_score)

    def get_top_matches(self, user_question, top_n=3, threshold=0.2):
        """Get top N matches above threshold"""
        user_vector = self.vectorizer.transform([user_question])
        similarities = cosine_similarity(user_vector, self.question_vectors)[0]
        
        # Get indices sorted by similarity
        top_indices = np.argsort(similarities)[::-1][:top_n]
        
        # Filter by threshold
        results = []
        for idx in top_indices:
            score = similarities[idx]
            if score >= threshold:
                results.append((int(idx), float(score)))
        
        return results
