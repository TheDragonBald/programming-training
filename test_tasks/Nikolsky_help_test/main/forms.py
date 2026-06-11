from django import forms

from .models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['name', 'phone', 'email', 'subject', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        labels = {
            'name': 'Имя',
            'phone': 'Телефон',
            'email': 'Email',
            'subject': 'Тема',
            'text': 'Текст обращения',
        }