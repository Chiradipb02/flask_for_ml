from flask import Flask,redirect,render_template
from forms import InputForms

app=Flask(__name__)
app.config["SECRET_KEY"]="this_is_the_secret_key"
@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html",title="Home")

@app.route("/predict")
def predict():
    form=InputForms()
    return render_template("predict.html",title="Prediction",form=form)

if __name__=="__main__":
    app.run(debug=True)