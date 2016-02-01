from django.db import models
import datetime

class Poll(models.Model):
    # Poll object
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()

class Choice(models.Model):
    # Choice object
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
