# Generated by Django 3.0 on 2019-12-24 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('func5api', '0004_auto_20191224_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='users',
            name='student_number',
            field=models.CharField(max_length=10),
        ),
    ]