from flask import Flask, render_template
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", host=socket.gethostname())

@app.route("/health")
def health():
    return {"service": "chess", "host": socket.gethostname(), "status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)   