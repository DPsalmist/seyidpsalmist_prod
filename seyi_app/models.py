from django.db import models
from django.utils import timezone

# Create your models here.
class Track(models.Model):
	name = models.CharField(max_length=100)
	pic  = models.ImageField(upload_to='tracks_pics/')
	track = models.FileField(upload_to='audio/')
	date_created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name

class ImageGallery(models.Model):
	pic_name = models.CharField(max_length=50, default='My Pic')
	mypictures = models.ImageField(upload_to='img_gallery')

	def __str__(self):
		return self.pic_name

class Video_Gallery(models.Model):
	vid_pic = models.ImageField(upload_to='vid_gallery')
	vid_name = models.CharField(max_length=100)
	vid_link = models.CharField(max_length=100)

	def __str__(self):
		return self.vid_name
