# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Book(models.Model):

    title = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    cover_image = models.ImageField()
    authors = models.ManyToManyField(Author)
    publishers = models.ManyToManyField(Publisher)
    categories = models.ManyToManyField(Category)
    published_date = models.DateField()
    number_of_pages = models.IntegerField()
    isbn = models.IntegerField()
    price = models.DecimalField()
    discount = models.IntegerField(
        default=0,
    )
    qty_in_stock = models.IntegerField(
        default=0,
    )


class Author(models.Model):

    name = models.CharField(
        max_length=255,
    )


class Publisher(models.Model):

    name = models.CharField(
        max_length=255,
    )


class Category(models.Model):

    SUBTYPE_CHOICES = (
        ('level', 'Уровень',),
        ('language', 'Язык',),
    )

    subtype = models.CharField(
        max_length=255,
        choices=SUBTYPE_CHOICES,
    )
    name = models.CharField(
        max_length=255,
    )


class Review(models.Model):

    RATING_CHOICES = (1, 2, 3, 4, 5,)

    book = models.ForeignKey(Book)
    rating = models.IntegerField(
        choices=RATING_CHOICES,
    )
    title = models.CharField(
        max_length=255
    )
    text = models.TextField()
    published_time = models.DateTimeField()