from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from dotenv import load_dotenv
from django.views import generic
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Profile
from .forms import FormProfile1, FormProfile2

load_dotenv()


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/registration.html'


def user_profile(request, username):
    username = request.user.username
    user = User.objects.get(username=username)
    if request.user.is_authenticated and '/users/user_profile/' + str(user.username) == request.path:
        template_name = 'users/user_profile.html'
        form1 = FormProfile1(request.POST or None)
        form2 = FormProfile2(request.POST or None)

        context = {
            'form1': form1,
            'form2': form2,
            'user': user,
        }
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            user.email = form1.cleaned_data['email']
            user.first_name = form1.cleaned_data['first_name']
            user.last_name = form1.cleaned_data['second_name']
            user.profile.birth_day = form2.cleaned_data['birth_day']
            return redirect('users:user_profile', user.username)

        return render(request, template_name, context)
    else:
        return render(request, 'homepage/homepage.html')


def user_detail(request, username):
    template_name = 'users/user_detail.html'
    user = User.objects.get(username=username)
    context = {
        'user': user,
    }
    return render(request, template_name, context)


def user_list(request):
    template_name = 'users/user_list.html'
    users = User.objects.filter(is_active=True)
    context = {
        'users': users,
    }
    return render(request, template_name, context)


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'users/user_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context
