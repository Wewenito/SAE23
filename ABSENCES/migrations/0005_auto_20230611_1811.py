# Generated by Django 2.1.15 on 2023-06-11 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ABSENCES', '0004_auto_20230611_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cours',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='cours',
            name='Duree',
        ),
        migrations.RemoveField(
            model_name='cours',
            name='Groupe',
        ),
        migrations.AddField(
            model_name='cours',
            name='Groupes',
            field=models.ManyToManyField(to='ABSENCES.GroupeEtu'),
        ),
    ]
