from django import forms
from .models import Movies, Category

class CustomForm(forms.Form):
    name = forms.CharField(max_length=233)
    title = forms.CharField(widget=forms.Textarea)

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'