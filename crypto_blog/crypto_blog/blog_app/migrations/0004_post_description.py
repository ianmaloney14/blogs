# Generated by Django 4.1.3 on 2022-11-28 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_post_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='In this article...', max_length=255),
        ),
    ]
