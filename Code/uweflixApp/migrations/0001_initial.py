# Generated by Django 4.1.2 on 2022-12-09 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('clubID', models.AutoField(primary_key=True, serialize=False)),
                ('clubName', models.CharField(max_length=50)),
                ('cardNum', models.CharField(max_length=16)),
                ('expDate', models.DateField()),
                ('discountRate', models.FloatField()),
            ],
        ),
    ]