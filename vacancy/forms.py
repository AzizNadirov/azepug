from blog.forms import GuestCommentForm as GForm
from blog.forms import UserCommentForm as UForm
from .models import Comment

class UserCommentForm(UForm):
    class Meta:
        model = Comment

class GuestCommentForm(GForm):
    class Meta:
        model = Comment

