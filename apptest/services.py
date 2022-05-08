from django_grpc_framework import generics
from apptest.models import Test
from apptest.serializers import TestProtoSerializer


class TestService(generics.ModelService):
    """
    gRPC service that allows users to be retrieved or updated.
    """
    queryset = Test.objects.all()
    serializer_class = TestProtoSerializer
