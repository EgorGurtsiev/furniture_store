# Generated by Django 4.2.19 on 2025-04-22 14:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_discount_rename_productgroup_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='start_from',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Начало действия'),
        ),
        migrations.AlterField(
            model_name='price',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='goods.product'),
        ),
    ]
