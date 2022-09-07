from rest_framework import viewsets
from rest_framework import mixins
from api.serializers import RealEstateFundSerializer, PriceObservationSerializer
from core.models import RealEstateFund, PriceObservation


class RealEstateFundViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        viewsets.GenericViewSet):
    queryset = RealEstateFund.objects.filter(is_active=True).all()
    serializer_class = RealEstateFundSerializer


class PriceObservationViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        viewsets.GenericViewSet):
    queryset = PriceObservation.objects.all()
    serializer_class = PriceObservationSerializer
