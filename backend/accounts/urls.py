from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import LoginView, LogoutView, RegisterView

urlpatterns = [
    path("register/", csrf_exempt(RegisterView.as_view()), name="auth_register"),
    path("login/", csrf_exempt(LoginView.as_view()), name="auth_login"),
    path("logout/", csrf_exempt(LogoutView.as_view()), name="auth_logout"),
]
