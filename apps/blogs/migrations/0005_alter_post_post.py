# Generated by Django 3.2.9 on 2021-12-24 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_remove_post_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.TextField(),
        ),
    ]