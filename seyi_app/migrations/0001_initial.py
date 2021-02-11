# Generated by Django 2.2.2 on 2021-01-10 21:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_name', models.CharField(default='My Pic', max_length=50)),
                ('mypictures', models.ImageField(upload_to='img_gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pic', models.ImageField(upload_to='tracks_pics/')),
                ('track', models.FileField(upload_to='audio/')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Video_Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid_pic', models.ImageField(upload_to='vid_gallery')),
                ('vid_name', models.CharField(max_length=100)),
                ('vid_link', models.CharField(max_length=100)),
            ],
        ),
    ]
