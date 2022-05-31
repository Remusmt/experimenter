# Generated by Django 3.2.12 on 2022-05-02 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0004_language"),
        ("experiments", "0206_alter_nimbusfeatureconfig_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="nimbusexperiment",
            name="languages",
            field=models.ManyToManyField(blank=True, to="base.Language"),
        ),
    ]