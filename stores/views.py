from django.shortcuts import render

# Create your views here.
# from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import StoreSerializer
from .models import *
# from rest_framework import filters
from rest_framework import generics
from rest_framework import status

@api_view(['GET'])
def getRoutes(request):
    routes = [
        # store routes
        {
            'Endpoint': '/stores/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of stores'
        },
        {
            'Endpoint': '/stores/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single store object'
        },
        {
            'Endpoint': '/stores/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new store with data sent in post request'
        },
        {
            'Endpoint': '/stores/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing store with data sent in post request'
        },
        {
            'Endpoint': '/stores/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing store'
        },
        # product routes
        {
            'Endpoint': '/products/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of products'
        },
        {
            'Endpoint': '/products/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single product object'
        },
        {
            'Endpoint': '/products/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new product with data sent in post request'
        },
        {
            'Endpoint': '/products/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing product with data sent in post request'
        },
        {
            'Endpoint': '/products/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing product'
        }
    ]
    return Response(routes)

@api_view(['GET'])
def getStores(request):
    queryset = Store.objects.all()
    serializer = StoreSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getStore(request, pk):
    queryset = Store.objects.get(id=pk)
    serializer = StoreSerializer(queryset, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createStore(request):
    data = request.data
    serializer = StoreSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def updateStore(request,pk):
    data = request.data
    queryset = Store.objects.get(id=pk)
    serializer = StoreSerializer(queryset, data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteStore(request,pk):
    queryset = Store.objects.get(id=pk)
    queryset.delete()
    return Response("Deleted")

class StoreApiView(generics.ListCreateAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class StoreUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()


# class ProductApiView(generics.ListCreateAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()

#     def perform_create(self, serializer):
#         serializer.save()

# class ProductUpdate(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()


# class StoreViewSet(viewsets.ModelViewSet):
#     """
#     List all stores, or create a new store.
#     """
#     queryset = Store.objects.all()
#     serializer_class = StoreSerializer

#     def perform_create(self, serializer):
#         serializer.save()

#     def get_queryset(self):
#         queryset = Store.objects.all()
#         id = self.request.query_params.get('id', None)
#         if id is not None:
#             queryset = queryset.filter(id=id)
#         return queryset

#     # def delete(self, request):
#     #     queryset = Store.objects.all()
#     #     if request.method == 'DELETE':


# class ProductViewSet(viewsets.ModelViewSet):
#     """
#     List all products, or create a new product.
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [filters.OrderingFilter]
#     ordering_fields = ['creation_date']

#     def perform_create(self, serializer):
#         serializer.save()

#     def get_queryset(self):
#         all_products = {}

#         queryset = Product.objects.all()
#         id = self.request.query_params.get('id', None)
#         if id is not None:
#             queryset = queryset.filter(id=id)
#         return queryset


# class TeamViewSet(viewsets.ModelViewSet):
#     """
#     List all stores, or create a new store.
#     """
#     queryset = Team.objects.all()
#     serializer_class = StoreSerializer

#     def perform_create(self, serializer):
#         serializer.save()

#     def get_queryset(self):
#         queryset = Team.objects.all()
#         id = self.request.query_params.get('id', None)
#         if id is not None:
#             queryset = queryset.filter(id=id)
#         return queryset# from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import StoreSerializer
from .models import *
# from rest_framework import filters
from rest_framework import generics
from rest_framework import status

@api_view(['GET'])
def getRoutes(request):
    routes = [
        # store routes
        {
            'Endpoint': '/stores/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of stores'
        },
        {
            'Endpoint': '/stores/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single store object'
        },
        {
            'Endpoint': '/stores/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new store with data sent in post request'
        },
        {
            'Endpoint': '/stores/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing store with data sent in post request'
        },
        {
            'Endpoint': '/stores/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing store'
        },
        # product routes
        {
            'Endpoint': '/products/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of products'
        },
        {
            'Endpoint': '/products/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single product object'
        },
        {
            'Endpoint': '/products/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new product with data sent in post request'
        },
        {
            'Endpoint': '/products/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing product with data sent in post request'
        },
        {
            'Endpoint': '/products/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing product'
        }
    ]
    return Response(routes)

@api_view(['GET'])
def getStores(request):
    queryset = Store.objects.all()
    serializer = StoreSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getStore(request, pk):
    queryset = Store.objects.get(id=pk)
    serializer = StoreSerializer(queryset, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createStore(request):
    data = request.data
    serializer = StoreSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def updateStore(request,pk):
    data = request.data
    queryset = Store.objects.get(id=pk)
    serializer = StoreSerializer(queryset, data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteStore(request,pk):
    queryset = Store.objects.get(id=pk)
    queryset.delete()
    return Response("Deleted")

class StoreApiView(generics.ListCreateAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class StoreUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()


# class ProductApiView(generics.ListCreateAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()

#     def perform_create(self, serializer):
#         serializer.save()

# class ProductUpdate(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()


# class StoreViewSet(viewsets.ModelViewSet):
#     """
#     List all stores, or create a new store.
#     """
#     queryset = Store.objects.all()
#     serializer_class = StoreSerializer

#     def perform_create(self, serializer):
#         serializer.save()

#     def get_queryset(self):
#         queryset = Store.objects.all()
#         id = self.request.query_params.get('id', None)
#         if id is not None:
#             queryset = queryset.filter(id=id)
#         return queryset

#     # def delete(self, request):
#     #     queryset = Store.objects.all()
#     #     if request.method == 'DELETE':


# class ProductViewSet(viewsets.ModelViewSet):
#     """
#     List all products, or create a new product.
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [filters.OrderingFilter]
#     ordering_fields = ['creation_date']

#     def perform_create(self, serializer):
#         serializer.save()

#     def get_queryset(self):
#         all_products = {}

#         queryset = Product.objects.all()
#         id = self.request.query_params.get('id', None)
#         if id is not None:
#             queryset = queryset.filter(id=id)
#         return queryset


# class TeamViewSet(viewsets.ModelViewSet):
#     """
#     List all stores, or create a new store.
#     """
#     queryset = Team.objects.all()
#     serializer_class = StoreSerializer

#     def perform_create(self, serializer):
#         serializer.save()

#     def get_queryset(self):
#         queryset = Team.objects.all()
#         id = self.request.query_params.get('id', None)
#         if id is not None:
#             queryset = queryset.filter(id=id)
#         return queryset