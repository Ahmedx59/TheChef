# Generated by Django 5.1.2 on 2024-11-11 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_restaurant_address_alter_restaurant_desc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='max_people',
            field=models.IntegerField(blank=True, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='table',
            name='available',
            field=models.CharField(choices=[('Available', 'Available'), ('Reserved', 'Reserved')], default='Reserved', max_length=50, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='table',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_table', to='restaurant.restaurant'),
        ),
        migrations.AlterField(
            model_name='table',
            name='table_type',
            field=models.CharField(choices=[('Normal', 'Normal'), ('Vib', 'Vib')], default='Normal', max_length=50, verbose_name=''),
        ),
    ]