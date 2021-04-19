from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from penilaian.models import Reviewer, Admin

class IndexHomeView(TemplateView):
    template_name = 'index.html'

class TechSupportView(TemplateView):
    template_name = 'tech.html'

class Success(TemplateView):
    template_name = 'success.html'

def loginView(request):
    if request.method == 'POST':
        # print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('home')
    return render(request, 'login.html')

def logoutView(request):
    if request.method == 'POST':
        # print(request.POST)
        if request.POST['logout'] == 'Logout':
            logout(request)
            return redirect('home')
        else:
            return redirect('home')
    return render(request, 'index.html')