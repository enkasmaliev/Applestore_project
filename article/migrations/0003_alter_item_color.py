# Generated by Django 4.2 on 2023-04-04 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_category_options_alter_item_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='color',
            field=models.CharField(choices=[('BLACK', 'black'), ('GOLD', 'gold'), ('SILVER', 'silver')], max_length=50),
        ),
    ]
