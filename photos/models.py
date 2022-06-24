from django.db import models

class UploadPhoto(models.Model):
	image = models.ImageField(upload_to='images')