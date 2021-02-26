from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
babel = Babel(app)
app.config['SECRET_KEY'] = '78e1ff03db3c3a1b68af11fa9aae6dcebe9a6925d51c032d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from blog import routes
