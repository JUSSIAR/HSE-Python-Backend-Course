# Generated by Django 4.2.19 on 2025-02-22 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.TextField(blank=True, max_length=500)),
                ('last_name', models.TextField(blank=True, max_length=500)),
            ],
        ),
    ]
