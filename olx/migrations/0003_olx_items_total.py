# Generated by Django 3.2.9 on 2021-11-30 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0002_auto_20211130_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='olx_items',
            name='total',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
