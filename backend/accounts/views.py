import json
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponseBadRequest
from django.http.response import HttpResponse, HttpResponseForbidden
from django.views import View
from django import forms

from src import settings
from accounts.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
                "username",
                "first_name",
                "last_name",
                "password",
            ]

class RedirectAuthenticatedUserMixin(AccessMixin):
    """Verify that the current user is NOT authenticated."""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)


class RegisterView(RedirectAuthenticatedUserMixin, View):
    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        body = json.loads(request.body.decode())
        print(body)
        register_form = RegisterForm(body)
        print(register_form.is_valid())

        if register_form.is_valid():
            # we can now create the user
            user = User.objects.create_user(
                    username=body["username"],
                    first_name=body['first_name'],
                    last_name=body['last_name'],
                    email=body['email'],
                    password=body['password'], # passwords should be hashed for security
                    )
            user.save()
            return HttpResponse("user creation was successful")
        else:
            return HttpResponseBadRequest(register_form.errors.as_json())

    def get(
        self,
        request: HttpRequest,
        *args,
        **kwargs,
    ) -> HttpResponse:
        return HttpResponse("<h1>Register Page</h1>")


class LoginView(RedirectAuthenticatedUserMixin, View):
    redirect_authenticated_user = True

    def post(
        self, 
        request,
    ) -> HttpResponse:
        '''
        print(f"Username {request.POST.get('username')}")
        print(f"Password {request.POST.get('password')}")
        '''

        user = authenticate(
                username=request.POST.get('username'), 
                password=request.POST.get('password')
            )

        if not user is None:
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        return HttpResponseForbidden(content="Credentials are wrong")

    def get(
        self,
        request: HttpRequest,
        *args,
        **kwargs,
    ) -> HttpResponse:
        login_html = """
            <div>
                <form method="POST" action="http://localhost:8000/api/v1/accounts/login/">
                    <input type="hidden" name="csrfmiddlewaretoken" value="PASTE_TOKEN_HERE">
                    <input type="text" name="username" placeholder="Username">
                    <input type="password" name="password" placeholder="Password">
                    <button type="submit">Login</button>
                </form>
            </div>

        """
        return HttpResponse(login_html)


class LogoutView(LoginRequiredMixin, View):
    def post(
        self,
        request: HttpRequest,
    ) -> HttpResponse:
        logout(request)
        return redirect(settings.LOGOUT_REDIRECT_URL) 
