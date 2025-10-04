from flask import Flask, render_template, request, redirect, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "gizli_anahtar"

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"png", "psd"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        student_id = request.form.get("student_id")
        project = request.form.get("project")
        file = request.files.get("file")

        if not all([name, surname, student_id, project, file]):
            flash("Lütfen tüm alanları doldurun.")
            return redirect("/")

        if not allowed_file(file.filename):
            flash("Sadece .png veya .psd dosyaları kabul edilir.")
            return redirect("/")

        filename = secure_filename(f"{name}_{surname}_{student_id}_{project}.{file.filename.rsplit('.',1)[1]}")
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        flash("Dosya başarıyla yüklendi!")
        return redirect("/")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
