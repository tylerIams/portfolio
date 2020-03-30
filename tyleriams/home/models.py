from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=240, unique=True)
    announcement = models.TextField(max_length=2500)
    posted = models.DateTimeField(db_index=True, auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s, %s" % (self.title, self.posted)
