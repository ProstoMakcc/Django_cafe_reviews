from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Review
        fields = ['title', 'content']