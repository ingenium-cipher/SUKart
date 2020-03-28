from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.http import Http404

# Create your views here.
def home(request):
    return render(request, 'home.html')

def ProductDetail(request, pk):
    return render(request, 'product_detail.html')

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

class ProductDetailView(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductListSerializer(product)
        return Response(serializer.data)

class ProductSearchAPI(APIView):

    def post(self, request, *args, **kwargs):
        data = dict(request.data)
        search_string = data.get('search_string')[0]

        products = Product.objects.filter(title__icontains=search_string)

        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)

        # if len(products)!=0 :
        #     for product in products
