# Generated by Django 3.1.5 on 2021-03-13 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disc_pirate_store', '0004_auto_20210313_2209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppingbasketitems',
            old_name='basket_id',
            new_name='basketId',
        ),
    ]