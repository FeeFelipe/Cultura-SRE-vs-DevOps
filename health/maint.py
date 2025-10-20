import os
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

SERVICE = os.getenv("SERVICE_NAME", "reliability-lab-py")
VERSION = os.getenv("VERSION", "1.0.0")
PORT = int(os.getenv("PORT", "8080"))

@app.get("/health")
def health():
    # Para o lab: simular falha definindo HEALTH_FAIL=true (retorna 500)
    if os.getenv("HEALTH_FAIL", "false").lower() == "true":
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
