# Generated by Django 2.0.1 on 2018-01-25 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_auto_20180125_1819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='flashParent',
            new_name='flash_parent',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='previousReport',
            new_name='previous_report',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='primaryFile',
            new_name='primary_file',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='sourceFile',
            new_name='source_file',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='sourceParent',
            new_name='source_parent',
        ),
    ]
