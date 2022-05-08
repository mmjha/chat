from django_filters import rest_framework as filters
from apptest.models import Test


class TestFilter(filters.FilterSet):
    """
    Test Filter Description
    https://django-filter.readthedocs.io/en/stable/
    """
    code = filters.CharFilter(
        field_name='code',
        lookup_expr='icontains',
        help_text='일련번호')
    start_date = filters.DateFilter(
        field_name='date',
        lookup_expr='gte',
        help_text='시작날짜')
    end_date = filters.DateFilter(
        field_name='date',
        lookup_expr='lte',
        help_text='종료날짜')

    class Meta:
        model = Test
        fields = ['start_date', 'end_date', 'code']
