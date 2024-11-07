from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('accounts:signup_success')
    
    # フォームに入力して登録ボタンを押したときにはじめて呼び出される
    def form_valid(self, form):
        user = form.save()
        self.object = user
        return super().form_valid(form)

class SignUpSuccessView(TemplateView):
    template_name = 'signup_success.html'
    
    