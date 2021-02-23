from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from .logic import signin as do_signup, signout as do_signout
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth.models import User


@api_view(["POST"])
def signin(request):
    username = request.data.get('username', '')
    password = request.data.get('password', None)

    try:
        user, token = do_signup(request, username, password)
        return Response({
            'token': token,
            'data': UserSerializer(user).data,
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_403_FORBIDDEN)


@api_view(["POST"])
def signout(request):
    do_signout(request, user=request.user)
    return redirect('/')


@csrf_exempt
def login_view(request):
    return render(request, "portal/login.html")


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
