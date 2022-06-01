from django import forms
from .models import Questions, Reviews, OtinishVak,RequestHelp


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ("name", "email", "text",)
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Есіміңіз"}),
            "email": forms.EmailInput(attrs={"class": "form-control border", "placeholder": "Почтаңыз"}),
            "text": forms.Textarea(attrs={"class": "form-control border", "placeholder": "Сұрағыңыз..."}),

        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ("name", "surname", "email", "text", "image")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Есіміңіз"}),
            "surname": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Тегіңіз"}),
            "email": forms.EmailInput(attrs={"class": "form-control border", "placeholder": "Почтаңыз"}),
            "text": forms.Textarea(attrs={"class": "form-control border", "placeholder": "Біз туралы пікіріңіз..."}),

        }


class OtinishVakForm(forms.ModelForm):
    class Meta:
        model = OtinishVak
        fields = ("name", "surname", "email", "nomer", "vakancia")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Есіміңіз"}),
            "surname": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Тегіңіз"}),
            "nomer": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Телефон номеріңіз"}),
            "email": forms.EmailInput(attrs={"class": "form-control border", "placeholder": "Почтаңыз"}),

        }

class RequestHelpForm(forms.ModelForm):
    class Meta:
        model = RequestHelp
        fields = ("name", "surname", "email", "nomer", "req")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Есіміңіз"}),
            "surname": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Тегіңіз"}),
            "nomer": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Телефон номеріңіз"}),
            "email": forms.EmailInput(attrs={"class": "form-control border", "placeholder": "Почтаңыз"}),

        }
