from django.urls import path
from .views import SignupView, GetCSRFToken, LoginView, LogoutView, CheckAuthenticatedView, DeleteAccountView, ADNSU, ADNSUDetail, DataDateView, DataDateDetailView, user_count

urlpatterns = [
    path('authenticated/', CheckAuthenticatedView.as_view()),
    path('register/', SignupView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('delete/', DeleteAccountView.as_view()),
    path('csrf_cookie/', GetCSRFToken.as_view()),

    path('ml-adnsu/', ADNSU.as_view()),
    path('ml-adnsu/<int:pk>/', ADNSUDetail.as_view()),

    path('ml-date/', DataDateView.as_view()),
    path('ml-date/<int:pk>/', DataDateDetailView.as_view()),
    path('user_count/', user_count, name='user_count'),
]
