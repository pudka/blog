from flask import render_template, url_for, flash, redirect
from blog import app, db, bcrypt
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post
from flask_login import login_user, current_user, logout_user


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
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in',
              'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password',
                  'success')
    else:
        flash('Login unsuccessful. Please check email and password',
              'success')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('home'))
