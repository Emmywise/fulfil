from django import forms
from django.forms import ModelForm, fields
from .models import Products


class ProductForm(forms.ModelForm): #product form
    class Meta:
        model = Products
        fields = '__all__'