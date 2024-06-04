from django.shortcuts import render
from .models import Food_Type,Food,Comment
from rest_framework import viewsets,permissions
from .serializer import Food_TypeSerializerclass,FoodSerializerclass,CommentSerializerclass
# Create your views here.



class Food_TypeAPIViewSet(viewsets.ModelViewSet):
    queryset = Food_Type.objects.all()
    serializer_class = Food_TypeSerializerclass
    permission_classes = (permissions.IsAuthenticated)



class FoodAPIViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializerclass
    permission_classes = (permissions.IsAuthenticated)


class CommentAPIViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializerclass
    permission_classes = (permissions.IsAuthenticated)