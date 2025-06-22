from django.shortcuts import render
from django.http import JsonResponse
from likes.models import Posts
from .kafka_producer import SendLikeEvent
# Create your views here.


def post_like(request, post_id):
    SendLikeEvent(post_id)
    # post = Posts.objects.get(id=post_id)
    # post.like += 1
    # post.save()
    return JsonResponse({
        'status': True,
        'message': 'Like Incremented'
    })
