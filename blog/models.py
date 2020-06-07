from django.db import models

# Create your models here.
class Catagory(models.Model):
    catagory_name = models.CharField(primary_key=True,max_length=50)
    def __str__(self):
        return self.catagory_name
class Tag(models.Model):
    tag_name = models.CharField(primary_key=True,max_length=50)
    def __str__(self):
        return self.tag_name

class Blog(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=10)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    change_time = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    comment_reader = models.CharField(max_length=20)
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_blog = models.ForeignKey(Blog,on_delete=models.CASCADE)