# Generated by Django 3.2.3 on 2021-05-22 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kickons_inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(),
        ),
    ]
