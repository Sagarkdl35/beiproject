# Generated by Django 3.2.5 on 2022-02-07 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0016_auto_20220207_0806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='citizenship_back',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='citizenship_front',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='driving_license',
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='owner_photo',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]