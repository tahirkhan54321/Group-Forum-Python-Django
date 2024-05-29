# This file is where you define your data models, 
# which are Python classes that represent database tables.

from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your database models here.

# This is the topic the users will talk about
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# This is the individual room a person can join (message board)
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) # a room can only have one topic
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)   # blanks allowed
    #participants = 
    updated = models.DateTimeField(auto_now=True)   # timestamp for when saved
    created = models.DateTimeField(auto_now_add=True)   # timestamp for when created

    # String representation
    def __str__(self):
        return self.name

# This is the messages a user can make
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # note that we are using the default django User as imported
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # one to many relationship, related to Room. CASCADE - when a room is deleted, all its messages are deleted
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)   # timestamp for when saved
    created = models.DateTimeField(auto_now_add=True)   # timestamp for when created

    # String representation
    def __str_(self):
        return self.body[0:50]