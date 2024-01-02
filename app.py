import png
import pyqrcode
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_qr_code", methods=["POST"])
def generate_qr_code():
    url = request.form["url"]
    filename = request.form["filename"]

    qr = pyqrcode.create(url)
    qr.png(f"static/{filename}.png", scale=8)

    return send_file(f"static/{filename}.png", mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)
