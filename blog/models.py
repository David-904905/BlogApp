from django.db import models
from django.contrib.auth.models import User
from users.models import UserProfile
# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    # the models.CASCADE tells django to delete everything associated with the user when the user is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def comment_count(self):
        return self.commentmodel_set.all().count()
    
    def comments(self):
        return self.commentmodel_set.all()




    def __str__(self):
        return self.title
    

class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=128)

    def __str__(self):
        return self.user.username