from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to DevOps Lab 1!",
        "student": "Upadhyayula Nijaagna",
        "project": "DevOps Foundations & Continuous Integration",
        "status": "Running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
