from flask import Flask, render_template, request
from pickle import load

app = Flask(__name__)

# Load the model
model = load(open("diab.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        try:
            # Collect form data
            age = float(request.form["age"])
            bmi = float(request.form["bmi"])
            fs = float(request.form["fs"])
            hb = float(request.form["hb"])
            ge = int(request.form["gender"])
            hy = int(request.form["hypertension"])
            fh = int(request.form["family"])

            # Prepare input for prediction
            d1 = [age, bmi, fs, hb]
            d2 = [1, 0] if ge == 1 else [0, 1]
            d3 = [1, 0] if hy == 1 else [0, 1]
            d4 = [1, 0] if fh == 1 else [0, 1]

            d = [d1 + d2 + d3 + d4]
            pred = model.predict(d)[0]
            result = "Diabetic" if pred == 1 else "Not Diabetic"
        except:
            result = "Invalid input. Please check values."
    return render_template("home.html", result=result)

if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
