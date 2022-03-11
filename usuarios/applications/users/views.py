from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

# Create your views here.
from django.views.generic import (
    View,
    CreateView
)
from django.views.generic.edit import (
    FormView
)

from usuarios.applications.users.functions import code_generator
from .models import User
from .forms import(
    UserRegisterForm, 
    LoginForm,
    UpdatePasswordForm
)
from .functions import code_generator

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):

        codigo = code_generator()
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombre = form.cleaned_data['nombre'],
            apellido = form.cleaned_data['apellido'],
            sexo = form.cleaned_data['sexo'],
            codregistro = codigo
        )
        asunto = 'Validacion de email'
        mensaje = 'Codigo de verificacion: ' + codigo
        email_remitente = 'frpizarrob@gmail.com'
        send_mail(asunto, mensaje, email_remitente, [form.cleaned_data['email'],])
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )


class Login(FormView):
    template_name= 'users/login.html'
    form_class=LoginForm
    success_url= reverse_lazy('home_app:panel')

    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )
        login(self.request, user)
        return super(Login, self).form_valid(form)


class Logout(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )


class UpdatePassword(LoginRequiredMixin, FormView):
    template_name= 'users/update.html'
    form_class = UpdatePasswordForm
    success_url= reverse_lazy('users_app:user-login')
    login_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            username = usuario.username,
            password = form.cleaned_data['password1']
        )
        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()
        logout(self.request)
        return super(UpdatePassword, self).form_valid(form)