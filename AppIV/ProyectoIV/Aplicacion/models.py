from django.db import models


# Create your models here.

class Enterprise(models.Model):

	name=models.CharField(max_length=100)
	town=models.CharField(max_length=50)
	sector=models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Calification(models.Model):
	
	player=models.CharField(max_length=100)
	calification=models.IntegerField(default=0)
	enterprise=models.ForeignKey(Enterprise)
	def __str__(self):
		return self.player

