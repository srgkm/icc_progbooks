# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 19:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='\u0424\u0418\u041e')),
            ],
            options={
                'verbose_name': '\u0410\u0432\u0442\u043e\u0440',
                'verbose_name_plural': '\u0410\u0432\u0442\u043e\u0440\u044b',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('cover_image', models.ImageField(upload_to=b'', verbose_name='\u041e\u0431\u043b\u043e\u0436\u043a\u0430')),
                ('price', models.DecimalField(db_index=True, decimal_places=2, max_digits=8, verbose_name='\u0426\u0435\u043d\u0430')),
                ('discount', models.PositiveIntegerField(db_index=True, default=0, verbose_name='\u0421\u043a\u0438\u0434\u043a\u0430 \u0432 %')),
                ('qty_in_stock', models.PositiveIntegerField(db_index=True, default=0, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432 \u043d\u0430\u043b\u0438\u0447\u0438\u0438')),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('language', models.CharField(choices=[['en', '\u0410\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439'], ['ru', '\u0420\u0443\u0441\u0441\u043a\u0438\u0439']], db_index=True, max_length=2, verbose_name='\u042f\u0437\u044b\u043a')),
                ('published_date', models.DateField(db_index=True, verbose_name='\u0414\u0430\u0442\u0430 \u0432\u044b\u0445\u043e\u0434\u0430')),
                ('num_of_pages', models.IntegerField(verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u0440\u0430\u043d\u0438\u0446')),
                ('isbn', models.PositiveIntegerField(db_index=True, verbose_name='ISBN')),
                ('archive', models.BooleanField(db_index=True, default=False, verbose_name='\u0410\u0440\u0445\u0438\u0432?')),
                ('created_time', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('authors', models.ManyToManyField(related_name='books', to='z_store.Author', verbose_name='\u0410\u0432\u0442\u043e\u0440\u044b')),
            ],
            options={
                'verbose_name': '\u041a\u043d\u0438\u0433\u0430',
                'verbose_name_plural': '\u041a\u043d\u0438\u0433\u0438',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='\u041d\u0430\u0437\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[['initiated', '\u0417\u0430\u043a\u0430\u0437 \u0438\u043d\u0438\u0446\u0438\u0438\u0440\u043e\u0432\u0430\u043d \u041a\u043b\u0438\u0435\u043d\u0442\u043e\u043c'], ['placed', '\u0417\u0430\u043a\u0430\u0437 \u0440\u0430\u0437\u043c\u0435\u0449\u0435\u043d \u041a\u043b\u0438\u0435\u043d\u0442\u043e\u043c'], ['confirmed', '\u0417\u0430\u043a\u0430\u0437 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d \u041c\u0430\u0433\u0430\u0437\u0438\u043d\u043e\u043c'], ['delivered', '\u0417\u0430\u043a\u0430\u0437 \u0434\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d \u041c\u0430\u0433\u0430\u0437\u0438\u043d\u043e\u043c'], ['canceled_by_customer', '\u0417\u0430\u043a\u0430\u0437 \u043e\u0442\u043c\u0435\u043d\u0435\u043d \u041a\u043b\u0438\u0435\u043d\u0442\u043e\u043c'], ['canceled_by_store', '\u0417\u0430\u043a\u0430\u0437 \u043e\u0442\u043c\u0435\u043d\u0435\u043d \u041c\u0430\u0433\u0430\u0437\u0438\u043d\u043e\u043c']], db_index=True, default=['initiated', '\u0417\u0430\u043a\u0430\u0437 \u0438\u043d\u0438\u0446\u0438\u0438\u0440\u043e\u0432\u0430\u043d \u041a\u043b\u0438\u0435\u043d\u0442\u043e\u043c'], max_length=32, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441')),
                ('phone', models.CharField(db_index=True, max_length=32, verbose_name='\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('address', models.TextField(verbose_name='\u0410\u0434\u0440\u0435\u0441 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438')),
                ('comment_by_customer', models.TextField(blank=True, verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u041a\u043b\u0438\u0435\u043d\u0442\u0430')),
                ('comment_by_store', models.TextField(blank=True, verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u041c\u0430\u0433\u0430\u0437\u0438\u043d\u0430')),
                ('created_time', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('updated_time', models.DateTimeField(auto_now=True, db_index=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0417\u0430\u043a\u0430\u0437',
                'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u044b',
            },
        ),
        migrations.CreateModel(
            name='OrderBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_price', models.DecimalField(db_index=True, decimal_places=2, max_digits=8, verbose_name='\u0426\u0435\u043d\u0430')),
                ('book_discount', models.PositiveIntegerField(db_index=True, default=0, verbose_name='\u0421\u043a\u0438\u0434\u043a\u0430 \u0432 %')),
                ('book_qty', models.PositiveIntegerField(db_index=True, default=1, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='z_store.Book')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='z_store.Order')),
            ],
            options={
                'verbose_name': '\u0417\u0430\u043a\u0430\u0437\u0430\u043d\u043d\u0430\u044f \u043a\u043d\u0438\u0433\u0430',
                'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0435 \u043a\u043d\u0438\u0433\u0438',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0418\u0437\u0434\u0430\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u0418\u0437\u0434\u0430\u0442\u0435\u043b\u0438',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], db_index=True, verbose_name='\u0420\u0435\u0439\u0442\u0438\u043d\u0433 \u043a\u043d\u0438\u0433\u0438')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043e\u0431\u0437\u043e\u0440\u0430')),
                ('created_time', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='z_store.Book', verbose_name='\u041a\u043d\u0438\u0433\u0430')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='\u041a\u043b\u0438\u0435\u043d\u0442')),
            ],
            options={
                'verbose_name': '\u041e\u0431\u0437\u043e\u0440',
                'verbose_name_plural': '\u041e\u0431\u0437\u043e\u0440\u044b',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='books',
            field=models.ManyToManyField(through='z_store.OrderBook', to='z_store.Book', verbose_name='\u041a\u043d\u0438\u0433\u0438 \u0432 \u0437\u0430\u043a\u0430\u0437\u0435'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='\u041a\u043b\u0438\u0435\u043d\u0442'),
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(related_name='books', to='z_store.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='z_store.Publisher', verbose_name='\u0418\u0437\u0434\u0430\u0442\u0435\u043b\u044c'),
        ),
    ]
