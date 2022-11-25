from django.shortcuts import render, redirect
from django.core.mail import send_mail
import os
from dotenv import load_dotenv
from django.shortcuts import get_object_or_404

from feedback.forms import FormFromFeedback, Feedback


load_dotenv()


def feedback(request):
    template_name = 'feedback/feedback.html'
    form = FormFromFeedback(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        feedback = form.save(commit=False)
        date = str(Feedback.created_on)
        feedback.save()
        send_mail(
            'Привет, твой отзыв успешно отправлен',
            date,
            os.getenv('ADMIN_EMAIL'),
            [feedback.email],
            fail_silently=False
        )
        return redirect('feedback:feedback')

    return render(request, template_name, context)
