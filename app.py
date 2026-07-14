from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

import os
import uuid

from predict import predict_species
from chatbot import chatbot

app = Flask(__name__)

# Configuration

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

ALLOWED_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg",
    "webp"
}


# ==========================================
# Helper
# ==========================================

def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


# ==========================================
# Home Page
# ==========================================

@app.route("/")
def home():

    return render_template("index.html")


# ==========================================
# Predict Animal
# ==========================================

@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:

        return jsonify({
            "success": False,
            "message": "No image uploaded."
        }), 400

    file = request.files["image"]

    if file.filename == "":

        return jsonify({
            "success": False,
            "message": "No image selected."
        }), 400

    if not allowed_file(file.filename):

        return jsonify({
            "success": False,
            "message": "Unsupported image format."
        }), 400

    extension = os.path.splitext(
        secure_filename(file.filename)
    )[1]

    filename = f"{uuid.uuid4().hex}{extension}"

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    try:
        species = predict_species(filepath)

    except Exception as e:

        return jsonify({

            "success": False,

            "message": str(e)

        }), 500

    return jsonify({

        "success": True,

        "species": species,

        "image": f"/static/uploads/{filename}"

    })


# ==========================================
# Chatbot
# ==========================================

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    if data is None:

        return jsonify({

            "success": False,

            "message": "Invalid JSON."

        }), 400

    species = data.get("species", "")

    question = data.get("question", "")

    if species == "" or question == "":

        return jsonify({

            "success": False,

            "message": "species and question are required."

        }), 400

    answer = chatbot(species, question)

    return jsonify({

        "success": True,

        "answer": answer

    })

@app.route("/admin/clear_uploads")
def clear_uploads():
    upload_folder = app.config["UPLOAD_FOLDER"]

    deleted = 0

    for filename in os.listdir(upload_folder):
        filepath = os.path.join(upload_folder, filename)

        if os.path.isfile(filepath):
            os.remove(filepath)
            deleted += 1

    return jsonify({
        "message": f"{deleted} files deleted."
    })

# ==========================================
# Run
# ==========================================

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)