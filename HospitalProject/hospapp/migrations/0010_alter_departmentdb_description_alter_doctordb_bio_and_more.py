# Generated by Django 4.1.7 on 2023-08-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospapp', '0009_rename_speciality_doctordb_department_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmentdb',
            name='Description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='doctordb',
            name='Bio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='nursedb',
            name='Bio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
