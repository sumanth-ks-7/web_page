from __init__ import app
from flask import render_template


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


if __name__ == "__main__":
    app.run(debug=True)


