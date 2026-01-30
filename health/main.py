import os
from datetime import datetime
import time
from flask import Flask, jsonify

app = Flask(__name__)

SERVICE = os.getenv("SERVICE_NAME", "reliability-lab-py")
VERSION = os.getenv("VERSION", "1.0.0")
PORT = int(os.getenv("PORT", "8080"))

@app.get("/health")
def health():
    # Simula latência se SLEEP_MS estiver definido
    sleep_ms = int(os.getenv("SLEEP_MS", "0"))
    if sleep_ms > 0:
        time.sleep(sleep_ms / 1000)

    health_fail = os.getenv("HEALTH_FAIL", "false").lower()
    if health_fail == "true":
        return jsonify({
            "status": "DOWN",
            "service": SERVICE,
            "version": VERSION,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }), 500

    return jsonify({
        "status": "UP",
        "service": SERVICE,
        "version": VERSION,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
