# Generated by Django 4.0.1 on 2022-01-30 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_member_ritwik'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='signature',
            field=models.ImageField(blank=True, null=True, upload_to='images/account/member/signature'),
        ),
    ]
