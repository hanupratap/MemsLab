# Generated by Django 2.2.3 on 2019-07-18 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memslab', '0055_auto_20190718_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_image',
            name='title',
        ),
    ]