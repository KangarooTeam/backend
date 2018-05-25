from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Articles

def index(request):
    posts = Articles.objects.all()
    return render(request, 'homepage/wrapper.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Articles, pk=pk)
    return render(request, 'homepage/post_detail.html', {'post': post})

