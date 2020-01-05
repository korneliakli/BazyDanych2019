# Generated by Django 2.2.6 on 2020-01-05 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20200105_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='customer_customer_demo',
            field=models.ManyToManyField(blank=True, db_table='customer_customer_demo', to='database.CustomerDemographics', verbose_name='Customer customer demo'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='territories',
            field=models.ManyToManyField(blank=True, db_table='employee_territories', to='database.Territories', verbose_name='Territories'),
        ),
    ]
