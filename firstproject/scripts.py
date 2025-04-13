import os
from itertools import product

import django
import itertools
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'firstproject.settings'
django.setup()
import django
import random
from faker import Faker
from home.models import Author, Book, Person
from datetime import datetime, timedelta
from django.db.models import Avg, Sum, Min, Max, Count, Q
from django.db.models import Subquery, OuterRef
from home.models import Products, Brand

# Aggregate functions
# 1
# def handle():
#     book = Book.objects.count()
#     print(book)
# handle()

# 2 -> Avg, Sum, min, max
# def handle():
#     book = Book.objects.aggregate(Price = Avg('price'))
#     book = Book.objects.aggregate(Price = Sum('price'))
#     book = Book.objects.aggregate(Price = Min('price'))
#     book = Book.objects.aggregate(Price = Max('price'))
#     print(book)
# handle()

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


# Subqueries
# 1
# def handle():
#
#     book = Book.objects.filter(
#         author = OuterRef('id')
#     ).order_by('-published_date').values('book_name')[:1]
#
#     authors = Author.objects.annotate(books = Subquery(book))
#
#     for author in authors:
#         # print(vars(author))
#         print(f"Author name is {author.author_name} and books {author.books}")
# handle()

# 2
# def handle():
#
#     book = Book.objects.filter(
#         author = OuterRef('id'),
#         published_date__year = 2023
#     ).values('author').annotate(total_price = Sum('price')).values('total_price')
#
#     authors = Author.objects.annotate(totaL_price_for_book = Subquery(book))
#
#     for author in authors:
#         # print(vars(author))
#         print(f"Author name is {author.author_name} and books {author.totaL_price_for_book}")
# handle()

# 3
# def handle():
#
#     book = Book.objects.filter(
#         author = OuterRef('id')
#     ).values('author').annotate(book_count = Count('id')).values('book_count')
#
#     authors = Author.objects.annotate(book_count = Subquery(book))
#
#     for author in authors:
#         # print(vars(author))
#         print(f"Author name is {author.author_name} and books {author.book_count}")
# handle()

# 4
# def handle():
#
#     book = Book.objects.filter(
#         author = OuterRef('id'),
#     ).values('author').annotate(avg_price = Avg('price')).values('avg_price')
#
#     authors = Author.objects.annotate(avg_price = Subquery(book))
#
#     for author in authors:
#         # print(vars(author))
#         print(f"Author name is {author.author_name} and books {author.avg_price}")
# handle()

# 5
# def handle():
#
#     book = Book.objects.filter(
#         author = OuterRef('id')
#     ).values('author').order_by('-price').values('price')[:1]
#
#     authors = Author.objects.annotate(book_price = Subquery(book))
#
#     for author in authors:
#         # print(vars(author))
#         print(f"Author name is {author.author_name} and books {author.book_price}")
# handle()

# 6
# def handle():
#
#     book = Book.objects.filter(
#         author = OuterRef('id'),
#         price__gte = 50
#     ).values('id')[:1]
#
#     authors = Author.objects.annotate(id__in = Subquery(book.values('author')))
#
#     for author in authors:
#         print(author.author_name)
#         # print(vars(author))
#         # print(f"Author name is {author.author_name} and books {author.book_price}")
# handle()

# 7
# def handle():
#
#     book = Book.objects.filter(
#         author = OuterRef('id'),
#         price__gte = 50
#     ).values('author').annotate(earning = Sum('price')).values('earning')
#
#     authors = Author.objects.annotate(Total_earning = Subquery(book))
#
#     for author in authors:
#         # print(vars(author))
#         print(f"Author name is {author.author_name} and books {author.Total_earning}")
# handle()

# 8
# def handle():
#
#     book = Book.objects.filter(
#         author = OuterRef('id'),
#         published_date__year__gte = 2023
#     ).values('author').annotate(avg_price = Avg('price')).values('avg_price')
#
#     authors = Author.objects.annotate(avg_p = Subquery(book))
#
#     for author in authors:
#         # print(vars(author))
#         print(f"Author name is {author.author_name} and books {author.avg_p}")
# handle()

# 9
# def handle():
#
#     book = Book.objects.filter(
#         author = OuterRef('id'),
#         published_date__year = 2023
#     ).values('author').annotate(book_price = Max('price')).values('book_price')\
#
#     authors = Author.objects.annotate(book_price = Subquery(book))
#
#     for author in authors:
#         # print(vars(author))
#         print(f"Author name is {author.author_name} and books {author.book_price}")
# handle()

# 10 --> Complex query
# def handle():
#
#     book = Book.objects.filter(
#         author = OuterRef('id'),
#         price__gte = 50
#     ).values('author').annotate(earning = Sum('price')).values('earning')
#
#     authors = Author.objects.annotate(Total_earning = Subquery(book))
#
#     for author in authors:
#         # print(vars(author))
#         print(f"Author name is {author.author_name} and books {author.Total_earning}")
# handle()


# Over-riding save method
# Products.objects.create(brand = Brand.objects.first(), product_name = 'Laptop with mouse razer')


# bulk_create
fake = Faker()

def createPerson(number):
    create  = [Person(person_name = fake.name()) for _ in range(number)]
    # print(create)
    Person.objects.bulk_create(create)


# bulk_delete
# def deletePerson(number):
    # for _ in range(number):
    #     person = Person.objects.first().delete()

    # or
    # Person.objects.all().delete()
# createPerson(1000)
# deletePerson(30)

# bulk_update
def updatePerson(name):
    print(Person.objects.filter(person_name__icontains = name).count())
    print(Person.objects.filter(person_name__icontains = name).update(person_name = 'Nick'))

updatePerson('davis')