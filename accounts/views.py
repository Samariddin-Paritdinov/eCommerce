from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.shortcuts import redirect
from django.contrib.auth import authenticate


@login_required
def profile_view(request):
    return render(request, 'auth/profile.html')

def logout_view(request):
    logout(request)
    return redirect('common:index')  

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('common:index')
        else:
            return render(request, 'auth/login.html', {'error': 'Invalid credentials'})
    return render(request, 'auth/login.html')