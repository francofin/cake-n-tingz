# Generated by Django 3.0.7 on 2020-09-06 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifestyle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lifestyle',
            name='category',
            field=models.CharField(default='', max_length=300),
        ),
    ]
