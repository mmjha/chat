from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    """
    Custom Pagination
    https://www.django-rest-framework.org/api-guide/pagination/
    """
    page_size = 10
    page_size_query_param = 'limit'
    
    def get_limit_number(self):
        # limit_number = self.request.query_param.get(self.page_size_query_param, 1)
        limit_number = int(self.request.GET.get(self.page_size_query_param, 1))
        return limit_number

    def get_paginated_response(self, data):
        return Response({
            'total_count': self.page.paginator.count,
            'current_page': self.page.number,
            'limit': self.get_limit_number(),
            'data': data,
        })
