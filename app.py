from flask import Flask, render_template, request
from pipeline.pipeline import run_pipeline

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    pipeline_result = None

    if request.method == "POST":
        text = request.form["text"]
        pipeline_result = run_pipeline(text)

    return render_template("index.html", result=pipeline_result)

if __name__ == "__main__":
    app.run(debug=True)
