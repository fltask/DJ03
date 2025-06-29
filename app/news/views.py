from django.shortcuts import render
from .models import News_Post

# Create your views here.
def index(request):
    news = News_Post.objects.all()
    return render(request, 'news/index.html', {'news':news})