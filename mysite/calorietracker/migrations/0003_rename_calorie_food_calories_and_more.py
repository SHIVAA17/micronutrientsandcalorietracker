# Generated by Django 4.0.3 on 2023-03-05 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calorietracker', '0002_consume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='calorie',
            new_name='calories',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='proteins',
            new_name='protein',
        ),
    ]
