# Generated by Django 2.1.7 on 2019-06-07 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_urldata_shopname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='urldata',
        ),
    ]