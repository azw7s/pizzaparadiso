# Generated by Django 5.0.2 on 2024-05-26 04:30

import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=1, verbose_name='quantity')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_item', to='order.cart', verbose_name='cart')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menuitem', verbose_name='dish')),
                ('dish_option', models.ManyToManyField(related_name='dish_option', to='menu.optionvalue', verbose_name='dish option')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=30, verbose_name='payment method')),
                ('delivered', models.BooleanField(default=False, verbose_name='delivered')),
                ('ordered_date', models.DateField(auto_now_add=True, verbose_name='ordered date')),
                ('total_price', models.DecimalField(decimal_places=3, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='total price')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='customer.address')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='customer.customer', verbose_name='customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.TextField(max_length=50, verbose_name='item')),
                ('quantity', models.PositiveSmallIntegerField(default=1, verbose_name='quantity')),
                ('price', models.DecimalField(decimal_places=3, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='order.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItemOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_option', models.TextField(max_length=50, null=True, verbose_name='item option')),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item_option', to='order.orderitem')),
            ],
        ),
    ]
