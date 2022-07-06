from __init__ import app
from flask import render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app.config['SECRET_KEY'] = 'fd8740f98ddd013ce021f5f2bde3c3d7'  # to get secret key in python console type --> import secrets --> secrets.token_hex(16)

posts = [
    {
        'author': 'Sumanth',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'Jan 1st, 2022'
    },
    {
        'author': 'SSBHAT',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'Jan 2nd, 2022'
    }
]


# @app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)


