from django.forms import ModelForm as mf
from blog.models import Post

class PostForm(mf):
    class Meta:
        model = Post
        fields = "__all__"