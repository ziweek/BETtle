# Generated by Django 4.0.4 on 2022-05-28 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bettleApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='seocondMember',
            new_name='secondMember',
        ),
    ]
