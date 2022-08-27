from django.db import models
from django.contrib.auth.models import User

# Create your models here.

READ_STATUS = (('0', 'not added'),
                ('1', 'added'),
                
                )


class Book(models.Model):
    id = models.AutoField(primary_key=True)    
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True)
    author = models.CharField(max_length=50)
    status = models.CharField(choices=READ_STATUS, max_length=20, default='0')
    cover = models.ImageField(upload_to='book-covers/', null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.book) +" "+ str(self.created)
