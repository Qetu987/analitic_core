# Generated by Django 3.2.9 on 2021-11-30 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211108_2206'),
        ('olx', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='olx_items',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='olx_items',
            name='title',
        ),
        migrations.RemoveField(
            model_name='olx_items',
            name='url',
        ),
        migrations.AddField(
            model_name='olx_items',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.brand'),
        ),
        migrations.AddField(
            model_name='olx_items',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
        ),
        migrations.AddField(
            model_name='olx_items',
            name='heading',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.heading'),
        ),
        migrations.AddField(
            model_name='olx_items',
            name='item_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.item_model'),
        ),
        migrations.AddField(
            model_name='olx_items',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.type'),
        ),
    ]