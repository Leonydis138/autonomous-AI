from sklearn.ensemble import RandomForestRegressor
import numpy as np

class PredictiveModel:
    def __init__(self):
        self.model = RandomForestRegressor()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

# Example usage:
X_train = np.array([[1, 2], [2, 3], [3, 4]])
y_train = np.array([3, 5, 7])
model = PredictiveModel()
model.train(X_train, y_train)
prediction = model.predict(np.array([[4, 5]]))
print(prediction)
