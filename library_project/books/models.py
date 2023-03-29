from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.TextField(max_length=50,db_index=True, unique=True)
    def __str__(self) -> str:
        return self.title


class Book(models.Model):
    title = models.TextField(max_length=75,unique=True,db_index=True)
    pub_date= models.DateField(auto_now=False, auto_now_add=False)
    author = models.TextField(max_length=75)
    description = models.TextField(max_length=175)
    category = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return f"{self.title} - {self.author} - {self.pub_date}"
