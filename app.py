import pandas as pd
import numpy as np
import joblib

from flask import Flask,redirect,render_template
from forms import InputForms

app=Flask(__name__)
app.config["SECRET_KEY"]="this_is_the_secret_key"

model=joblib.load("best_random_forest_model.joblib")

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html",title="Home")

@app.route("/predict",methods=["GET","POST"])
def predict():
    form=InputForms()
    if form.validate_on_submit():
        x_new=np.array(pd.DataFrame({
            "SepalLengthCm":[form.sepal_length.data],
            "SepalWidthCm":[form.sepal_width.data],
            "PetalLengthCm":[form.petal_length.data],
            "PetalWidthCm":[form.petal_width.data]
        }))

        pred=model.predict(x_new).item()
        classes=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
        for i in range(len(classes)):
            if pred==i:
                pred=classes[i]
                message=f"the predicted class: {pred}"
                break
        
    else:
        message="please provide valid feature values"

    return render_template("predict.html",title="Prediction",form=form,output=message)

if __name__=="__main__":
    app.run(debug=True)