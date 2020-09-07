from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


# Create your models here.


class Lifestyle(models.Model):

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
    category = models.CharField(max_length=300, default="")
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.lifestyle_title
