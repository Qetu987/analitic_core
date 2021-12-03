# Generated by Django 3.2.9 on 2021-12-03 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0003_olx_items_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Olx_examples',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('title', models.CharField(max_length=300)),
                ('cost', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olx.olx_items')),
            ],
        ),
    ]
