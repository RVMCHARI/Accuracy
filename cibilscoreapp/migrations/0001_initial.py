# Generated by Django 3.0.4 on 2020-03-18 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=10)),
                ('mobilenum', models.BigIntegerField()),
                ('address', models.CharField(max_length=12)),
                ('salary', models.IntegerField()),
                ('dob', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]