# Generated by Django 4.2 on 2023-04-16 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basis', '0002_alter_company_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='debt',
            field=models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=10),
        ),
    ]
