# -*- coding: utf-8 -*-

# Python 2/3 comp
from __future__ import absolute_import, division, print_function, unicode_literals

from django.contrib import admin

from .models import Book, Review, Author, Publisher, Category, Order, OrderBook


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


class OrderBookInline(admin.StackedInline):

    model = OrderBook
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    inlines = [
        OrderBookInline
    ]
