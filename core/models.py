from django.db import models


class RealEstateFund(models.Model):
    """
    Model entity that defines a Real Estate Fund on the application
    """
    code = models.CharField(max_length=8)
    sector = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)


class PriceObservation(models.Model):
    """
    Model that will store a periodic Price Observation of the Real Estate Fund
    """
    real_estate_fund = models.ForeignKey(RealEstateFund, on_delete=models.CASCADE)
    current_price = models.DecimalField(max_digits=8, decimal_places=2)
    ffo_yield = models.DecimalField(max_digits=5, decimal_places=2)
    dividend_yield = models.DecimalField(max_digits=5, decimal_places=2)
    p_vp = models.DecimalField(max_digits=6, decimal_places=2)
    market_value = models.DecimalField(max_digits=15, decimal_places=2)
    liquidity = models.PositiveIntegerField()
    property_count = models.PositiveSmallIntegerField()
    square_meter_price = models.DecimalField(max_digits=8, decimal_places=2)
    square_meter_rent_price = models.DecimalField(max_digits=8, decimal_places=2)
    capitalization_rate = models.DecimalField(max_digits=5, decimal_places=2)
    average_vacancy = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_created=True)
