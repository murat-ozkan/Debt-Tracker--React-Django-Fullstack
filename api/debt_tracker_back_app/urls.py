from rest_framework.routers import DefaultRouter
from .views import DebtView

router = DefaultRouter()

router.register("tutorials", DebtView)

urlpatterns = router.urls
