# Generated by Django 5.0.4 on 2024-05-03 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0002_alter_patients_age_alter_patients_patient_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='Patient_ID',
            field=models.IntegerField(),
        ),
    ]
