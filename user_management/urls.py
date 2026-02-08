from django.urls import path
from .import views


urlpatterns = [
		path('',views.get_users,name='get_users'),
		path('get_total_user_count/',views.get_total_user_count,name = 'get_total_user_count'),
	]
