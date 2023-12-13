from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']
        
        widgets = {
            "title": TextInput(attrs={
                 'class': 'form-control',
                 'placeholder': 'Name of the article'    
            }),
            "anons": TextInput(attrs={
                 'class': 'form-control',
                 'placeholder': 'Anons of the article'    
            }),
            "date": DateTimeInput(attrs={
                 'class': 'form-control',  
                 'placeholder': 'Date of Publication'
            }),
            "full_text": Textarea(attrs={
                 'class': 'form-control',  
                 'placeholder': 'Text of the article'
            }),
            
        }