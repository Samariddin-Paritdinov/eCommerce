# Generated by Django 5.2.1 on 2025-06-21 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_blogpost_category_en_blogpost_category_ru_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mediafile',
            options={'verbose_name': 'Media File', 'verbose_name_plural': 'Media Files'},
        ),
    ]
