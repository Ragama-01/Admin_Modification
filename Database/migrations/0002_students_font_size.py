# Generated by Django 4.2.6 on 2023-11-08 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='font_size',
            field=models.IntegerField(default=18, verbose_name=18),
            preserve_default=False,
        ),
    ]