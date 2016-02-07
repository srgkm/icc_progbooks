# -*- coding: utf-8 -*-

# Python 2/3 comp
from __future__ import absolute_import, division, print_function, unicode_literals

from django.db import models
from django.contrib.auth.models import User


# TODO: Choose real books and make fixtures
# TODO: Add verbose_name and help_text to all models


class Author(models.Model):

    name = models.CharField(
        max_length=255,
        db_index=True
    )


class Publisher(models.Model):

    name = models.CharField(
        max_length=255,
        db_index=True
    )


class Category(models.Model):

    TYPE_CHOICES = [
        ['experience_level', 'Уровень подготовки'],
        ['programming_language', 'Язык программирования']
    ]

    type = models.CharField(
        max_length=32,
        choices=TYPE_CHOICES,
        db_index=True
    )
    name = models.CharField(
        max_length=255,
        db_index=True
    )


class Book(models.Model):

    # TODO: Add simple QueryManager
    # TODO: Add simple ISBN validator

    LANGUAGE_CHOICES = [
        ['english', 'Английский'],
        ['russian', 'Русский']
    ]

    title = models.CharField(
        max_length=255,
        db_index=True
    )
    cover_image = models.ImageField()
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        db_index=True
    )
    qty_in_stock = models.PositiveIntegerField(
        default=0,
        db_index=True
    )
    authors = models.ManyToManyField(
        to=Author,
        related_name='books'
    )
    publishers = models.ManyToManyField(
        to=Publisher,
        related_name='books'
    )
    categories = models.ManyToManyField(
        to=Category,
        related_name='books'
    )
    description = models.TextField()
    language = models.CharField(
        max_length=32,
        choices=LANGUAGE_CHOICES,
        db_index=True
    )
    num_of_pages = models.IntegerField()
    created_time = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )


class Review(models.Model):

    RATING_CHOICES = [
        [1, 1],
        [2, 2],
        [3, 3],
        [4, 4],
        [5, 5]
    ]

    book = models.ForeignKey(
        to=Book
    )
    user = models.ForeignKey(
        to=User
    )
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        db_index=True
    )
    title = models.CharField(
        max_length=255
    )
    text = models.TextField()
    created_time = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )


class Order(models.Model):

    # TODO: Validate phone and address
    # TODO: Explain through arg

    user = models.ForeignKey(
        to=User,
        null=True,
        blank=True,
        related_name='orders'
    )
    books = models.ManyToManyField(
        to=Book,
        through='OrderBook'
    )
    phone = models.CharField(
        max_length=32,
        db_index=True
    )
    address = models.TextField()
    comment_by_customer = models.TextField(
        blank=True
    )
    comment_by_store = models.TextField(
        blank=True
    )
    created_time = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )


class OrderStatus(models.Model):

    # TODO: Validate status on change. Eg "confirmed" can't go after "shipped" or "delivered"

    STATUS_CHOICES = [
        ['placed', 'Заказ сформирован'],
        ['confirmed', 'Заказ подтвержден'],
        ['shipped', 'Заказ отгружен'],
        ['delivered', 'Заказ доставлен'],
        ['canceled_by_customer', 'Заказ отменен Клиентом'],
        ['canceled_by_store', 'Заказ отменен Магазином']
    ]

    order = models.ForeignKey(
        to=Order,
        related_name='statuses'
    )
    status = models.CharField(
        max_length=32,
        choices=STATUS_CHOICES,
        db_index=True
    )
    comment = models.TextField(
        blank=True
    )
    created_time = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )
    updated_time = models.DateTimeField(
        auto_now=True,
        db_index=True
    )

    class Meta:
        unique_together = ['order', 'status']


class OrderBook(models.Model):

    order = models.ForeignKey(
        to=Order
    )
    book = models.ForeignKey(
        to=Book
    )
    book_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        db_index=True
    )
    book_qty = models.PositiveIntegerField(
        default=1,
        db_index=True
    )
    created_time = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )
    updated_time = models.DateTimeField(
        auto_now=True,
        db_index=True
    )
