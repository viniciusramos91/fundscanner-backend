# Generated by Django 4.1 on 2022-08-30 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RealEstateFund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8)),
                ('sector', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PriceObservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('ffo_yield', models.DecimalField(decimal_places=2, max_digits=5)),
                ('dividend_yield', models.DecimalField(decimal_places=2, max_digits=5)),
                ('p_vp', models.DecimalField(decimal_places=2, max_digits=6)),
                ('market_value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('liquidity', models.PositiveIntegerField()),
                ('property_count', models.PositiveSmallIntegerField()),
                ('square_meter_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('square_meter_rent_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('capitalization_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('average_vacancy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('real_estate_fund', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.realestatefund')),
            ],
        ),
    ]
