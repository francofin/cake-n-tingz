# Generated by Django 3.0.7 on 2020-09-01 04:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0006_food_is_for_home_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('website', models.URLField(blank=True)),
                ('food_id', models.IntegerField()),
                ('comments', models.TextField()),
                ('user_id', models.IntegerField(blank=True)),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
