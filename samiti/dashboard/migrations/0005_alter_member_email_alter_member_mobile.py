# Generated by Django 4.0.1 on 2022-01-23 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_member_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='member',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
