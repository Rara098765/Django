from django.shortcuts import render
from .models import News, AboutUs

def homepage(request):
    news = News.objects.all()
    context = {'news':news}
    return render(request, 'index.html', context)

def about(request):
    about = AboutUs.objects.latest('id')
    context = {'about':about}
    return render(request, 'about.html', context)

def reviews(request):
    reviews = reviews.objects.all()
    context = {'reviews':reviews}
    return render(request, 'reviews.html', context)
