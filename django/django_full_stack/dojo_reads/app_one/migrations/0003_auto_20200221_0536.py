# Generated by Django 3.0.3 on 2020-02-21 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_author_book_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
    ]
