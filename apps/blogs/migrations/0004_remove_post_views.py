# Generated by Django 3.2.9 on 2021-12-24 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_post_image_header'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
    ]