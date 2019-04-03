from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Email, Length, DataRequired
from wtforms import validators
from wtforms.fields.html5 import EmailField, DateTimeField
from wtforms.fields import DateField
from flask_bootstrap import Bootstrap


class MyForm(FlaskForm):
    name = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    date = DateField('date', id='datepick', format='yyyy/mm/dd')
    email = EmailField('Email address', [DataRequired(), validators.Email()])
    wtf = StringField('wtf', validators=[DataRequired(), validators.Length(min=3)])


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
Bootstrap(app)





@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    return render_template('index.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    return render_template('login.html', form=form)



if __name__ == "__main__":
    app.run()