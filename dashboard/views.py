from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from dashboard.models import Post


@login_required
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'dashboard/home.html', context=context)


@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')
