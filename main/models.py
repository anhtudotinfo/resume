from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    image = models.ImageField(upload_to='resume_site_images/')

    def __str__(self):
        return self.subject
