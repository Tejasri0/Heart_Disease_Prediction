from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

with open("Heart_Disease_Prediction.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        features = [float(i) for i in request.form.values()]

        features = np.array(features).reshape(1, -1)

        prediction = model.predict(features)[0]

        probability = model.predict_proba(features)[0][1]

        if prediction == 1:
            result = "Heart Disease Detected"
        else:
            result = "No Heart Disease"

        return render_template(
            "index.html",
            prediction_text=result,
            probability=f"{probability:.2%}"
        )

    except Exception as e:

        return render_template(
            "index.html",
            prediction_text=str(e)
        )


if __name__ == "__main__":
    app.run(debug=True)