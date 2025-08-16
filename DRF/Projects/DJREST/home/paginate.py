from rest_framework.pagination import PageNumberPagination, CursorPagination


# 1) PageNumberPagination
# page no. will be visible like (page=2, page=3 , ...)
class LargeResultPagination(PageNumberPagination):
    page_size = 100
    max_page_size = 1000
    page_size_query_param = 'page_size' #Optional

class StandardResultPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size' 
    max_page_size = 100


# 2) CursorPagination
class CustomCursorPagination(CursorPagination):
    page_size = 2
    ordering = 'name'
