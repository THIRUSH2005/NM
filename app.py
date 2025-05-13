from flask import Flask, jsonify, render_template
import random
import time
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Simulated sensor functions
def read_gas_sensors():
    return round(random.uniform(10, 300), 2)

def read_temperature():
    return round(random.uniform(0, 40), 2)

def read_humidity():
    return round(random.uniform(20, 90), 2)

def read_color_value():
    return round(random.uniform(0, 255), 2)

def read_ph():
    return round(random.uniform(4.5, 8.5), 2)

# Model training
def load_model():
    model = RandomForestClassifier(n_estimators=10, random_state=42)
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

model = load_model()

# Route: Webpage with freshness prediction
@app.route('/')
def index():
    gas = read_gas_sensors()
    temp = read_temperature()
    humidity = read_humidity()
    color = read_color_value()
    ph = read_ph()
    features = [[gas, temp, humidity, color, ph]]
    freshness = model.predict(features)[0]

    data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "gas": gas,
        "temperature": temp,
        "humidity": humidity,
        "color": color,
        "ph": ph,
        "freshness": freshness
    }
    return render_template("index.html", data=data)

# Route: JSON API
@app.route('/api/data')
def api_data():
    gas = read_gas_sensors()
    temp = read_temperature()
    humidity = read_humidity()
    color = read_color_value()
    ph = read_ph()
    features = [[gas, temp, humidity, color, ph]]
    freshness = model.predict(features)[0]

    return jsonify({
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "gas": gas,
        "temperature": temp,
        "humidity": humidity,
        "color": color,
        "ph": ph,
        "freshness": freshness
    })

if __name__ == '__main__':
    app.run(debug=True)
