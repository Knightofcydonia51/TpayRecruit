from . import views
from django.urls import path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# product_viewset = views.ReviewViewSet.as_view(
#     {"get": "retrieve", "patch": "partial_update", "delete": "destroy"}
# )

schema_view = get_schema_view(
    openapi.Info(
        # 필수인자
        title="Music API",
        default_version="v1",
        # 선택인자
        description = "음악관련 API서비스입니다.",
        terms_of_service="https://www.google.com/plicies/terms",
        contact = openapi.Contact(email="leavingwill@gmail.com"),
        license= openapi.License(name="SSAFY License"),
    )
)


app_name='shop'

urlpatterns = [
    path('product/', views.product_list, name='product_list'),
    path('docs/', schema_view.with_ui('redoc'), name='api_docs'),
    path('swagger/', schema_view.with_ui('swagger'), name='api_swagger'),
]