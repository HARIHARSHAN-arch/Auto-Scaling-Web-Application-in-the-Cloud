from flask import Flask, request, jsonify
import socket
import datetime

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return f"""
    <h1>Welcome to Auto-Scaling Demo App</h1>
    <p>This app is running on: {socket.gethostname()}</p>
    <p>Server Time: {datetime.datetime.now()}</p>
    <p>Use /hello, /add, or /feedback routes to test functionality.</p>
    """

# Simple Hello Route
@app.route("/hello")
def hello():
    return "Hello! This is a Cloud Auto-Scaling Demo."

# Simple Calculator Route
@app.route("/add")
def add():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return jsonify({
            "a": a,
            "b": b,
            "sum": a + b
        })
    except Exception as e:
        return jsonify({"error": str(e)})

# Feedback Route
@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.json
    name = data.get("name", "Anonymous")
    message = data.get("message", "")
    return jsonify({
        "status": "success",
        "name": name,
        "message": message,
        "timestamp": str(datetime.datetime.now())
    })

if __name__ == "__main__":
    # Run on port 80 for AWS Load Balancer compatibility
    app.run(host="0.0.0.0", port=80)