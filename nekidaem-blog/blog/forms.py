from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Post


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(
        label=_('title'),
        widget=forms.TextInput(
            attrs={'class': 'form-control','max_length': 125}),
        required=True,
    )
    description = forms.CharField(
        label=_('description'),
        widget=forms.Textarea(attrs={
            'class': 'form-control', 'style': 'resize:none;'}),
        required=True,
    )

    class Meta:
        model = Post
        fields = ('title', 'description')
