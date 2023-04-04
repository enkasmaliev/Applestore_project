# Generated by Django 4.2 on 2023-04-04 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['price'], 'verbose_name': 'Продукция', 'verbose_name_plural': 'Продукции'},
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ManyToManyField(related_name='items', to='article.category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='items'),
        ),
    ]