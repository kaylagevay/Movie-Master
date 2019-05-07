

# Django will import users and validations with models
from django.contrib.auth.models import Permission, User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# The Movie class will consist of title / genre / movie_logo which will find the files
# Title and Genre will have max length 100 / 200
class Movie(models.Model):

	title   	= models.CharField(max_length=200)
	
	genre  		= models.CharField(max_length=100)
	
	movielogo  = models.FileField() 

	def __str__(self):
		return self.title
		
# This will model usres with the movie and its rating 
class Myrating(models.Model):


	user   	= models.ForeignKey(User,on_delete=models.CASCADE) 
	
	
	movie 	= models.ForeignKey(Movie,on_delete=models.CASCADE)
	
	rating 	= models.IntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(0)])
		