# Generated by Django 3.0.7 on 2020-09-14 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0021_food_description_short'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='prep_time',
            field=models.CharField(choices=[('10 Minutes', '10 Minutes'), ('15 Minutes', '15 Minutes'), ('20 Minutes', '20 Minutes'), ('30 Minutes', '30 Minutes'), ('40 Minutes', '40 Minutes'), ('50 Minutes', '50 Minutes'), ('60 Minutes', '60 Minutes'), ('1 hr 10 minutes', '1 hr 10 minutes')], default='', max_length=200),
        ),
    ]