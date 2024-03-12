from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import logout


# Create your views here.

class LogoutView(View):
    # template_name = 'users/logout.html'

    def get(self, request):
        logout(request)
        # редирект куди завгодно
        return redirect(to="quotes:root")


class RegisterView(View):
    template_name = 'users/register.html'
    form_class = RegisterForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="quotes:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect(to="users:signin")
        return render(request, self.template_name, {'form': form})
