# Generated by Django 4.1.5 on 2023-03-16 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_signup_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USER_NAME', models.CharField(max_length=50, null=True)),
                ('PASSWORD', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
