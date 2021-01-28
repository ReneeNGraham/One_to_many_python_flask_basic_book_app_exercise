from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
from repositories import book_repository
from repositories import author_repository


books_blueprint = Blueprint("books", __name__)

# SHOW
# GET '/tasks/<id>'
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)

    # NEW
# GET '/tasks/new'
@books_blueprint.route("/books/new", methods=['GET'])
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors = authors)

# # # CREATE
# # POST '/tasks'
@books_blueprint.route("/books",  methods=['POST'])
def create_book():
    title     = request.form['title']
    genre     = request.form['genre']
    publisher  = request.form['publisher']
    author     = author_repository.select(request.form['author_id'])
    book =     Book(title, genre, publisher, author)
    book_repository.save(book) 
    return redirect('/books')

# SHOW
# GET '/tasks/<id>'
@books_blueprint.route("/books/<id>", methods=['GET'])
def show_book(id):
    book = book_repository.select(id)
    return render_template('books/show.html', book = book)

# EDIT
# GET '/books/<id>/edit'
 

# UPDATE
# PUT '/books/<id>'
@books_blueprint.route("/books/<id>", methods=['POST'])
def update_task(id):
    title      = request.form['title']
    genre      = request.form['genre']
    publisher  = request.form['publisher']
    author     = author_repository.select(request.form['author_id'])
    book       = Book (title, genre, publisher, author, id)
    book_repository.update(book)
    return redirect('/books')


# DELETE
# DELETE '/books/<id>'

@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books') 