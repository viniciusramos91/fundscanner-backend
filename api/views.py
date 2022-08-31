from rest_framework import viewsets
from rest_framework import mixins
from api.serializers import RealEstateFundSerializer
from core.models import RealEstateFund


class RealEstateFundViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        viewsets.GenericViewSet):
    queryset = RealEstateFund.objects.filter(is_active=True).all()
    serializer_class = RealEstateFundSerializer
