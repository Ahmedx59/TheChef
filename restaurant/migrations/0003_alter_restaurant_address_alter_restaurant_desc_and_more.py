# Generated by Django 5.1.2 on 2024-11-09 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_restaurant_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='desc',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='restaurant/logo/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='min_price',
            field=models.FloatField(blank=True, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='table',
            name='available',
            field=models.FloatField(blank=True, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='table',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='table',
            name='table_type',
            field=models.FloatField(blank=True, null=True, verbose_name=''),
        ),
    ]
