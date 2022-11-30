from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/registration.html'


class ProfileView(UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/profile.html'

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        return super(ProfileView, self).form_valid(form)


def user_detail(request, email):
    if request.user.is_authenticated:
        template_name = 'users/user_detail.html'
        user = CustomUser.objects.get(email=email)
        context = {
            'user': user,
        }
        return render(request, template_name, context)
    else:
        return redirect('homepage:home')


def user_list(request):
    if request.user.is_authenticated:
        template_name = 'users/user_list.html'
        users = CustomUser.objects.filter(is_active=True)
        context = {
            'users': users,
        }
        return render(request, template_name, context)
    else:
        return redirect('homepage:home')
