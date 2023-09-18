# Generated by Django 3.0.8 on 2021-10-17 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courier', '0002_courier'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourierDeliveryStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_shipped', models.BooleanField(default=False, verbose_name='Courier is Shipped')),
                ('out_for_delivery', models.BooleanField(default=False, verbose_name='Courier is Out for Delivery')),
                ('is_delivered', models.BooleanField(default=False, verbose_name='Courier Delivered')),
                ('delivered_date', models.DateField(blank=True, null=True, verbose_name='Delivered Date')),
                ('courier', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='courier', to='courier.Courier', verbose_name='Courier')),
                ('delivery_boy', models.ForeignKey(blank=True, limit_choices_to={'groups__name': 'Delivery Boy'}, on_delete=django.db.models.deletion.DO_NOTHING, related_name='delivary_boy', to=settings.AUTH_USER_MODEL, verbose_name='Delivery Boy')),
                ('shipping_center', models.ForeignKey(blank=True, limit_choices_to={'groups__name': 'Shipping Center'}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='shipping_center', to=settings.AUTH_USER_MODEL, verbose_name='Shipping Center')),
            ],
            options={
                'verbose_name': 'Courier Status',
                'verbose_name_plural': 'Couriers Status',
                'ordering': ['-id'],
            },
        ),
    ]
