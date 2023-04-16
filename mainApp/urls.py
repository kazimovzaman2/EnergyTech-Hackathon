from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainPage, name='index'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('dashboard/', views.dashboardPage, name='dashboard'),
    path('pages-calendar/', views.pagesCalendarPage, name='pages-calendar'),
    path('payment/', views.payment, name='payment'),
]
