from django.db import models

# Create your database models here.
class Room(models.Model):
    # host = 
    # topic =
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)   # blanks allowed
    #participants = 
    updated = models.DateTimeField(auto_now=True)   # timestamp for when saved
    created = models.DateTimeField(auto_now_add=True)   # timestamp for when created

    def __str__(self):
        return self.name
