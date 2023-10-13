import pickle
import pandas as pd
from flask import Flask, render_template, request, url_for

app = Flask(__name__)


def load_object(file_path):
    with open(file_path, "rb") as file_obj:
        return pickle.load(file_obj)


def predict(df):
    model = load_object("./artifacts/logisticRegression.pkl")
    return model.predict(df)


@app.route("/")
@app.route("/home")
def homePage():
    return render_template("home.html")


@app.route("/prediction", methods=["POST", "GET"])
def predictionPage():
    prediction = None
    if request.method == "GET":
        return render_template("predict.html")
    else:
        df = pd.DataFrame(
            {
                "sepal_length": float(request.form.get("sepal_length")),
                "sepal_width": float(request.form.get("sepal_width")),
                "petal_length": float(request.form.get("petal_length")),
                "petal_width": float(request.form.get("petal_width")),
            },
            index=[0],
        )
        prediction = predict(df)
        return render_template("predict.html", prediction=prediction)