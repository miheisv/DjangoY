from django.shortcuts import render, redirect
from django.core.mail import send_mail
import os
from dotenv import load_dotenv

from feedback.forms import FormFromFeedback

load_dotenv()


def feedback(request):
    template_name = 'feedback/feedback.html'
    form = FormFromFeedback(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        feedback = form.save(commit=False)
        form.save()
        send_mail(
            'Привет, твой отзыв успешно отправлен',
            'Отзыв: ' + str(form.cleaned_data['text']),
            os.getenv('ADMIN_EMAIL'),
            [form.cleaned_data['email']],
            fail_silently=False
        )
        return redirect('feedback:feedback')

    return render(request, template_name, context)
