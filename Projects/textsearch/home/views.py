from django.shortcuts import render
from .models import Product
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


def index(request):

    # FullText Search in django
    if search := request.GET.get('search'):

        # 1
        # SearchVector only
        # results = Product.objects.annotate(
        #     search = SearchVector('title') + SearchVector('description') + SearchVector('category')
        # ).filter(search = search)

        # 2 
        # SearchQuery only
        query = SearchQuery(search)
        results = Product.objects.annotate(
            search = SearchVector('title') + SearchVector('description') + SearchVector('category')
        ).filter(search = query)

        # 3
        # SearchRank
        # vector = SearchVector('title', 'description')
        # rank = SearchRank(vector, query)
        # results = Product.objects.annotate(
        #     rank = rank
        # ).order_by('-rank')

    else:
        results = Product.objects.all()

    return render(request, 'index.html', {'results': results})