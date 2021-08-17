# Generated by Django 3.1.1 on 2021-06-03 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_posts_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='post/pdfs'),
        ),
        migrations.AlterField(
            model_name='events',
            name='snipet',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='category',
            field=models.CharField(choices=[('Early Years', 'Early Years'), ('primary', 'Primary'), ('news letter', 'News Letter'), ('activities', 'Activities'), ('parent teachers forum ', 'Parent Teachers Forum')], default='green', max_length=100),
        ),
        migrations.AlterField(
            model_name='posts',
            name='snipet',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
    ]