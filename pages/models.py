from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=200)
    twitter_link = models.URLField(max_length=200)
    pintrest_link = models.URLField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name

class Ashley(models.Model):
    name_element = models.CharField(max_length=300)
    years_of_exp = models.IntegerField()
    food_articles = models.IntegerField()
    lifestyle_articles = models.IntegerField()
    customers = models.IntegerField()
    home_page_about = RichTextField()
    about_me_side_bar = RichTextField()
    about_stories2 = RichTextField()
    about_short = RichTextField()
    food_detail_pre_comment = RichTextField(default = "")
    last_update = models.DateTimeField(blank=True, default=datetime.now)
    ashley_images_home = models.ImageField(upload_to='photos/%Y/%m/%d/')
    ashley_images_about1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    ashley_images_about2 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    about_side_bar = models.ImageField(upload_to='photos/%Y/%m/%d/')
    side_category_image1 = models.ImageField(upload_to='photos/%Y/%m/%d/', default="")
    side_category_image2 = models.ImageField(upload_to='photos/%Y/%m/%d/', default="")
    side_category_image3 = models.ImageField(upload_to='photos/%Y/%m/%d/', default="")

    def __str__(self):
        return self.name_element
