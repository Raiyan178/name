# Generated by Django 4.0.1 on 2022-01-28 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fahadsapp', '0014_alter_uploadportfolio_threed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
