# Generated by Django 4.0.2 on 2023-05-15 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0047_client_information_leeds_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client_information',
            old_name='leeds',
            new_name='lc',
        ),
        migrations.RenameField(
            model_name='client_information',
            old_name='leeds_file',
            new_name='lc_file',
        ),
        migrations.RenameField(
            model_name='client_information',
            old_name='leeds_target',
            new_name='lc_target',
        ),
        migrations.RenameField(
            model_name='client_information',
            old_name='leeds_txt',
            new_name='lc_txt',
        ),
    ]
