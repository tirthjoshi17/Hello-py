from django import django
from postable import Postable
from post import Post
from comment import Comment

class Profile(models.Model):
 user = models.OneToOneField(User)
class Post(models.Model):
 posted_by = models.ForeignKey(User)
class Comment(models.Model):
 commented_by = models.ForeignKey(User)
 for_post = models.ForeignKey(Post)
class Like(models.Model):
 liked_by = models.ForeignKey(User)
 post = models.ForeignKey(Post)