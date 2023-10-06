from myapp.views import StatisticsView, UserProductView, UserProductDetailView
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("static", StatisticsView, "tags")
router.register("product", UserProductView, "ingredients")
router.register("detail", UserProductDetailView, "recipes")

urlpatterns = (
    path("", include(router.urls)),
)
