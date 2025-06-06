from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    review = request.form["review_input"]
    vp = request.form["vp"]
    results = [
        {"tag": "価格が高い", "problem": "コストが高い", "solution": "値下げ検討"}
    ]
    return render_template("index.html", results=results, vp=vp)

if __name__ == "__main__":
    app.run(debug=True)
