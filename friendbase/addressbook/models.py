from django.db import models
import datetime

class Family(models.Model):
    family_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.family_name

class Person(models.Model):
    family = models.ForeignKey(Family)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthday = models.DateField("Birthday", blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=1024, default='', blank=True, null=True)
    picture = models.ImageField(upload_to='pics/', blank=True)
    def is_birthday_soon(self):
        if self.birthday not in [None,'']:
            days_till = (self.birthday - datetime.date.today()).days
            return (days_till < 30) and (days_till >= 0)
        else:
            return False
    def __unicode__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Meeting(models.Model):
    person = models.ForeignKey(Family)
    date_time = models.DateTimeField("Meeting Date/Time")
    notes = models.CharField(max_length=20000, default='', blank=True)
    def __unicode__(self):
        return "{} {}".format()
