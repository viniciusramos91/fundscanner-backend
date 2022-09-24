from django.http import QueryDict
from rest_framework import serializers
from core.models import RealEstateFund, PriceObservation


class PriceObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceObservation
        fields = '__all__'
    
    def to_internal_value(self, data):
        data = data.copy()

        if data.get('ticker', None):
            data['real_estate_fund'] = RealEstateFund.objects.get(code=data.get('ticker')).id
            del data['ticker']

        return super(PriceObservationSerializer, self).to_internal_value(data)


class RealEstateFundSerializer(serializers.ModelSerializer):
    price_observations = PriceObservationSerializer(source='priceobservation_set', many=True, read_only=True)

    class Meta:
        model = RealEstateFund
        fields = '__all__'
