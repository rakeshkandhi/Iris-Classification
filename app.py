from flask import Flask,url_for,render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/prediction")
def predictionPage():
    return render_template('predict.html')
@app.route("/about")
def aboutPage():
    return render_template('about.html')
