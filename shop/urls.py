from . import views
from django.urls import path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename="Product")
urlpatterns = router.urls


# products = views.ProductViewSet.as_view(
#     {"get": "retrieve", "post": "create"}
# )


# app_name='shop'

# urlpatterns = [
#     url("^products", products, name="products"),
# ]