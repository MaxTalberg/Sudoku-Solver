from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def upload_text_file():
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]

        if file and file.filename != "":
            filename = "input.txt"
            file.save(os.path.join("/src", filename))
            return redirect(url_for("uploaded_file", filename=filename))

        # solve sudoku
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    """


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    # Run your sudoku solver script here and return the output
    return "File uploaded successfully"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
