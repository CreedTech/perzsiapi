
from django.contrib import admin
from django.urls import path, include
# from stores.views import StoreViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter
from stores.views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers


schema_view = get_schema_view(
    openapi.Info(
        title = "Perzsi Api Calls",
        default_version='v1',
        description="Perzsi API calls",
        contact=openapi.Contact(email="creedtechh@gmail.com",),
        license=openapi.License(name="Test License")
    ),
    public = True,
    permission_classes=(permissions.AllowAny,),
)



# router.register(r'api/store', StoreViewSet, basename='stores')
# router.register(r'api/product', ProductViewSet, basename='products')



urlpatterns = [
    path('admin/', admin.site.urls),    
    # path(r'', include(router.urls)),
    path('rest_api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('stores.urls')),
    path("",schema_view.with_ui('swagger', cache_timeout=0), name='schema_swagger_ui'
    ),
    # path('api/store/', StoreApiView.as_view()),
    # path('api/store/<int:pk>/', StoreUpdate.as_view()),
    # path('api/product/', ProductApiView.as_view()),
    # path('api/product/<int:pk>/', ProductUpdate.as_view()),
]

router = DefaultRouter()
urlpatterns += router.urls