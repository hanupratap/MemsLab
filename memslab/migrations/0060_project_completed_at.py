# Generated by Django 2.2.3 on 2019-07-21 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memslab', '0059_auto_20190721_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='completed_at',
            field=models.DateTimeField(null=True),
        ),
    ]