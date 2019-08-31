from django.db import models
from datetime import datetime
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=30)
	content = models.TextField()
	author = models.ForeignKey('Author', on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=datetime.now)
	updated_at = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('detail',kwargs={'pk':self.pk})

class Author(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	email = models.EmailField()
	phone = models.IntegerField()

	def __str__(self):
		return self.user.username