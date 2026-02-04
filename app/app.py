from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>Dynamic Web Application</h1>
    <p>Server Hostname: {socket.gethostname()}</p>
    <p>Status: Running successfully 🚀</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

