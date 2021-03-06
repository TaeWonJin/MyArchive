# Generated by Django 3.0.5 on 2020-04-26 18:09

import Nano.models
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Nano', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='descript',
            name='Image',
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', imagekit.models.fields.ProcessedImageField(null=True, upload_to=Nano.models.user_path)),
                ('Descript', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nano.Descript')),
            ],
        ),
    ]
