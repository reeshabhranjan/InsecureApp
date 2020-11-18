from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful, proceed to login.")
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', context={'form': form})


def homepage(request):
    return render(request, 'registration/homepage.html')
