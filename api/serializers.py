from rest_framework import serializers
from core.models import RealEstateFund, PriceObservation


class PriceObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceObservation
        fields = '__all__'


class RealEstateFundSerializer(serializers.ModelSerializer):
    price_observations = PriceObservationSerializer(source='priceobservation_set', many=True)

    class Meta:
        model = RealEstateFund
        fields = '__all__'
