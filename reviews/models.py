from django.db import models
from django.contrib.auth.models import User
import numpy as np


class Wine(models.Model):
    name = models.CharField(max_length=200)
    
    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)
        
    def __unicode__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    wine = models.ForeignKey(Wine)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)
    
class Cluster(models.Model):
    #store a name and a list of users.
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User) #ManytoMany so each user can belong to more than one cluster.

    def get_members(self):
        return "\n".join([u.username for u in self.users.all])