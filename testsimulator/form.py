from wtforms import Form, TextField, PasswordField, validators, TextAreaField, FileField


class SigninForm(Form):
    name = TextField('Name', [validators.Required(message='Name required')])
    address = TextAreaField('Address', [validators.Required(message='Address required')])
    email = TextField('Email', [validators.Required(message='Email required')])
    phone = TextField('Phone', [validators.Required(message='Phone required')])
    password = PasswordField('Password', [validators.Required(message='Password required')])


class LoginForm(Form):
    username = TextField('User name', [validators.Required(message='Type your email')])
    password = PasswordField('Password', [validators.Required(message='Type your password')])
