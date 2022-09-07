from rest_framework import routers
from api.views import RealEstateFundViewSet, PriceObservationViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('real-estate-funds', RealEstateFundViewSet)
router.register('price-observations', PriceObservationViewSet)

urlpatterns = router.urls
