# Generated by Django 4.0.1 on 2022-03-02 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0001_initial'),
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VaccineStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('vaccine_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccine.vaccines')),
            ],
        ),
    ]
