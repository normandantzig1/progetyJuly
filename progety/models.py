


# Create your models here

from django.db import models
"""
#consider http://django-generic-ratings.readthedocs.io/en/latest/
class Rating(models.Model)
    1 = '1'
    2 = '2'
    3 = '3'
    4 = '4'
    5 = '5'
    """


class Term(models.Model):
    term_name=models.CharField(max_length=150)
    term_type=models.CharField(max_length=150) #type of command
    term_pub_date=models.DateTimeField('Term Pub Date')

    def __str__(self):
        return self.term_name

class Etymology(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    etymology_text=models.TextField()
    classification=models.CharField(max_length=150) #prog or tool reference
    etymology_votes = models.IntegerField(default=0)
  # rating= 
   # user=
    etymology_pub_date=models.DateTimeField('Ety date published')

    def __str__(self):
        return self.etymology_text[:50] + "..."


class Comment(models.Model):
    etymology = models.ForeignKey(Etymology, on_delete=models.CASCADE)
    comment_text= models.TextField()
    comment_votes = models.IntegerField(default=0)
    #rating=
    #user=
    comment_pub_date=models.DateTimeField('com pub date')

    def __str__(self):
        return self.comment_text[:50] + "..."

