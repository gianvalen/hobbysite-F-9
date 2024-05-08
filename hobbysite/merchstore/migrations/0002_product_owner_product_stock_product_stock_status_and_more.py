# Generated by Django 5.0.4 on 2024-05-06 10:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0001_initial'),
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='user_management.profile'),
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_status',
            field=models.CharField(choices=[('AV', 'Available'), ('S', 'On sale'), ('OS', 'Out of stock')], default='Available', max_length=20),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('transaction_status', models.CharField(choices=[('C', 'On cart'), ('P', 'To Pay'), ('S', 'To Ship'), ('R', 'To Receive'), ('D', 'Delivered')], max_length=20)),
                ('created_on', models.DateTimeField(null=True)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyer', to='user_management.profile')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='merchstore.product')),
            ],
        ),
    ]
