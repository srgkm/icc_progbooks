# -*- coding: utf-8 -*-

# Python 2/3 comp
from __future__ import absolute_import, division, print_function, unicode_literals

import urlparse
import uuid

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.utils import dateparse, html

from z_store.models import Author, Publisher, Category, Book


def get_qs_arg_from_url(url, arg):
    parsed_url = urlparse.urlparse(url)
    if parsed_url.query:
        parsed_qs = urlparse.parse_qs(parsed_url.query)
        if len(parsed_qs.get(arg, [])):
            return parsed_qs[arg][0]


def get_filename_and_file_obj_from_url(url):
    r = requests.get(url)
    if not r.ok:
        return
    return '%s.%s' % (uuid.uuid4(), r.headers['Content-Type'].split('/')[-1]), ContentFile(r.content)


class Command(BaseCommand):

    book_urls = []
    api_endpoint = 'https://www.googleapis.com/books/v1/volumes/'

    def handle(self, *args, **options):
        book_ids = []
        if self.book_urls:
            for book_url in self.book_urls:
                book_ids.append(get_qs_arg_from_url(book_url, 'id'))
        else:
            for q in ('python', 'django', 'javascript', 'html'):
                r = requests.get(self.api_endpoint, {'q': q})
                if not r.ok:
                    self.stdout.write(self.style.ERROR('ERROR: %s' % r.url))
                for i in r.json().get('items', []):
                    book_ids.append(i['id'])
        for book_id in book_ids:
            r = requests.get(self.api_endpoint + str(book_id))
            if not r.ok:
                self.stdout.write(self.style.ERROR('ERROR: %s' % r.url))
            book_data = r.json()['volumeInfo']
            self.stdout.write(self.style.SUCCESS(book_id))
            keys_to_check = (
                'title',
                'description',
                'language',
                'publishedDate',
                'pageCount',
                'industryIdentifiers',
                'publisher',
                'imageLinks',
                'authors',
                'categories'
            )
            # mazafaka
            skip = False
            for k in keys_to_check:
                if not book_data.get(k):
                    skip = True
            if skip:
                continue
            book_obj = Book(
                title=book_data['title'],
                price=0,
                description=html.strip_tags(book_data['description']),
                language=book_data['language'],
                num_of_pages=book_data['pageCount'],
                isbn=int(book_data['industryIdentifiers'][-1]['identifier'])
            )
            if dateparse.parse_date(book_data['publishedDate']):
                book_obj.published_date = dateparse.parse_date(book_data['publishedDate'])
            else:
                book_obj.published_date = dateparse.parse_date('%s-01-01' % book_data['publishedDate'])
            publisher_obj, created = Publisher.objects.get_or_create(name=book_data['publisher'])
            book_obj.publisher = publisher_obj
            filename, file_obj = get_filename_and_file_obj_from_url(book_data['imageLinks']['thumbnail'])
            book_obj.cover_image.save(filename, file_obj, save=False)
            book_obj.save()
            for author in book_data['authors']:
                author_obj, created = Author.objects.get_or_create(name=author)
                book_obj.authors.add(author_obj)
            for category in book_data['categories']:
                category_obj, created = Category.objects.get_or_create(name=category)
                book_obj.categories.add(category_obj)
        self.stdout.write(self.style.SUCCESS('OK'))
