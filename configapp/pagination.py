from rest_framework.pagination import PageNumberPagination


class StudentPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100


class TeacherPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100


class ParentsPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100

class CoursePagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100

class DepartmentPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100

class MonthPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50


class PaynetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50

class PaynettypePagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50


