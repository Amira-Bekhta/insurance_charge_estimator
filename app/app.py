from flask import Flask, render_template, request
import joblib

model = joblib.load("model/model.pkl")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    estimation = None  

    if request.method == "POST": 
        age = float(request.form.get("age"))
        sex = request.form.get("sex")
        bmi = float(request.form.get("bmi"))
        children = int(request.form.get("children"))
        smoker = request.form.get("smoker")
        region = request.form.get("choices")

        if sex == "male":
            sex = 0
        else:
            sex = 1

        if smoker == "yes":
            smoker = 1
        else:
            smoker = 0

        if region == "NorthEast":
            region = 0
        elif region == "NorthWest":
            region = 1
        elif region == "SouthEast":
            region = 2
        else:
            region = 3

        pred = model.predict([[age, sex, bmi, children, smoker, region]])
        estimation = pred[0]

    return render_template("index.html", estimation=estimation)

if __name__ == "__main__":
    app.run(debug=True)
