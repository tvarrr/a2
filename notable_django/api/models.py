from django.db import models

# Create your models here.

class Note(models.Model):
    key = models.CharField(max_length=60,default='default')
    value = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
def __str__(self):
        return '%s %s' % (self.key, self.value)