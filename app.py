from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(240), unique=True, nullable=False)
    author = db.Column(db.String(120), unique=False, nullable=False)
    publishedDate = db.Column(db.DateTime, unique=False, nullable=False)
    isbn = db.Column(db.Integer, unique=True, nullable=False)
    pageCount = db.Column(db.Integer, unique=False, nullable=False)
    previewLink = db.Column(db.String(240), unique=True, nullable=False)
    language = db.Column(db.String(20), unique=False, nullable=False)


db.create_all()

if __name__ == "__main__":
    app.run()
    # app.run(debug=True)
