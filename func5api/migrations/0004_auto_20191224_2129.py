# Generated by Django 3.0 on 2019-12-24 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('func5api', '0003_fix_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='users',
            name='student_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]