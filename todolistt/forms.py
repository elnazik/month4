from django import forms
from .models import Category

class TaskFilterForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    search = forms.CharField(max_length=56, required=False)
