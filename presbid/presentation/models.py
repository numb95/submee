from django.db import models
from django.utils import timezone

from accounts.models import CustomUser

class Session(models.Model):
    date = models.DateTimeField()
    number = models.PositiveSmallIntegerField(max_length=10,unique=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "number: %s date: %s" % (self.number, self.date)


class Presentation(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    created_date = models.DateTimeField(default=timezone.now)
    person = models.ForeignKey(CustomUser)

    def __str__(self):
        return "title: %s person: %s" % (self.title, self.person)





class Comment(models.Model):
    text = models.CharField(max_length=200)
    sender_name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=10)

    def __str__(self):
        return "name: %s text: %s" % (self.sender_name, self.text)

class ReplyComment(models.Model):
    comment = models.ForeignKey(Comment, related_name='+')
    reply_to = models.ForeignKey(Comment, related_name='+')

    def __str__(self):
        return "%s -- %s" % (self.comment, self.reply_to)
