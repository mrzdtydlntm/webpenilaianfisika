from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

class IndexHomeView(TemplateView):
    template_name = 'index.html'

class Success(TemplateView):
    template_name = 'success.html'

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
        elif user is None:
            messages.error(request, 'NIP atau Password yang Dimasukkan Salah')
            return redirect('login')
    return render(request, 'login.html')

def logoutView(request):
    if request.method == 'POST':
        if request.POST['logout'] == 'Logout':
            logout(request)
            return redirect('home')
        else:
            return redirect('home')
    return render(request, 'index.html')