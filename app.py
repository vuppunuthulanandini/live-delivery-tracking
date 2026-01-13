from flask import Flask, request, jsonify, render_template
import sqlite3
from llm import human_readable_eta  # your function to generate ETA message
from flask_cors import CORS
from eta import estimate_eta  # your ETA calculation function

app = Flask(__name__)
CORS(app)

# Endpoint to receive driver location
@app.route("/update_location", methods=["POST"])
def update_location():
    data = request.json

    # Store in database
    conn = sqlite3.connect("../database/delivery.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO driver_location (driver_id, latitude, longitude) VALUES (?, ?, ?)",
        (data["driver_id"], data["latitude"], data["longitude"])
    )
    conn.commit()
    conn.close()

    # Calculate ETA and generate message
    eta = estimate_eta(data["latitude"], data["longitude"])
    message = human_readable_eta(data["driver_id"], eta)

    # Print to terminal for monitoring
    print("Stored in DB:", data)
    print(f"ETA to destination: {eta:.2f} minutes")
    print(f"Message to user: {message}")

    return {"status": "success", "eta": eta, "message": message}

# Route to serve the map page
@app.route("/")
def map_page():
    return render_template("map.html")

# Route to fetch latest driver location with ETA & message
@app.route("/get_location")
def get_location():
    conn = sqlite3.connect("../database/delivery.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT driver_id, latitude, longitude FROM driver_location ORDER BY rowid DESC LIMIT 1"
    )
    row = cursor.fetchone()
    conn.close()

    if row:
        driver_id, lat, lon = row
        # Add ETA and human-readable message for map popup
        eta = estimate_eta(lat, lon)
        message = human_readable_eta(driver_id, eta)
        return jsonify({
            "driver_id": driver_id,
            "latitude": lat,
            "longitude": lon,
            "eta": eta,
            "message": message
        })
    else:
        return jsonify({
            "driver_id": None,
            "latitude": None,
            "longitude": None,
            "eta": None,
            "message": None
        })

if __name__ == "__main__":
    app.run(debug=True)
