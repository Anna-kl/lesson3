from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=126)
    rating = models.IntegerField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=126)
    text = models.TextField()
    dttm_created = models.DateTimeField(auto_created=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Test(models.Model):
    text = models.TextField()
    answer1 = models.BooleanField(verbose_name='test1')
    answer2 = models.BooleanField(verbose_name='test2')


    def __str__(self):
        return self.text

# Create your models here.
