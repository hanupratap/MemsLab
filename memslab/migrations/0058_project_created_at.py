# Generated by Django 2.2.3 on 2019-07-21 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memslab', '0057_project_image_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]