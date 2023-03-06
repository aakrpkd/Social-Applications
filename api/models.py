from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    upvote=models.ManyToManyField(User,related_name="posts")


    def __str__(self):
        return self.title
    
    @property
    def likes_count(self):
        return self.upvote.all().count()

    @property
    def post_comments(self):
        return Comments.objects.filter(post=self)
    
    
    

class Userprofile(models.Model):
    profile_pic=models.ImageField(upload_to="images",null=True)
    bio=models.CharField(max_length=300)
    time_line_pic=models.ImageField(upload_to="images",null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")

class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=400)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    upvote=models.ManyToManyField(User,related_name="like")

    def __str__(self):
        return self.post
# Create your models here.
