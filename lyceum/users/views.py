from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/registration.html'


class ProfileView(UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('homepage:home')
    template_name = 'users/profile.html'

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        return super(ProfileView, self).form_valid(form)


def user_detail(request, email):
    if request.user.is_authenticated:
        template_name = 'users/user_detail.html'
        user = get_object_or_404(CustomUser, email=email)
        context = {
            'user': user,
        }
        return render(request, template_name, context)
    return redirect('homepage:home')


def user_list(request):
    if request.user.is_authenticated:
        template_name = 'users/user_list.html'
        users = get_list_or_404(CustomUser.objects.filter(is_active=True))
        context = {
            'users': users,
        }
        return render(request, template_name, context)
    return redirect('homepage:home')
