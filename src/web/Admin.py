#Admin auth control for registeration 
from django.contrib import admin
from .models import Movie,Myrating

admin.site.register(Movie)
admin.site.register(Myrating)
