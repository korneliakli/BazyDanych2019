# Generated by Django 2.2.6 on 2020-01-05 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='discontinued',
            field=models.IntegerField(),
        ),
    ]