# Generated by Django 2.2.2 on 2019-07-03 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memslab', '0040_auto_20190704_0054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='area',
            new_name='area_of_interest',
        ),
    ]
