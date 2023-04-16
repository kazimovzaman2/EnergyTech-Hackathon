from .models import User, Data, DataDate
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib import auth
from rest_framework.response import Response
from .serializers import UserSerializer, DataSerializer, DataDateSerializer
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from rest_framework import generics


class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        user = self.request.user

        try:
            isAuthenticated = user.is_authenticated

            if isAuthenticated:
                return Response({ 'isAuthenticated': 'success' })
            else:
                return Response({ 'isAuthenticated': 'error' })
        except:
            return Response({ 'error': 'Something went wrong when checking authentication status' })

@method_decorator(csrf_protect, name='dispatch')
class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        abonet_code = data['abonet_code']
        password = data['password']

        if len(password) < 6:
            return Response({ 'error': 'Password must be at least 6 characters' })

        if User.objects.filter(abonet_code=abonet_code).exists():
            return Response({ 'error': 'abonet_code already exists' })

        user = User.objects.create_user(abonet_code=abonet_code, password=password)

        return Response({ 'success': 'User created successfully' })


# @method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        abonet_code = data['abonet_code']
        password = data['password']

        try:
            user = auth.authenticate(abonet_code=abonet_code, password=password)

            if user is not None:
                auth.login(request, user)
                return Response({ 'success': 'User authenticated' })
            else:
                return Response({ 'error': 'Error Authenticating' })
        except:
            return Response({ 'error': 'Something went wrong when logging in' })

class LogoutView(APIView):
    def post(self, request, format=None):
        try:
            auth.logout(request)
            return Response({ 'success': 'Loggout Out' })
        except:
            return Response({ 'error': 'Something went wrong when logging out' })

# @method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        return Response({ 'success': 'CSRF cookie set' })

class DeleteAccountView(APIView):
    def delete(self, request, format=None):
        user = self.request.user

        try:
            User.objects.filter(id=user.id).delete()

            return Response({ 'success': 'User deleted successfully' })
        except:
            return Response({ 'error': 'Something went wrong when trying to delete user' })


class ADNSU(generics.ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

class ADNSUDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer



class DataDateView(generics.ListCreateAPIView):
    queryset = DataDate.objects.all()
    serializer_class = DataDateSerializer

class DataDateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataDate.objects.all()
    serializer_class = DataDateSerializer





from django.http import JsonResponse
from api.models import User

def user_count(request):
    count = User.objects.count()
    return JsonResponse({'count': count})