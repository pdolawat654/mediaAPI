from django.db import models
from django.db.models.signals import post_delete,pre_save
from django.dispatch import receiver
from django.utils import timezone



# Create your models here.
class Posts(models.Model):
    artist_id=models.TextField(default=None)
    file=models.FileField(upload_to='Posts')
    content=models.TextField(default=None)
    upvotes=models.IntegerField(default=0)
    date=models.DateTimeField(default=timezone.now)


@receiver(post_delete, sender=Posts)
def submission_delete(sender, instance, **kwargs):
    instance.file.delete(False)

