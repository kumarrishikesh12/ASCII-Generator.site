# Generated by Django 3.1.6 on 2021-04-18 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_outputascii_to_generatedascii'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='generatedascii',
            name='date_shared',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='date_reported',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
