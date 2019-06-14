from django.db import models

# Create your models here.
class track_data(models.Model):
	name=models.CharField(max_length=100)
	tracking_no=models.CharField(max_length=20)
	date=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name