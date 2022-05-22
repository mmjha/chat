import graphene
from graphene_django import DjangoObjectType

from apptest.models import Test

class TestType(DjangoObjectType):
    class Meta:
        model = Test
        fields = ("id", )

class Query(graphene.ObjectType):
    all_test = graphene.List(TestType)

    def resolve_all_test(root, info):
        # We can easily optimize query count in the resolve method
        return Test.objects.select_related("test_info").all()

schema = graphene.Schema(query=Query)
