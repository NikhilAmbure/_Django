from django.shortcuts import render
from .models import Product
from django.contrib.postgres.search import (SearchVector, SearchQuery, SearchRank, TrigramSimilarity)
from django.db.models import Q 

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
        # query = SearchQuery(search)
        # results = Product.objects.annotate(
        #     search = SearchVector('title') + SearchVector('description') + SearchVector('category')
        # ).filter(search = query)

        # 3
        # SearchRank
        # vector = SearchVector('title', 'description')
        # rank = SearchRank(vector, query)
        # results = Product.objects.annotate(
        #     rank = rank
        # ).order_by('-rank')

        # OR
        # rank = SearchRank(vector, query)
        # results = Product.objects.annotate(
        #     rank = rank
        # ).filter(rank__gte = 0.75).order_by('-rank')

        # 4 
        # SearchHeadline
        # Search_type





        # TrigramSimilarity
        query = SearchQuery(search)
        vector = SearchVector('title', 'description', 'category')
        rank = SearchRank(vector, query) 
        results = Product.objects.annotate(
            rank = rank,
            similarity = TrigramSimilarity("title", search) + TrigramSimilarity("description", search) + TrigramSimilarity("category", search)
        ).filter(Q(rank__gte = 0.0) | Q(similarity__gte = 0.0)).distinct().order_by('-rank', '-similarity')
    

    else:
        results = Product.objects.all()


    if request.GET.get('min_price') and request.GET.get('max_price'):
        min_price = float(request.GET.get('min_price'))
        max_price = float(request.GET.get('max_price'))
        results = results.filter(
            price__gte = min_price,
            price__lte = max_price
        ).order_by('price')

    if request.GET.get('category'):
        results = results.filter(
            category__icontains = request.GET.get('category')
        ).order_by('price')

    category = Product.objects.all().distinct('category').order_by('category')

    return render(request, 'index.html', {'results': results , 'search': search , 
                                          'categories': category})