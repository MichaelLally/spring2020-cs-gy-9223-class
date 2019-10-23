# Generated by Django 2.2.6 on 2019-10-23 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("mercury", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Vehicle",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("owner", models.CharField(max_length=30)),
                ("created_at", models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name="enginetemperaturesensor",
            name="vehicle",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="mercury.Vehicle",
            ),
            preserve_default=False,
        ),
    ]