# Generated by Django 3.1.1 on 2021-06-27 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_comments_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userapply',
            name='phone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
