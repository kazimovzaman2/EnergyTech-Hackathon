from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect


# Create your views here.
def mainPage(request):

    return render(request, 'mainPage.html')


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        abonet_code = request.POST.get('abonet_code')
        password = request.POST.get('password')
        
        user = authenticate(request, abonet_code=abonet_code, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            context = {'error': 'Invalid credentials'}
            return render(request, 'loginPage.html', context)
    else:
        return render(request, 'loginPage.html')

def logoutPage(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

@login_required(login_url='login')
def dashboardPage(request):
    return render(request, 'mainApp/dashboard.html')


@login_required(login_url='login')
def pagesCalendarPage(request):
    return render(request, 'mainApp/pages-calendar.html')


@login_required(login_url='login')
def payment(request):
        
    return render(request, 'mainApp/payment.html')
