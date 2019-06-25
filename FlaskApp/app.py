from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Email, Length, DataRequired
from wtforms import validators
from wtforms.fields.html5 import EmailField, DateTimeField
from wtforms.fields import DateField
from flask_bootstrap import Bootstrap


class MyForm(FlaskForm):
    name = StringField('Имя', validators=[InputRequired(), Length(min=4, max=15)])
    surname = StringField('Фамилия')
    patronymic = StringField('Отчество', validators=[InputRequired(), Length(min=4, max=15)])
    date = DateField('Когда Вам позвонить?', id='datepick', format='yyyy/mm/dd')
    email = EmailField('Email address', [DataRequired(), validators.Email()])
    wtf = StringField('wtf', validators=[DataRequired(), validators.Length(min=3)])
    phone = StringField('Номер телефона', validators=[InputRequired(), Length(min=4, max=15)])


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
Bootstrap(app)





@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    return render_template('index.html', form=form)

@app.route('/succsess', methods=['GET', 'POST'])
def succsess():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        date = request.form.get('date')
        return render_template('succsess.html', name=name, email=email, date=date)

if __name__ == "__main__":
    app.run()



