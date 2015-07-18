from django.db import models

# Create your models here.
class Message(models.Model):
	msg_type = models.CharField(max_length=20)
	title = models.CharField(max_length=30)
	doc = models.CharField(max_length=200, null=True, default="no description")
	url = models.CharField(max_length=100, null=True, default="http://www.linkedin.com")
	img_url = models.CharField(max_length=100, null=True, default="http://www.linkedin.com")
	start_time = models.DateTimeField(null=True)
	end_time = models.DateTimeField(null=True)
	category = models.CharField(max_length=20)
	unlock_type = models.IntegerField()
	lat = models.DecimalField(decimal_places=10, max_digits=15, null=True)
	lng = models.DecimalField(decimal_places=10, max_digits=15, null=True)