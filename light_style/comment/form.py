from django import forms
from comment.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'body')
        exclude = ['expires_at']
