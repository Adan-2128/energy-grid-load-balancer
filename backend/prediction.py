import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Synthetic training data (replace with real data)
# Features: [hour, day_of_week, temp, humidity]
# Target: energy_usage (kWh)
X_train = np.random.rand(1000, 4) * [24, 7, 40, 100]  # Random features
y_train = 10 + (X_train[:, 0] / 24)*5 + (X_train[:, 2]/40)*10 + (X_train[:, 3]/100)*3 + np.random.randn(1000)*2  # Simulated formula

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

def predict_energy_usage(features):
    """
    Predict energy usage for given features: [hour, day_of_week, temp, humidity]
    """
    return model.predict([features])[0]