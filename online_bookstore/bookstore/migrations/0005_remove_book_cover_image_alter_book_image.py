# Generated by Django 5.1.2 on 2024-10-20 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_book_is_best_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cover_image',
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
