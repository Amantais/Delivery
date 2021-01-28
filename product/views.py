from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import viewsets, permissions, mixins, status 
from rest_framework.decorators import action  
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from .models import Product, Category, MainComment
from .serializers import ProductSerializer, CategorySerializer, CreateUpdateProductSerializer, MainCommentSerializer,  ProductDetailSerializer
from .filters import ProductFilter


import stripe 

stripe.api_key = 'sk_test_51IB1WnBMt2sNLCqmqHitMk5CcwBFRIq1RzEA1j2uWpSHhcOIA187ywyPskW4zxU9ni9JLNt1oPcoJF9wDOqApsNz007B0wY5ZK'



class CateogriesList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_class = ProductFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductSerializer
        elif self.action == 'retrieve':
            return ProductDetailSerializer

        return CreateUpdateProductSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'search']:
            permission = [permissions.IsAuthenticated]
        else:
            permission = [permissions.IsAdminUser]
        return [permission() for permission in permission]

    @action(methods=['GET'], detail=False)
    def search(self, request):
        q = request.query_params.get('q')
        queryset = self.get_queryset()
        if q is not None:
            queryset = queryset.filter(Q(title__icontains=q) | Q(description__icontains=q))
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MainCommentViewSet(mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):

    queryset = MainComment.objects.all().order_by('-created')
    serializer_class = MainCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

