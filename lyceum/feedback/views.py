from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils.dateparse import parse_datetime

from feedback.models import FormFromFeedback, Feedback

def feedback(request):
    template_name = 'feedback/feedback.html'
    
    form = FormFromFeedback(request.POST or None)

    context = {
            'form': form,
        }

    if request.method == 'POST' and form.is_valid():
        feedback = Feedback.objects.create()
        text = form.cleaned_data['text']
        date = Feedback.created_on
        feedback.text = text
        feedback.save()
        send_mail(
            f'Привет, {text}',
            'Дата создания' + str(date),
            'example@yandex.ru',
            ['yandex@yandex.ru'],
            fail_silently=False
        )
        return redirect('homepage:home')#request.META.get('HTTP_REFERER'))

    return render(request, template_name, context)
