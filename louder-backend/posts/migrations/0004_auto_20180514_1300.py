# Generated by Django 2.0.5 on 2018-05-14 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_songs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='songs',
            field=models.TextField(),
        ),
    ]
