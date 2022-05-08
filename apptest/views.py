from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from apptest.serializers import TestSerializer
from apptest.models import Test
from apptest.filters import TestFilter


class TestViewSet(viewsets.ModelViewSet):
    """
    Test ViewSet Description
    """
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    filterset_class = TestFilter

    @swagger_auto_schema(tags=['test api description'])
    @action(detail=False, methods=['get'])
    def test(self, request):
        """
        Test function Description
        """
        queryset = Test.custom_objects.test_counts()
        return Response(queryset.values())
