# Generated by Django 2.2.3 on 2019-07-10 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memslab', '0051_auto_20190710_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pic',
            field=models.ImageField(blank=True, upload_to='news_image'),
        ),
    ]