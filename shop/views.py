from rest_framework import generics
from a_panel.models import *
from .serializer import *
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from .perrmissions import IsAdminOrReadOnly

    # Category API 

class CategoryAPIPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CategoryAPIList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = CategoryAPIPagination


class CategoryAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser,)

class CategoryAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser),


    # Subcategory API 
    
class SubcategoryAPIPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000
    
class SubcategoryAPIList(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    pagination_class = SubcategoryAPIPagination
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly,)

class SubcategoryAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    pagination_class = SubcategoryAPIPagination
    permission_classes = (IsAdminUser,)
    
class SubcategoryAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    permission_classes = (IsAdminUser,)

    # Product API

class ProductAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)

class ProductAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset  =Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUser,)

class ProductAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUser,)

    # Order API

class OrderAPIList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminUser,)

class OrderAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminUser,)







