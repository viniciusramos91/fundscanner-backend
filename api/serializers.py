from rest_framework import serializers
from core.models import RealEstateFund


class RealEstateFundSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstateFund
        fields = '__all__'
