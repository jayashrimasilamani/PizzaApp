# Generated by Django 3.0.3 on 2020-06-15 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(null=True, upload_to='pictures/'),
        ),
    ]
