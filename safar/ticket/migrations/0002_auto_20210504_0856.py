# Generated by Django 3.1 on 2021-05-04 08:56

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='logo',
            field=models.ImageField(default='logos/default.jpeg', upload_to='logos/'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone Number'),
        ),
    ]
