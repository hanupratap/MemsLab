# Generated by Django 2.2.3 on 2019-07-18 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memslab', '0054_remove_news_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pic',
            field=models.ImageField(blank=True, upload_to='news_images'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_pic',
            field=models.ImageField(blank=True, upload_to='project_image'),
        ),
    ]
