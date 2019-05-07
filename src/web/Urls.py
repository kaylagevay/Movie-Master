
# The intention of this file base is routing paths
from django.urls import path

from . import views

# This is the django pathing for user auth
urlpatterns = [

    path('', views.index, name='index'),
    path('<int:movie_id>/',views.detail ,name='detail'),
    path('signup/',views.signUp,name='signup'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('recommend/',views.recommend,name='recommend')
]