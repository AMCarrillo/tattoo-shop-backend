from django.db import models

# Create your models here.

class ContactModel(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	message = models.TextField(max_length=250)

	def __str__(self):
		return self.name