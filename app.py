from flask import Flask, render_template, request
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import os
import cred

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
# for WTF the following keys have different names.
app.config['RECAPTCHA_PUBLIC_KEY'] = cred.recaptcha_site_key
app.config['RECAPTCHA_PRIVATE_KEY'] = cred.recaptcha_secret_key
app.config['TESTING'] = False

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Login')
    recaptcha = RecaptchaField()

@app.route('/', methods=['GET','POST'])
def home():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            return render_template('success.html', form=form)

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)