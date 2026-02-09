from django.urls import path
from .import views


urlpatterns = [
		path('',views.get_users,name='get_users'),
		path('get_total_user_count/',views.get_total_user_count,name = 'get_total_user_count'),
		path('create_user/<str:username>/<str:email>/',views.create_user,name = 'create_user'),
		path('delete_user/<int:user_id>/',views.delete_user,name = 'delete_user'),
	]
