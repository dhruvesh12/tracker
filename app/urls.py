
from django.urls import path
from app.views import *

urlpatterns = [
	path('',home, name='home'),
	path('add',add,name='add'),
	path('detail/<int:pk>/',track_detail,name='track_detail'),
    #path('search/<int:pk>/',song_detail, name='song_detail'),
]