# Generated by Django 4.2.5 on 2023-10-01 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppointmentApp', '0006_remove_doctorsdetails_available_slots'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorsdetails',
            name='available_slots',
            field=models.IntegerField(blank=True, default=10, help_text='Number of Patients Doctor Check', null=True),
        ),
    ]
