from django import forms
from comment.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        #fields = ('title', 'author', 'body')
        exclude = ['expires_at']


