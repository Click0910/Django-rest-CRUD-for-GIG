from rest_framework import routers
from info_dealers.api_dealers.api import DealerViewSet

router = routers.DefaultRouter()

router.register('api/dealer', DealerViewSet, 'dealer')
router.register('api/dealer/<int:id>', DealerViewSet, 'dealer by id')


urlpatterns = router.urls

