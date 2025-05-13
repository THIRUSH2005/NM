import time
import random
import json
from sklearn.ensemble import RandomForestClassifier

# Simulated sensor read functions
def read_gas_sensors():
    return random.uniform(10, 300)

def read_temperature():
    return random.uniform(0, 40)

def read_humidity():
    return random.uniform(20, 90)

def read_color_value():
    return random.uniform(0, 255)

def read_ph():
    return random.uniform(4.5, 8.5)

# Load model once for efficiency
def load_model():
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    # Add more diverse training samples for better accuracy
    X_train = [
        [50, 25, 60, 120, 6.8], 
        [300, 35, 80, 200, 8.0],
        [20, 10, 40, 100, 5.0],
        [75, 20, 55, 110, 6.5],
        [250, 38, 85, 210, 7.9]
    ]
    y_train = ["Fresh", "Spoiled", "Slightly Spoiling", "Fresh", "Spoiled"]
    model.fit(X_train, y_train)
    return model

# One-time setup
model = load_model()

# Real-time data simulation loop
def run_real_time_simulation(duration_seconds=10, interval=2):
    start_time = time.time()
    while time.time() - start_time < duration_seconds:
        gas = read_gas_sensors()
        temp = read_temperature()
        humidity = read_humidity()
        color = read_color_value()
        ph = read_ph()

        features = [[gas, temp, humidity, color, ph]]
        freshness = model.predict(features)[0]

        output = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "gas": gas,
            "temperature": temp,
            "humidity": humidity,
            "color": color,
            "ph": ph,
            "freshness": freshness
        }

        print(json.dumps(output, indent=2))
        time.sleep(interval)

# Run the simulation
run_real_time_simulation()




