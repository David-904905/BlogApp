# Generated by Django 5.1 on 2024-08-29 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_postmodel_author_postmodel_date_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={'ordering': ('-date_created',)},
        ),
    ]
