from django import forms
from users.models import User, Profile


class FormProfile1(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        fields = ('birth_day',)
        labels = {
            Profile.birth_day.field.name: 'День рождения',
        }


class FormProfile2(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',)
        labels = {
            User.email.field.name: 'Почта',
            User.first_name.field.name: 'Фамилия',
            User.last_name.field.name: 'Имя',
        }
