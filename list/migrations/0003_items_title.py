# Generated by Django 4.0.2 on 2022-03-01 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_alter_items_options_items_created_items_due_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='title',
            field=models.CharField(default='default', max_length=250),
        ),
    ]
