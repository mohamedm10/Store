# Generated by Django 4.0.3 on 2022-03-04 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.jpg', null=True, upload_to=''),
        ),
    ]