# Generated by Django 5.0.2 on 2024-02-26 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.TextField()),
                ('coordinate', models.CharField(max_length=20)),
                ('temp', models.CharField(max_length=20)),
                ('pressure', models.DecimalField(decimal_places=2, max_digits=10)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
