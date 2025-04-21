from sklearn.linear_model import Lasso
import numpy as np

# Data
X = np.array([[1], [2], [3], [4]])
y = np.array([1, 2, 3, 4])

# Model with Lasso
model = Lasso(alpha=0.1)
model.fit(X, y)

# Predict
print("Prediction for input 5:", model.predict([[5]])[0])
