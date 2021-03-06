# Generated by Django 3.0.7 on 2020-09-15 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifestyle', '0004_lifestylecomment_lifestyledashboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='lifestyle',
            name='is_for_family',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lifestyle',
            name='is_for_men',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lifestyle',
            name='is_for_women',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lifestyle',
            name='is_health',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lifestyle',
            name='is_new_for_blog',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lifestyle',
            name='is_travel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lifestyle',
            name='is_workout',
            field=models.BooleanField(default=False),
        ),
    ]
