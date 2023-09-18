# Generated by Django 3.0.8 on 2021-11-01 18:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20211101_1652'),
        ('general', '0004_availabledestination_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='faculty_employees',
        ),
        migrations.AddField(
            model_name='availabledestination',
            name='delivery_boys',
            field=models.ForeignKey(blank=True, limit_choices_to={'group__name': 'Delivery Boy'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.StaffUser', verbose_name='Available Delivery Boys'),
        ),
        migrations.AlterField(
            model_name='availabledestination',
            name='city',
            field=models.CharField(default=1, max_length=200, verbose_name='City/Town'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='availabledestination',
            name='district',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='District'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='availabledestination',
            name='pincode',
            field=models.CharField(max_length=10, verbose_name='Pincode'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='city',
            field=models.CharField(max_length=50, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='district',
            field=models.CharField(max_length=50, verbose_name='District'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='pincode',
            field=models.CharField(max_length=6, verbose_name='Pincode'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='street',
            field=models.CharField(max_length=200, verbose_name='Street'),
        ),
    ]
