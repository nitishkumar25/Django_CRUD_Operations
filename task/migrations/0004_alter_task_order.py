# Generated by Django 3.2.6 on 2021-08-10 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20210809_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='order',
            field=models.CharField(max_length=50),
        ),
    ]