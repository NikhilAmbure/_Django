import os

import django
import itertools
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'firstproject.settings'
django.setup()
import django
import random
from faker import Faker
from home.models import Author, Book
from datetime import datetime, timedelta
from django.db.models import Avg, Sum, Min, Max, Count, Q

# Aggregate functions
# 1
# def handle():
#     book = Book.objects.count()
#     print(book)
# handle()

# 2 -> Avg, Sum, min, max
def handle():
    book = Book.objects.aggregate(Price = Avg('price'))
    book = Book.objects.aggregate(Price = Sum('price'))
    book = Book.objects.aggregate(Price = Min('price'))
    book = Book.objects.aggregate(Price = Max('price'))
    print(book)
handle()

# Annotate
# 3
# def handle():
    # authors = Author.objects.annotate(total_books = Count('book'))
    
    # for author in authors:
        # print(f"Author name  {author.author_name} Total books {author.total_books}")
    # print(author[0].total_books)
# handle()

# 4
# def handle():
    # authors = Author.objects.annotate(avg_price = Avg('book__price'))
    
    # for author in authors:
        # print(f"Author name  {author.author_name} Total avg price {author.avg_price}")
# handle()

# 5
# def handle():
    # authors = Author.objects.annotate(
        # avg_price = Avg('book__price'),
        # total_books = Count('book')
    # )
    
    # for author in authors:
        # print(f"Author name  {author.author_name} Total books {author.total_books} Total avg price {author.avg_price})")
# handle()

# 6
# def handle():
    # authors = Author.objects.annotate(
        # book_count = Count('book', filter=Q(book__published_date__year__gte = 2023))  
    # )
    
    # for author in authors:
        # print(f"Author name  {author.author_name} Book Count {author.book_count}")
# handle()

# 7
# def handle():
    # authors = Author.objects.annotate(
        # expensive_book = Max('book__price')
    # )

    # for author in authors:
        # print(f"Author name {author.author_name} expensive book is {author.expensive_book}")
# handle()


# 8
# def handle():
    # authors = Author.objects.annotate(
        # book_count = Count('book', filter=Q(book__price__gte = 50))
    # ).filter(book_count__gte = 1)
    
    # for author in authors:
        # print(f"Author name  {author.author_name} Total books {author.book_count}")
# handle()


# 9
# def handle():
    # authors = Author.objects.annotate(
        # total_earnings = Sum('book__price')
    # )

    # for author in authors:
        # print(f"Author name  {author.author_name} Total books {author.total_earnings}")
# handle()

# 10
# def handle():
    # authors = Author.objects.annotate(
        # total_earnings = Sum('book__price'),
        # book_count = Count('book', filter=Q(book__published_date__year = 2023))
    # )

    # for author in authors:
        # print(f"author name {author.author_name} Total earnings {author.total_earnings} book count {author.book_count}")
# handle()

# 11
# def handle():
    # books = Book.objects.annotate(avg_price = Avg('price', filter=Q(published_date__year = 2023)))
    # for book in books:
        # print(f"Book name {book.book_name} avg price in 2023 = {book.avg_price}")
# handle()

# 12
# def handle():
    # authors = Author.objects.annotate(latest_publication_date= Max('book__published_date'))
    # authors = Author.objects.annotate(earliest_publication_date= Min('book__published_date'))

    # for author in authors:
        # print(f"{author.author_name} - Latest published book {author.latest_publication_date}")
        # print(f"{author.author_name} - Earliest published book {author.earliest_publication_date}")
# handle()
