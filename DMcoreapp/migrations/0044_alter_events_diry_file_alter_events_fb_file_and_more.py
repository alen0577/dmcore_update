# Generated by Django 4.0.2 on 2023-05-10 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0043_alter_events_diry_file_alter_events_fb_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='diry_file',
            field=models.ImageField(null=True, upload_to='images/smo_post/'),
        ),
        migrations.AlterField(
            model_name='events',
            name='fb_file',
            field=models.ImageField(null=True, upload_to='images/smo_post/'),
        ),
        migrations.AlterField(
            model_name='events',
            name='insta_file',
            field=models.ImageField(null=True, upload_to='images/smo_post/'),
        ),
        migrations.AlterField(
            model_name='events',
            name='link_file',
            field=models.ImageField(null=True, upload_to='images/smo_post/'),
        ),
        migrations.AlterField(
            model_name='events',
            name='pin_file',
            field=models.ImageField(null=True, upload_to='images/smo_post/'),
        ),
        migrations.AlterField(
            model_name='events',
            name='qra_file',
            field=models.ImageField(null=True, upload_to='images/smo_post/'),
        ),
        migrations.AlterField(
            model_name='events',
            name='sbms_file',
            field=models.ImageField(null=True, upload_to='images/smo_post/'),
        ),
        migrations.AlterField(
            model_name='events',
            name='tumb_file',
            field=models.ImageField(null=True, upload_to='images/smo_post/'),
        ),
        migrations.AlterField(
            model_name='events',
            name='tw_file',
            field=models.ImageField(null=True, upload_to='images/smo_post/'),
        ),
        migrations.AlterField(
            model_name='events',
            name='yt_file',
            field=models.ImageField(null=True, upload_to='images/smo_post/'),
        ),
    ]
