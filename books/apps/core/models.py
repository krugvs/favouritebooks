from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=128, null=False)
    last_name = models.CharField(max_length=128, null=False)
    gender = models.CharField(max_length=16)

    def __init__(self, first_name, last_name, gender, *args, **kwargs):
        super(Author, self).__init__(*args, **kwargs)
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender


class Genre(models.Model):
    genre_name = models.CharField(max_length=128, null=False)

    def __init__(self, genre, *args, **kwargs):
        super(Genre, self).__init__(*args, **kwargs)
        self.genre_name = genre


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=128, null=False)

    def __init__(self, publisher, *args, **kwargs):
        super(Publisher, self).__init__(*args, **kwargs)
        self.publisher_name = publisher


class Book(models.Model):
    book_name = models.CharField(max_length=512, null=True)
    isbn = models.CharField(max_length=13, null=True)
    pages = models.IntegerField()
    year = models.IntegerField()
    author = models.ForeignKey(Author)
    genre = models.ForeignKey(Genre)
    publisher = models.ForeignKey(Publisher)

    def __init__(self, book, isbn, pages, year, author, genre, publisher, *args, **kwargs):
        super(Book, self).__init__(*args, **kwargs)
        self.book_name = book
        self.isbn = isbn
        self.pages = pages
        self.year = year
        self.author = author
        self.genre = genre
        self.publisher = publisher
