# Generated by Django 3.1.1 on 2021-06-27 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0018_userapply_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='phone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
