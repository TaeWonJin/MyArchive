# Generated by Django 3.0.5 on 2020-05-25 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nano', '0003_auto_20200525_2353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worddict',
            name='id',
        ),
        migrations.AlterField(
            model_name='worddict',
            name='word',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
