from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        year = int(request.form["year"])
        month = int(request.form["month"])
        prediction = model.predict([[year, month]])[0]
        result = f"₹{prediction:.2f}"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
