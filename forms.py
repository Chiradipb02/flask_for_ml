from flask_wtf import FlaskForm
import pandas as pd
from wtforms import (
    FloatField,
    SubmitField
)
from wtforms.validators import InputRequired



class InputForms(FlaskForm):
    sepal_length = FloatField('Sepal Length (cm)', validators=[InputRequired()])
    sepal_width = FloatField('Sepal Width (cm)', validators=[InputRequired()])
    petal_length = FloatField('Petal Length (cm)', validators=[InputRequired()])
    petal_width = FloatField('Petal Width (cm)', validators=[InputRequired()])
    submit = SubmitField('Predict')

