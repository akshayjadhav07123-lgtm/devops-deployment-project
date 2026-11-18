from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head><title>DevOps Deployment Project</title></head>
      <body>
        <h1>Welcome to My DevOps Project!</h1>
        <h2>Application deployed successfully.</h2>
        <p>Technology: Python + Flask + Docker + Jenkins</p>
        <p>Server: {}</p>
      </body>
    </html>
    """.format(socket.gethostname())

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "devops-deployment-project"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


























































