from rest_framework import routers
from api.views import RealEstateFundViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('real-estate-funds', RealEstateFundViewSet)

urlpatterns = router.urls
