from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils.dateparse import parse_datetime
import os
from dotenv import load_dotenv

from feedback.models import FormFromFeedback, Feedback


load_dotenv()

def feedback(request):
    template_name = 'feedback/feedback.html'
    form = FormFromFeedback(request.POST or None)
    context = {
            'form': form,
        }
    if request.method == 'POST' and form.is_valid():
        feedback = Feedback.objects.create()
        text = form.cleaned_data['text']
        email = form.cleaned_data['email']
        date = Feedback.created_on
        feedback.text = text
        feedback.email = email
        feedback.save()
        send_mail(
            'Привет, это твой отзыв',
            f'Отзыв: {text},\n'
            'Дата создания: ' + str(date),
            os.getenv('ADMIN_EMAIL'),
            [feedback.email],
            fail_silently=False
        )
        return redirect('feedback:feedback')

    return render(request, template_name, context)
