# Generated by Django 3.0.3 on 2020-02-20 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_book_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
        migrations.AddField(
            model_name='book',
            name='added_user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='books_added', to='app_one.User'),
            preserve_default=False,
        ),
    ]
