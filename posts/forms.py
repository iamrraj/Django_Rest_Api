from django import forms

# from pagedown.widgets import PagedownWidget
# from django.forms.utils import flatatt

from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(max_length=200)
    publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publish",
        ]