# Generated by Django 2.2.9 on 2020-02-05 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mercury', '0006_delete_simulateddata'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AccelerationSensor',
        ),
    ]