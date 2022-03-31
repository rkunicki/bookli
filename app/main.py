import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

DATABASE_URL = os.environ['DATABASE_URL']

app = Flask(__name__, template_folder="templates")

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL.replace("postgres", "postgresql")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Create a table in the database
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(240), unique=True, nullable=False)
    author = db.Column(db.String(120), unique=False, nullable=False)
    publishedDate = db.Column(db.DateTime, unique=False, nullable=False)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    pageCount = db.Column(db.Integer, unique=False, nullable=True)
    imageLink = db.Column(db.String(240), unique=False, nullable=True)
    language = db.Column(db.String(20), unique=False, nullable=False)


db.create_all()


# Def to convert publishedDate from str to datetime object
def try_parsing_date(text):
    for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            pass
    raise ValueError('no valid date format found')


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/manage")
def manage():
    return render_template("manage.html")


@app.route("/add-manually")
def add_manually():
    return render_template("add-manually.html")


@app.route("/add-api")
def add_api():
    return render_template("add-api.html")


@app.route("/success", methods=["POST", "GET"])
def add_book():
    title = request.form.get("title")
    author = request.form.get("author")
    published_date = request.form.get("publishedDate")
    isbn = request.form.get("isbn")
    page_count = request.form.get("pageCount")
    image_link = request.form.get("imageLink")
    language = request.form.get("language")

    # if isbn == None:
    #     print("Błąd! ISBN powinien składać się z 10 lub 13 cyfr")
    #     return render_template("error-isbn.html")

    if len(isbn) != 10 and len(isbn) != 13:
        print("Błąd! ISBN powinien składać się z 10 lub 13 cyfr")
        return render_template("error-isbn.html")

    database = db.session.query(Books).all()
    all_books = [row.isbn for row in database]  # List of all books title from database by use comprehensive list
    if title and author and published_date and isbn and language:

        published_date = try_parsing_date(published_date)

        if isbn in all_books:
            print("Błąd! Podana książka jest już w bazie")
            return render_template("error-database.html")

        book = Books(
            title=title,
            author=author,
            publishedDate=published_date,
            isbn=isbn,
            pageCount=page_count,
            imageLink=image_link,
            language=language
        )
        db.session.add(book)
        db.session.commit()
        return render_template("success.html")
    return render_template("error.html")


@app.route("/books")
def books_list():
    title = request.form.get("title")
    author = request.form.get("author")
    published_date = request.form.get("publishedDate")
    language = request.form.get("language")

    if title:
        books = db.session.query(Books).filter(Books.title == title).all()
        return render_template("books.html", books=books)

    books = db.session.query(Books).all()
    return render_template("books.html", books=books)
