# Generated by Django 3.0.8 on 2020-07-14 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32, unique=True)),
                ('pwd', models.CharField(max_length=64)),
                ('user_type', models.IntegerField(choices=[(1, 'simple'), (2, 'vip'), (3, 'svip')])),
            ],
        ),
    ]
