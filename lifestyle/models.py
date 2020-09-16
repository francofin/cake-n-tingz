from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


# Create your models here.


class Lifestyle(models.Model):

    category = (
        ('Workouts', 'Workouts'),
        ('health', 'health'),
        ('women', 'women'),
        ('men', 'men'),
    )

    lifestyle_title = models.CharField(max_length=300)
    description = RichTextField()
    #Max length for description_short is 50
    description_short = RichTextField(default="")
    lifestyle_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    lifestyle_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    lifestyle_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    lifestyle_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    lifestyle_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    lifestyle_photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    lifestyle_photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    owner = models.CharField(max_length=200)
    is_for_lifestyle_page = models.BooleanField(default=False)
    is_workout = models.BooleanField(default=False)
    is_health = models.BooleanField(default=False)
    is_new_for_blog = models.BooleanField(default=False)
    is_travel = models.BooleanField(default=False)
    is_for_women = models.BooleanField(default=False)
    is_for_men = models.BooleanField(default=False)
    is_for_family = models.BooleanField(default=False)
    category = models.CharField(max_length=300, default="")
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.lifestyle_title

class LifestyleComment(models.Model):

    first_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    website = models.URLField(max_length=200,  blank=True)
    lifestyle_id = models.IntegerField()
    comments = models.TextField()
    user_id = models.IntegerField(blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email


class LifestyleDashboard(models.Model):
    lifestyle_title = models.CharField(max_length=300, default="", editable=False)
    user_id = models.IntegerField()
    life_id = models.IntegerField()
    life_photo = models.ImageField(blank=True)
    life_description = models.TextField(null=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    def __int__(self):
        return self.lifestyle_title
