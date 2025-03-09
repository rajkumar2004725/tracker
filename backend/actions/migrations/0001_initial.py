# Generated by Django 5.1.7 on 2025-03-09 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SustainabilityAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('points', models.IntegerField()),
            ],
        ),
    ]
