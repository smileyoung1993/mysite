# Generated by Django 2.0.6 on 2018-06-28 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guestbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=2000)),
                ('regdate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
