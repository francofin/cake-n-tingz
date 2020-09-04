from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):

    first_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.TextField()
    food_id = models.IntegerField()
    message = models.TextField()
    user_id = models.IntegerField(blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email
