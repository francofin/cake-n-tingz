from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
# Create your models here.
class Food(models.Model):

    ingredients_list = (
        ('Sourdough', 'Sourdough'),
        ('Tumeric', 'Tumeric'),
        ('Cinnammon', 'Cinnammon'),
        ('Parsley', 'Parsley'),
        ('Chicken Foot','Chicken Foot'),
        ('Love', 'Love'),
        ('Sativa', 'Sativa'),
        ('Gluten Free', 'Gluten Free'),
    )

    recipe_title = models.CharField(max_length=300)
    description = RichTextField()
    food_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    food_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    food_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    food_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    food_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    food_photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    food_photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    owner = models.CharField(max_length=200)
    igredients = MultiSelectField(choices=ingredients_list)
    is_featured = models.BooleanField(default=False)
    is_for_home_page = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.recipe_title


class Comment(models.Model):

    first_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    website = models.URLField(max_length=200,  blank=True)
    food_id = models.IntegerField()
    comments = models.TextField()
    user_id = models.IntegerField(blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.comments
