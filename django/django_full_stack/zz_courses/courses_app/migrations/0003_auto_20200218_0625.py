# Generated by Django 3.0.3 on 2020-02-18 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0002_auto_20200218_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]
