from django.db import models

class UserProfile(models.Model):
	email = models.EmailField(unique = True)
	fullname = models.CharField(max_length=100)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email
