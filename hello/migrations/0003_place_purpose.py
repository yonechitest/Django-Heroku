# Generated by Django 2.1.7 on 2019-06-01 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20190422_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_place', models.CharField(max_length=15)),
                ('place1', models.CharField(blank=True, max_length=15)),
                ('place2', models.CharField(blank=True, max_length=15)),
                ('place3', models.CharField(blank=True, max_length=15)),
                ('place4', models.CharField(blank=True, max_length=15)),
                ('place5', models.CharField(blank=True, max_length=15)),
                ('place6', models.CharField(blank=True, max_length=15)),
                ('place7', models.CharField(blank=True, max_length=15)),
                ('place8', models.CharField(blank=True, max_length=15)),
                ('place9', models.CharField(blank=True, max_length=15)),
                ('place10', models.CharField(blank=True, max_length=15)),
                ('place11', models.CharField(blank=True, max_length=15)),
                ('place12', models.CharField(blank=True, max_length=15)),
                ('place13', models.CharField(blank=True, max_length=15)),
                ('place14', models.CharField(blank=True, max_length=15)),
                ('place15', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='purpose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_purpose', models.CharField(max_length=15)),
                ('purpose1', models.CharField(blank=True, max_length=15)),
                ('purpose2', models.CharField(blank=True, max_length=15)),
                ('purpose3', models.CharField(blank=True, max_length=15)),
                ('purpose4', models.CharField(blank=True, max_length=15)),
                ('purpose5', models.CharField(blank=True, max_length=15)),
                ('purpose6', models.CharField(blank=True, max_length=15)),
                ('purpose7', models.CharField(blank=True, max_length=15)),
                ('purpose8', models.CharField(blank=True, max_length=15)),
                ('purpose9', models.CharField(blank=True, max_length=15)),
                ('purpose10', models.CharField(blank=True, max_length=15)),
                ('purpose11', models.CharField(blank=True, max_length=15)),
                ('purpose12', models.CharField(blank=True, max_length=15)),
                ('purpose13', models.CharField(blank=True, max_length=15)),
                ('purpose14', models.CharField(blank=True, max_length=15)),
                ('purpose15', models.CharField(blank=True, max_length=15)),
            ],
        ),
    ]
