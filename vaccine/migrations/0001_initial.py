# Generated by Django 4.0.1 on 2022-03-07 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='VaccineNeedy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('place', models.CharField(max_length=50)),
                ('refid', models.BigIntegerField()),
                ('needed_vaccine', models.ForeignKey(default='covishield', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='vaccine.vaccines')),
            ],
        ),
    ]
