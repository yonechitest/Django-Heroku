# Generated by Django 2.1.7 on 2019-06-07 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_place_purpose'),
    ]

    operations = [
        migrations.CreateModel(
            name='urldata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('tag1', models.CharField(blank=True, max_length=15)),
                ('tag2', models.CharField(blank=True, max_length=15)),
                ('tag3', models.CharField(blank=True, max_length=15)),
                ('tag4', models.CharField(blank=True, max_length=15)),
                ('tag5', models.CharField(blank=True, max_length=15)),
                ('tag6', models.CharField(blank=True, max_length=15)),
                ('tag7', models.CharField(blank=True, max_length=15)),
                ('tag8', models.CharField(blank=True, max_length=15)),
                ('tag9', models.CharField(blank=True, max_length=15)),
                ('tag10', models.CharField(blank=True, max_length=15)),
                ('tag11', models.CharField(blank=True, max_length=15)),
                ('tag12', models.CharField(blank=True, max_length=15)),
                ('tag13', models.CharField(blank=True, max_length=15)),
                ('tag14', models.CharField(blank=True, max_length=15)),
                ('tag15', models.CharField(blank=True, max_length=15)),
            ],
        ),
    ]