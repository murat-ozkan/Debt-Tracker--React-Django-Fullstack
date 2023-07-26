from rest_framework.routers import DefaultRouter
from .views import DebtView

router = DefaultRouter()

router.register("debtview", DebtView)

urlpatterns = router.urls
