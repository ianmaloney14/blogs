# Generated by Django 4.1.4 on 2023-03-28 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_category_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(blank=True, default='images/img-not-found.png', null=True, upload_to='media/images/'),
        ),
    ]
