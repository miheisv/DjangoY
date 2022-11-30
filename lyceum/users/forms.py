from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'password')
        labels = {
            CustomUser.email.field.name: 'Почта',
            CustomUser.password.field.name: 'Пароль',
        }


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'birth_day')
        labels = {
            CustomUser.email.field.name: 'Почта',
            CustomUser.first_name.field.name: 'Фамилия',
            CustomUser.last_name.field.name: 'Имя',
            CustomUser.birth_day.field.name: 'День рождения',
        }
