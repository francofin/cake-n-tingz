# Generated by Django 3.0.7 on 2020-09-06 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0011_auto_20200906_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='food_photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='food_title',
            field=models.CharField(default='', editable=False, max_length=300),
        ),
    ]
