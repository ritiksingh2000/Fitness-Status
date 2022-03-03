from django import forms
from .models import Article

class AddArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'author',
            'author_email',
            'category',
            'thumbnail',
            'body',
        ]

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control p-2'}),
            'author' : forms.TextInput(attrs={'class': 'form-control p-2'}),
            'author_email' : forms.TextInput(attrs={'class': 'form-control p-2'}),
            'category' : forms.Select(attrs={'class': 'form-control p-2'}),
            'body' : forms.Textarea(attrs={'class': 'form-control p-2'}),
        }