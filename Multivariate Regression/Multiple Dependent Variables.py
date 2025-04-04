import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Example data
X = np.array([[1, 2], [2, 1], [3, 4], [4, 3], [5, 5]])  # Independent vars
Y = np.array([[5, 2], [6, 1], [7, 4], [8, 3], [10, 5]])  # Two dependent vars

# Fit multivariate regression
model = LinearRegression().fit(X, Y)

# Coefficients
print("Coefficients:\n", model.coef_)
print("Intercepts:\n", model.intercept_)

# Predict
predictions = model.predict(X)
print("Predictions:\n", predictions)
