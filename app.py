import png
import pyqrcode
from io import BytesIO
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
    stream = BytesIO()
    qr.png(stream, scale=8)
    stream.seek(0)

    return send_file(stream, mimetype="image/png", as_attachment=True, download_name=f'{filename}.png')

if __name__ == "__main__":
    app.run(debug=True)
