# Generated by Django 3.0.7 on 2020-09-06 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0009_food_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='food_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='food_photo',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='food_title',
            field=models.TextField(null=True),
        ),
    ]