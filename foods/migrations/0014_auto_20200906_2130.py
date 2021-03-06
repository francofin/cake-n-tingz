# Generated by Django 3.0.7 on 2020-09-07 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0013_auto_20200906_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='is_breakfast',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='food',
            name='is_cake',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='food',
            name='is_dessert',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='food',
            name='is_dinner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='food',
            name='is_for_kids',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='food',
            name='is_lunch',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='food',
            name='is_salad',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='food',
            name='is_workout',
            field=models.BooleanField(default=False),
        ),
    ]
