import datetime

from django.db import models
from django.utils import timezone

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    def __unicode__(self):
        return self.name

class InCart(models.Model):
    course = models.ForeignKey(Course)
    in_cart_date = models.DateTimeField('date course was put in cart')

class Purchase(models.Model):
    course = models.ForeignKey(Course)
    purchase_date = models.DateTimeField('date purchased')
