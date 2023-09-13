# Generated by Django 4.1.7 on 2023-08-02 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospapp', '0011_patientdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicineDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Medicine_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Manufacturer', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantity_Stock', models.IntegerField(blank=True, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Description', models.CharField(blank=True, max_length=300, null=True)),
                ('Medicine_Image', models.ImageField(blank=True, null=True, upload_to='medicines')),
            ],
        ),
    ]
