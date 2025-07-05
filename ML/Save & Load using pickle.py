import pickle

# Save model
with open('model_pickle.pkl', 'wb') as f:
    pickle.dump(model, f)

# Load model
with open('model_pickle.pkl', 'rb') as f:
    loaded_model_pickle = pickle.load(f)

# Predict using loaded model
print("Pickle Prediction:", loaded_model_pickle.predict([[3300]]))
