from django import forms
from .models import Snippet

class AddForm(forms.Form):
    description = forms.CharField()
    files = forms.CharField(required=False)
    link = forms.CharField(required=False)
    extra = forms.CharField(required=False)
    code = forms.CharField(widget=forms.Textarea)
    
class SnippetModelForm(forms.ModelForm):
    class Meta:
        model = Snippet
