# Generated by Django 3.0.7 on 2020-09-16 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_ashley_food_detail_pre_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='ashley',
            name='side_category_image1',
            field=models.ImageField(default='', upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='ashley',
            name='side_category_image2',
            field=models.ImageField(default='', upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='ashley',
            name='side_category_image3',
            field=models.ImageField(default='', upload_to='photos/%Y/%m/%d/'),
        ),
    ]
