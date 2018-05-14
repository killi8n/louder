# Generated by Django 2.0.5 on 2018-05-14 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_fileupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.ImageField(default='no_image.png', upload_to='images')),
            ],
        ),
        migrations.DeleteModel(
            name='FileUpload',
        ),
    ]
