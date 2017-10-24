from django.contrib.auth import logout
from django.shortcuts import redirect

from allauth.account.views import LoginView, SignupView


class CustomSignupView(SignupView):
    template_name = 'auth_ex/registration.html'
    view_name = 'signup'


class CustomLoginView(LoginView):
    template_name = 'auth_ex/login.html'
    view_name = 'login'


def logout_user(request):
    logout(request)
    return redirect('photos:homepage')
