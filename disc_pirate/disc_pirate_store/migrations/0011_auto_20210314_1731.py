# Generated by Django 3.1.5 on 2021-03-14 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disc_pirate_store', '0010_order_cardnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cardNumber',
            field=models.IntegerField(),
        ),
    ]