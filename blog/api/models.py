from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):

    Catagory=(
              ('Renegade','Renegade'),
              ('News','News'),
               ('Magazine','Magazine'),
               ('TRavel-News','Travel_News')
              )
    title= models.CharField(max_length=100)
    description=models.TextField()
    content= models.TextField()
    date_posted=models.DateField(default=timezone.now)
    category= models.CharField(max_length=160,null=True,choices=Catagory, default='Web-dev')

    def __str__(self):
        return self.title