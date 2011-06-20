from django.db import models

# Create your models here.
class Post(models.Model):
#    author = models.ForeignKey
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    published = models.DateTimeField(null = True)
    content = models.TextField()
    title = models.CharField(max_length = 50, null = True)
    def __unicode__(self):
        return self.content