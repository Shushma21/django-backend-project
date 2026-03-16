from django.urls import path
from .import views
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet
from .views import UserListAPIView

#router = DefaultRouter()
#router.register(r'users',UserProfileViewSet)

#urlpatterns = router.urls
urlpatterns = [
		path('user-list/',UserListAPIView.as_view()),
	]

#urlpatterns = [
#		path('',views.get_users,name='get_users'),
#		path('get_total_user_count/',views.get_total_user_count,name = 'get_total_user_count'),
#		path('create_user/<str:username>/<str:email>/',views.create_user,name = 'create_user'),
#		path('delete_user/<int:user_id>/',views.delete_user,name = 'delete_user'),
#		path('api/user_list/',views.user_list,name = 'user_list'),
#		path('api/user_detail/<int:id>/',views.user_detail,name = 'user_detail'),
#	]
