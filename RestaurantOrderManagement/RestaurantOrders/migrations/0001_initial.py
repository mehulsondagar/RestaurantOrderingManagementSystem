# Generated by Django 3.2.9 on 2021-12-03 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Line1', models.TextField(max_length=1000)),
                ('Line2', models.TextField(max_length=1000)),
                ('City', models.TextField(max_length=100)),
                ('ZipCode', models.TextField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=100)),
                ('Mobile', models.TextField(max_length=10)),
                ('PaymentMethod', models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card')], default='Cash', max_length=4)),
                ('Address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RestaurantOrders.address')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=100)),
                ('Quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderDate', models.DateTimeField()),
                ('OrderType', models.CharField(choices=[('Pickup', 'Pickup'), ('Delivery', 'Delivery')], default='Pickup', max_length=8)),
                ('Discount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('AmountPaid', models.DecimalField(decimal_places=2, max_digits=6)),
                ('OrderStatus', models.CharField(choices=[('Created', 'Created'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], default='Created', max_length=10)),
                ('CustomerDetail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RestaurantOrders.customerdetails')),
                ('OrderItems', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RestaurantOrders.items')),
            ],
        ),
    ]
