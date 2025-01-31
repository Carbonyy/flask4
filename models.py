from flask import  Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(250), nullable=False)

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    profession = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    stack_of_technologies = db.Column(db.String(200), nullable=False)
    soft_skills = db.Column(db.String(200), nullable=False)
    hard_skills = db.Column(db.String(200), nullable=False)
    description_about_me = db.Column(db.String(200), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()