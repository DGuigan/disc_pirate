# Generated by Django 3.1.5 on 2021-03-13 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disc_pirate_store', '0007_auto_20210313_2339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppingbasket',
            old_name='userId',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='shoppingbasketitems',
            old_name='albumId',
            new_name='album',
        ),
        migrations.RenameField(
            model_name='shoppingbasketitems',
            old_name='basketId',
            new_name='basket',
        ),
    ]
