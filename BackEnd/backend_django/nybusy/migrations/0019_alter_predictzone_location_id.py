# Generated by Django 4.2.2 on 2023-07-25 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("nybusy", "0018_remove_taxizone_id_alter_taxizone_location_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="predictzone",
            name="location_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="nybusy.taxizone",
            ),
        ),
    ]