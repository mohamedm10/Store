# Generated by Django 4.0.1 on 2022-02-11 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='products_purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty_in', models.IntegerField(blank=True, default=0)),
                ('qty_out', models.IntegerField(blank=True, default=0)),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField(blank=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='inventory.product')),
                ('products_purchase', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='stockout', to='inventory.products_purchase')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('discount', models.FloatField(blank=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='inventory.customer')),
                ('product_list', models.ManyToManyField(blank=True, through='inventory.products_purchase', to='inventory.Product')),
            ],
        ),
        migrations.AddField(
            model_name='products_purchase',
            name='purchase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='inventory.purchase'),
        ),
        migrations.AlterUniqueTogether(
            name='products_purchase',
            unique_together={('product', 'purchase')},
        ),
    ]