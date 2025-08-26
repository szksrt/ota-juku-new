from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Contact
from .forms import ContactForm

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('contact:success') # 送信成功後にリダイレクトするURL

# 送信完了ページ用のビュー（今は空でOK）
from django.views.generic import TemplateView

class ContactSuccessView(TemplateView):
    template_name = 'contact/contact_success.html'