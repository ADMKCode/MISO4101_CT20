from django.urls import path
from .views import signin, signout, login_view, RegisterView
from django.urls import path

urlpatterns = [
    path('signin', signin, name='Sign In'),
    path('signout', signout, name='Sign Out'),
    path('login/', login_view, name='login'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]
