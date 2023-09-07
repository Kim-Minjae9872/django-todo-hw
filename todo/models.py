from django.db import models


class Todo(models.Model):
    title = models.CharField('제목', max_length=50)
    content = models.TextField('내용')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name='id_of_user')
