# Generated by Django 2.2.4 on 2019-12-02 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20191202_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='weigth',
            new_name='weight',
        ),
    ]
