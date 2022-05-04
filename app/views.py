from time import sleep
from django.shortcuts import render
from django.views.generic import CreateView

from .forms import ContactForm
from .models import Contact
from .tasks import add, send_beat_email, send_spam
from django.core.mail import send_mail

def index(request):
    add.delay(1, 2)
    return render(request, 'index.html')


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'contacts.html'

    def form_valid(self, form):
        form.save()
        send_spam.delay(form.instance.email)
        return super().form_valid(form)