import numpy as np
from sklearn.linear_model import LinearRegression

class SelfLearningModel:
    def __init__(self):
        self.model = LinearRegression()
        self.X = []
        self.y = []

    def add_data(self, features, target):
        self.X.append(features)
        self.y.append(target)
        self.model.fit(np.array(self.X), np.array(self.y))  # Retrain model with new data

    def predict(self, features):
        return self.model.predict([features])

# Example usage:
self_learning = SelfLearningModel()
self_learning.add_data([1, 2], 3)
self_learning.add_data([2, 3], 5)
prediction = self_learning.predict([3, 4])
print(prediction)
