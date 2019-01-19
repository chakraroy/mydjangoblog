from django.shortcuts import render

# Create your views here.
posts = [
    {
        'author': 'Charox',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 19, 2019',
    },
    {
        'author': 'Ali Roy',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 20, 2019',
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
