# Generated by Django 3.0.3 on 2020-08-23 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emp_management', '0004_auto_20200823_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(default=None, max_length=6, null=True),
        ),
    ]
