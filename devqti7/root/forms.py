from django import forms
from django.core import validators
from .models import user


# class studentReg(forms.ModelForm):
#     class Meta:
#         model = user
#         fields = ['name',    'email',    'password']
#         Widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'from-control'}),
#             'password': forms.PasswordInput(attrs={'class': 'form-control'}),
#         }
# from .models import user


class studentReg(forms.ModelForm):
    class Meta:
        model = user
        fields = ['name', 'email', 'password']
        Widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),

        }
