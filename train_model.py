from sklearn.linear_model import LinearRegression
import pickle
import numpy as np

X = np.array([
    [2022, 6], [2022, 7], [2023, 6], [2023, 7], [2024, 6]
])
y = [25.5, 26.0, 27.0, 28.5, 30.0]

model = LinearRegression()
model.fit(X, y)
pickle.dump(model, open("model.pkl", "wb"))
print("✅ Model saved as model.pkl")
