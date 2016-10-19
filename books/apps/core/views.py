from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from books.apps.core.models import Author, Genre, Publisher


def dashboard(request):
    authors = Author.objects.all()
    genres = Genre.objects.all()
    publishers = Publisher.objects.all()
    data = {
        'authors': authors,
        'publishers': publishers,
        'genres': genres
    }
    return render(request, 'base.html', data)
