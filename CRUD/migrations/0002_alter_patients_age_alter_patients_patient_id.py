# Generated by Django 5.0.4 on 2024-05-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='Age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='patients',
            name='Patient_ID',
            field=models.IntegerField(max_length=3),
        ),
    ]
