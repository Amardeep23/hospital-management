# Generated by Django 4.1.7 on 2023-03-04 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0025_alter_appointment_appointmentdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointmentDate',
            field=models.DateTimeField(null=True),
        ),
    ]