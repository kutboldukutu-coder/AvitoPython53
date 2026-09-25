from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 5

class ReviewPagination(PageNumberPagination):
    page_size = 4
