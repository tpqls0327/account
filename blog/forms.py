from django import forms
from .models import Blog,Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog 

        fields = '__all__' 
        exclude = ['pub_date']

        widgets = { 
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {"body",}

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class' : 'form-control'})
        self.fields['body'].widget.attrs.update({'class' : 'form-control'})