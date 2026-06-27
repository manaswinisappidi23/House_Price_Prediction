import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv("house_price.csv")

# Features and Target
X = df[["Area", "Bedrooms", "Age"]]
y = df["Price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("house_model.pkl", "wb"))

print("Model trained and saved successfully!")