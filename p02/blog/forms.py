from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        # 어떤 모델로 폼을 만들지 장고에게 알려줌
        model = Post
        fields = ('title', 'text')
