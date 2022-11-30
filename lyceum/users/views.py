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


'''




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


def user_profile(request, username):
    if request.method == 'POST':
        userprofile_edit = FormProfile1(request.POST, instance = request.user.get_profile())
        if userprofile_edit.is_valid():
            userprofile_edit.save()
            return redirectt('users:user_detail', username)
    else:
        return redirect('homepage:home')
    return render_to_response('carloan/editprofile.html', {'userprofile_edit': userprofile_edit}, context_instance=RequestContext(request))
    username = request.user.username
    now_user = User.objects.get(username=username)
    if request.user.is_authenticated and '/users/user_profile/' + str(now_user.username) == request.path:
        template_name = 'users/user_profile.html'
        form1 = FormProfile1(request.POST or None)
        form2 = FormProfile2(request.POST or None)
        context = {
            'form1': form1,
            'form2': form2,
            'user': now_user,
        }
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.email = form1.cleaned_data['email'] or now_user.email
            user.first_name = form1.cleaned_data['first_name'] or now_user.first_name
            user.last_name = form1.cleaned_data['last_name'] or now_user.last_name
            user.save()
            user = form2.save(commit=False)
            user.birth_day = form2.cleaned_data['birth_day'] or now_user.profile.birth_day
            user.save()
            return redirect('users:user_profile', user.username)

        return render(request, template_name, context)
    else:
        return render(request, 'homepage/homepage.html')



'''