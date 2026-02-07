from django.db import models

class UserProfile(models.Model):
	email = models.EmailField(unique = True)
	fullname = models.CharField(max_length=100)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.fullname



class Product(models.Model):
	productId = models.AutoField(primary_key=True)
	productName = models.CharField(max_length=100)
	productPrice = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.productName
