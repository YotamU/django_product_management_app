# Generated by Django 3.2.9 on 2022-03-29 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CloudApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File_Name', models.CharField(max_length=200, null=True)),
                ('File_Type', models.CharField(max_length=10, null=True)),
                ('File_Size', models.CharField(max_length=200, null=True)),
                ('File', models.FileField(upload_to='Files')),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]