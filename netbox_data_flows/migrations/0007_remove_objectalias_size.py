# Generated by Django 4.1.6 on 2023-02-12 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("netbox_data_flows", "0006_reindex_netbox_data_flows"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="objectalias",
            name="size",
        ),
    ]
