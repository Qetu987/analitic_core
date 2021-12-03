# Generated by Django 3.2.9 on 2021-12-03 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0005_alter_olx_examples_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='olx_examples',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='childrens', to='olx.olx_items'),
        ),
    ]
