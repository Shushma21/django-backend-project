from rest_framework import status # provides readable http status codes
from rest_framework.decorators import api_view # turns normal function into drf api view
from rest_framework.response import Response # drf's response class that  returns json
from .serializers import UserProfileSerializer # converts UserProfile objects to/from json and handles validation
from django.http import HttpResponse
from .models import UserProfile # model
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


@api_view(['GET','POST'])	#declares this endpoint accepts only GET & POST
def user_list(request):
	if request.method == 'GET':
		users = UserProfile.objects.all()
		serializer = UserProfileSerializer(users,many=True)   #many=True tells drf its a list,not a single object
		return Response(serializer.data)

	if request.method == 'POST':
		serializer = UserProfileSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
