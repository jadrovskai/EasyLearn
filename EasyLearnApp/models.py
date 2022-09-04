from django.db import models

# Create your models here.

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=50)
    subject_image = models.ImageField(upload_to="cover_images/", null=True, blank=True)
    
class Video(models.Model):
    id = models.AutoField(primary_key=True)
    video_name = models.CharField(max_length=50)
    video_image = models.ImageField(upload_to="cover_images/", null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,  null=True, blank=True)