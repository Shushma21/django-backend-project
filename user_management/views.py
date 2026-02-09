from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserProfileSerializer
from django.http import HttpResponse
from .models import UserProfile
from django.http import JsonResponse


def get_users(request):
	users = list(UserProfile.objects.values())
	return JsonResponse(users,safe = False)



def get_total_user_count(request):
	count = UserProfile.objects.count()
	return HttpResponse(f"Total user count in platform is:{count}")


def create_user(request,username,email):

	if UserProfile.objects.filter(email=email).exists():
		return JsonResponse({"error":"User with this email already exists"})	

	user = UserProfile.objects.create(
			fullname = username,
			email = email
		)
	return JsonResponse({"message":"User created successfully","id":user.id})
	
def delete_user(request,user_id):
	UserProfile.objects.filter(id = user_id).delete()
	return JsonResponse({"message":"User deleted successfully"})


@api_view(['GET'])
def user_list(request):
	users = UserProfile.objects.all()
	serializer = UserProfileSerializer(users,many=True)
	return Response(serializer.data)
