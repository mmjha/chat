"""chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from apptest.views import TestViewSet
from apptest.services import TestService
from grpc_server import test_pb2_grpc
from graphene_django.views import GraphQLView

router = DefaultRouter()
router.register(r'api/test', TestViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="chat",
        default_version='1',
        description="chat API 문서",
        terms_of_service="",
        # contact=openapi.Contact(email="이메일"),
        # license=openapi.License(name="mit"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path(r'graphql/', GraphQLView.as_view(graphiql=True)),
    # path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc-v1'),
    # path(r'test', include('apptest.urls'))
]
urlpatterns += router.urls

def grpc_handlers(server):
    test_pb2_grpc.add_TestControllerServicer_to_server(TestService.as_servicer(), server)
