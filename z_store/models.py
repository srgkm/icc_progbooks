# -*- coding: utf-8 -*-

# Python 2/3 comp
from __future__ import absolute_import, division, print_function, unicode_literals

from django.contrib.auth.models import User
from django.db import models


# TODO: Choose real books and make fixtures
# TODO: Add verbose_name and help_text to all models


class Author(models.Model):

    name = models.CharField(
        max_length=255,
        db_index=True
    )

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Publisher(models.Model):

    name = models.CharField(
        max_length=255,
        db_index=True
    )

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'

    def __str__(self):
        return self.name


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

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return '%s / %s' % (self.type, self.name)


class Book(models.Model):

    # TODO: Add simple QueryManager
    # TODO: Add simple ISBN validator

    LANGUAGE_CHOICES = [
        ['english', 'Английский'],
        ['russian', 'Русский']
    ]

    title = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='Название'
    )
    cover_image = models.ImageField(
        verbose_name='Обложка'
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        db_index=True,
        verbose_name='Цена'
    )
    discount = models.PositiveIntegerField(
        default=0,
        db_index=True,
        verbose_name='Скидка в %'
    )
    qty_in_stock = models.PositiveIntegerField(
        default=0,
        db_index=True,
        verbose_name='Количество в наличии'
    )
    authors = models.ManyToManyField(
        to=Author,
        related_name='books',
        verbose_name='Авторы'
    )
    publishers = models.ManyToManyField(
        to=Publisher,
        related_name='books',
        verbose_name='Издатели'
    )
    categories = models.ManyToManyField(
        to=Category,
        related_name='books',
        verbose_name='Категории'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    language = models.CharField(
        max_length=32,
        choices=LANGUAGE_CHOICES,
        db_index=True,
        verbose_name='Язык'
    )
    published_date = models.DateField(
        db_index=True,
        verbose_name='Дата выхода'
    )
    num_of_pages = models.IntegerField(
        verbose_name='Количество страниц'
    )
    isbn = models.PositiveIntegerField(
        db_index=True,
        verbose_name='ISBN'
    )
    archive = models.BooleanField(
        default=False,
        db_index=True,
        verbose_name='Архив?'
    )
    created_time = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Время создания'
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title


class Review(models.Model):

    """
    Только залогиненный Клиент может оставить отзыв/обзор.
    """

    RATING_CHOICES = [
        [1, 1],
        [2, 2],
        [3, 3],
        [4, 4],
        [5, 5]
    ]

    book = models.ForeignKey(
        to=Book,
        related_name='reviews',
        verbose_name='Книга'
    )
    user = models.ForeignKey(
        to=User,
        related_name='reviews',
        verbose_name='Клиент'
    )
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        db_index=True,
        verbose_name='Рейтинг книги'
    )
    text = models.TextField(
        verbose_name='Текст обзора'
    )
    created_time = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Время создания'
    )

    class Meta:
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'

    def __str__(self):
        return self.book.title


class Order(models.Model):

    """
    Обрабатываем три кейса:
    1. Новый Клиент без регистрации.
        - Может добавлять Книги в Корзину (user_id = null)
        - На этапе чекаута ему нужно предложить регистрацию и залогинить
    2. Разлогиненные Клиент
        - Может добавлять Книги в Корзину (user_id = null)
        - На этапе чекаута ему нужно предложить залогиниться
    3. Залогиненный Клиент
        - Может добавлять Книги в Корзину (user_id = request.user.id)
    """

    # TODO: Validate phone and address
    # TODO: Explain state
    # TODO: Explain through arg

    STATUS_CHOICES = [
        ['initiated', 'Заказ инициирован Клиентом'],
        ['placed', 'Заказ размещен Клиентом'],
        ['confirmed', 'Заказ подтвержден Магазином'],
        ['delivered', 'Заказ доставлен Магазином'],
        ['canceled_by_customer', 'Заказ отменен Клиентом'],
        ['canceled_by_store', 'Заказ отменен Магазином']
    ]

    user = models.ForeignKey(
        to=User,
        null=True,
        blank=True,
        related_name='orders',
        verbose_name='Клиент'
    )
    books = models.ManyToManyField(
        to=Book,
        through='OrderBook',
        verbose_name='Книги в заказе'
    )
    status = models.CharField(
        max_length=32,
        choices=STATUS_CHOICES,
        default=STATUS_CHOICES[0],
        db_index=True,
        verbose_name='Статус'
    )
    phone = models.CharField(
        max_length=32,
        db_index=True,
        verbose_name='Контактный телефон'
    )
    address = models.TextField(
        verbose_name='Адрес доставки'
    )
    comment_by_customer = models.TextField(
        blank=True,
        verbose_name='Комментарий Клиента'
    )
    comment_by_store = models.TextField(
        blank=True,
        verbose_name='Комментарий Магазина'
    )
    created_time = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Время создания'
    )
    updated_time = models.DateTimeField(
        auto_now=True,
        db_index=True,
        verbose_name='Время обновления'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return '%s: %s' % (self.status, self.id)


class OrderBook(models.Model):

    """
    Здесь мы копируем текущую цену и скидку на книгу, чтобы зафиксировать данные параметры
    в момент, когда Клиент кладет Книгу в корзину. Если не копировать данные параметры,
    то может возникнуть ситуация, когда Клиент положил Книгу с одной ценой и скидкой,
    а на этапе оформления заказа (checkout) он увидит другую цену и скидку, если происходило обновление.
    """

    order = models.ForeignKey(
        to=Order
    )
    book = models.ForeignKey(
        to=Book
    )
    book_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        db_index=True,
        verbose_name='Цена'
    )
    book_discount = models.PositiveIntegerField(
        default=0,
        db_index=True,
        verbose_name='Скидка в %'
    )
    book_qty = models.PositiveIntegerField(
        default=1,
        db_index=True,
        verbose_name='Количество'
    )

    class Meta:
        verbose_name = 'Заказанная книга'
        verbose_name_plural = 'Заказанные книги'
