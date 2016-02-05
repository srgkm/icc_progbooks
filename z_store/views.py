# -*- coding: utf-8 -*-

# Python 2/3 comp
from __future__ import absolute_import, division, print_function, unicode_literals

from django.shortcuts import render


# TODO: login
# TODO: logout
# TODO: register


def home(request):
    # new releases
    # bestsellers
    return render(request, 'home.html')


def books_by_author(request, author_id):
    return render(request, 'books.html')


def books_by_publisher(request, publisher_id):
    return render(request, 'books.html')


def books_by_category(request, category_id):
    return render(request, 'books.html')


def book(request, book_id):
    return render(request, 'book.html')


def add_to_order(request):
    pass


def view_order(request):
    pass


# TODO: Add auth!!!
def checkout(request):
    pass
