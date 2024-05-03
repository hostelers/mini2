from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate  # Combine import statements






def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def index(request):
    return render(request, 'index.html')
def noti(request):
    return render(request, 'noti.html')
def reset(request):
    return render(request, 'reset.html')
def submissimform(request):
    return render(request, 'submissimform.html')
def view(request):
    return render(request, 'view.html')
def feed(request):
    return render(request, 'feed.html')
def contact(request):
    return render(request, 'contact.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful sign-up
    else:
        form = UserCreationForm()
    return render(request, 'index.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after successful sign-in
    else:
        form = AuthenticationForm()
    return render(request, 'index.html', {'form': form})