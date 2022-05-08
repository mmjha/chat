from rest_framework import serializers
from django_grpc_framework import proto_serializers
from grpc_server import test_pb2
from apptest.models import Test


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = '__all__'


class TestProtoSerializer(proto_serializers.ModelProtoSerializer):

    class Meta:
        model = Test
        proto_class = test_pb2.Test
        fields = ['id', 'code', 'date', 'count']
