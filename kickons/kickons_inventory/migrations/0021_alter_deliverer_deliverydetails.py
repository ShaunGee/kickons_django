# Generated by Django 3.2.3 on 2021-06-24 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kickons_inventory', '0020_alter_deliverer_deliverydetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverer',
            name='DeliveryDetails',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='kickons_inventory.deliverydetails'),
        ),
    ]