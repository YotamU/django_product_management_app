# Generated by Django 3.2.9 on 2022-04-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CloudApp', '0002_auto_20220329_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='File_Size',
        ),
        migrations.AddField(
            model_name='file',
            name='Uploaded_By',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='File_Type',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
