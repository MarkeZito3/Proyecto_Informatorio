from django.db                  import models
from django.contrib.auth.models import User as user_model
from apps.blogs.models          import Post


class Comment(models.Model):
    
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    comment = models.CharField(max_length=5000)

    def __str__(self):
        return self.comment