from django.shortcuts import render
from django.http import JsonResponse
from .script import scrap_news
from .models import News


def scrap_json(request):
    scrap_news()
    return JsonResponse(
        {
            "status": True,
            "message": "scraper executed"
        }
    )


def index(request):
    return render(request, 'index.html', context={
        "news_data": News.objects.all()
    })