# Generated by Django 2.1.7 on 2019-06-09 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0008_urldata'),
    ]

    operations = [
        migrations.CreateModel(
            name='suggest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggest', models.CharField(max_length=15)),
                ('suggestkana', models.CharField(max_length=30)),
            ],
        ),
    ]
