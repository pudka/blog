from flask import render_template, url_for, flash, redirect
from blog import app
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post


posts = [
    {
        'author': 'Valeria Voloshko',
        'title': 'Worthy people ',
        'content': 'Dreams',
        'date_post': '24 February 2021'
    },
    {
        'author': 'Valeria Voloshko',
        'title': 'Under your mind',
        'content': 'Dreams',
        'date_post': '24 February 2021'
    }
]


@app.route('/')
@app.route('/home')
def home():
    with open("/home/kiddo/Documents/valeria_notes.txt") as reader:
        rows = reader.readlines()
        posts[0]['content'] = ''.join(rows)

    with open("/home/kiddo/Documents/valeria_note_2.txt") as reader:
        rows = reader.readlines()
        posts[1]['content'] = ''.join(rows)

    post1 = Post.query.all()
    return render_template('home.html', posts=post1)


@app.route('/about')
def about():
    return render_template('about.html')


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