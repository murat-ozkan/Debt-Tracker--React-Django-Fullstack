# Generated by Django 4.2.3 on 2023-07-22 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toWhom', models.CharField(max_length=50)),
                ('howMuch', models.FloatField(max_length=20)),
                ('date', models.DateField()),
            ],
        ),
    ]
