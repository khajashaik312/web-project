# Generated by Django 4.1.5 on 2023-03-15 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_signup_age_alter_signup_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='EMAIL_ID',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='PASSWORD',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='RE_PASSWORD',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='USER_NAME',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
