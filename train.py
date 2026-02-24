import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import os

# 1. Load Data
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
cols = ['MPG','Cylinders','Displacement','Horsepower','Weight','Acceleration','Model Year','Origin']
df = pd.read_csv(url, names=cols, na_values='?', comment='\t', sep=" ", skipinitialspace=True).dropna()

# 2. Split into 3 sets (60% Train, 20% Val, 20% Test)
X = df[['Cylinders', 'Displacement', 'Weight', 'Acceleration']]
y = df['MPG']

X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.25, random_state=42)

# 3. Train & Save
model = LinearRegression().fit(X_train, y_train)
os.makedirs('app', exist_ok=True)
with open('app/model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Phase 1 Complete: model.pkl created in /app folder.")