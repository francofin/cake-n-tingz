# Generated by Django 3.0.7 on 2020-09-07 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0012_auto_20200906_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='is_featured_for_home_page',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='food',
            name='is_for_slider',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='food',
            name='is_holiday_recipe',
            field=models.BooleanField(default=False),
        ),
    ]
