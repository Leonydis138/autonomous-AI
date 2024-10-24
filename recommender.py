import pandas as pd
from sklearn.neighbors import NearestNeighbors

class RecommendationEngine:
    def __init__(self):
        self.model = NearestNeighbors()

    def fit(self, data):
        self.model.fit(data)

    def recommend(self, user_input):
        distances, indices = self.model.kneighbors(user_input, n_neighbors=3)
        return indices  # Return indices of recommended items

# Example usage:
data = pd.DataFrame({
    'feature1': [1, 2, 3],
    'feature2': [2, 3, 4]
})
recommendation_engine = RecommendationEngine()
recommendation_engine.fit(data)
recommended_indices = recommendation_engine.recommend([[2, 3]])
print(recommended_indices)
