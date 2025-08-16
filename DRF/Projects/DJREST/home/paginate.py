from rest_framework.pagination import PageNumberPagination, CursorPagination
from django.core.paginator import EmptyPage
from rest_framework.exceptions import ValidationError

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



# CustomPagination by modifting django's default pagination
def paginate(data, paginator, pagenumber):

    # check are there enough pages
    if int(pagenumber) > paginator.num_pages:
        raise ValidationError("Not enough pages.", code=404)
    
    # check for previous page number
    try:
        previous_page_number = paginator.page(pagenumber).previous_page_number()
    except EmptyPage:
        previous_page_number = None


    # check for next page number
    try:
        next_page_number = paginator.page(pagenumber).next_page_number()
    except EmptyPage:
        next_page_number = None
    

    # For which page number data we want to show
    data_to_show = paginator.page(pagenumber).object_list
    return{
        'pagination':{
            'previous_page_number': previous_page_number,
            'is_previous_page': paginator.page(pagenumber).has_previous(),
            'next_page_number': next_page_number,
            'is_next_page': paginator.page(pagenumber).has_next(),
            'start_index': paginator.page(pagenumber).start_index(),
            'end_index': paginator.page(pagenumber).end_index(),
            'total_entries': paginator.count,
            'total_pages': paginator.num_pages,
            'page': pagenumber
        },
        'results': data_to_show
    }
