# Generated by Django 4.0.1 on 2022-01-22 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('father_name', models.CharField(max_length=200)),
                ('Age', models.IntegerField(max_length=3)),
                ('perma_street', models.CharField(max_length=200, null=True)),
                ('perma_city', models.CharField(max_length=200, null=True)),
                ('perma_state', models.CharField(max_length=200)),
                ('perma_pin', models.IntegerField(max_length=6)),
                ('pres_street', models.CharField(max_length=200, null=True)),
                ('pres_city', models.CharField(max_length=200, null=True)),
                ('pres_state', models.CharField(max_length=200)),
                ('pres_pin', models.IntegerField(max_length=6)),
                ('education', models.CharField(max_length=200, null=True)),
                ('profession', models.CharField(max_length=200, null=True)),
                ('religion', models.CharField(max_length=200, null=True)),
                ('varna', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
