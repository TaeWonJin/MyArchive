# Generated by Django 3.0.5 on 2020-05-25 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nano', '0005_auto_20200526_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='rating',
            field=models.IntegerField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')]),
        ),
    ]
