# Generated by Django 3.0.3 on 2020-08-23 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emp_management', '0003_auto_20200822_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('--', '--'), ('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='--', max_length=6),
        ),
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, default='static/avatar.png', null=True, upload_to='static/'),
        ),
    ]
