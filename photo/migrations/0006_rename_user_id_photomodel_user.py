# Generated by Django 4.1.2 on 2022-10-18 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0005_alter_photomodel_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photomodel',
            old_name='user_id',
            new_name='user',
        ),
    ]
