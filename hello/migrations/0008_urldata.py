# Generated by Django 2.1.7 on 2019-06-07 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_delete_urldata'),
    ]

    operations = [
        migrations.CreateModel(
            name='urldata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopname', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=200)),
                ('shopplace1', models.CharField(blank=True, max_length=15)),
                ('shopplace2', models.CharField(blank=True, max_length=15)),
                ('shopplace3', models.CharField(blank=True, max_length=15)),
                ('shopplace4', models.CharField(blank=True, max_length=15)),
                ('shopplace5', models.CharField(blank=True, max_length=15)),
                ('tag1', models.CharField(blank=True, max_length=20)),
                ('tag2', models.CharField(blank=True, max_length=20)),
                ('tag3', models.CharField(blank=True, max_length=20)),
                ('tag4', models.CharField(blank=True, max_length=20)),
                ('tag5', models.CharField(blank=True, max_length=20)),
                ('tag6', models.CharField(blank=True, max_length=20)),
                ('tag7', models.CharField(blank=True, max_length=20)),
                ('tag8', models.CharField(blank=True, max_length=20)),
                ('tag9', models.CharField(blank=True, max_length=20)),
                ('tag10', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]