# Generated by Django 4.1.4 on 2024-08-19 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_urldb_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urldb',
            name='short_url',
            field=models.TextField(max_length=40),
        ),
    ]
