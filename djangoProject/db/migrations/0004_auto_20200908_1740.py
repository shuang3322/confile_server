# Generated by Django 3.1.1 on 2020-09-08 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_conf_path_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conf_path',
            name='path',
            field=models.CharField(max_length=500),
        ),
    ]
