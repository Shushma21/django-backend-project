from django.http import HttpResponse
from .models import UserProfile
from django.http import JsonResponse


def get_users(request):
	users = list(UserProfile.objects.values())
	return JsonResponse(users,safe = False)



def get_total_user_count(request):
	count = UserProfile.objects.count()
	return HttpResponse(f"Total user count in platform is:{count}")
