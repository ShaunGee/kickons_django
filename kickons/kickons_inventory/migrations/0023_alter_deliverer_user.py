# Generated by Django 3.2.3 on 2021-06-27 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kickons_inventory', '0022_auto_20210627_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverer',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='kickons_inventory.user'),
        ),
    ]