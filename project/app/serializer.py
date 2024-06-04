from rest_framework import serializers
from .models import Food_Type,Food,Comment


class Food_TypeSerializerclass(serializers.Serializer):
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Food_Type.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)


class FoodSerializerclass(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    food_type_id = serializers.IntegerField()
    tarkibi = serializers.CharField(max_length=255)
    narxi = serializers.IntegerField()

    def create(self, validated_data):
        return Food.objects.create(**validated_data)



    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.food_type_id = validated_data.get('food_type_id', instance.food_type_id)
        instance.tarkibi = validated_data.get('tarkibi', instance.tarkibi)
        instance.narxi = validated_data.get('narxi', instance.narxi)



class CommentSerializerclass(serializers.Serializer):
    text = serializers.CharField(max_length=155)
    food_id = serializers.IntegerField()
    author_id = serializers.IntegerField()
    created = serializers.DateTimeField(auto_now=True)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.food_id = validated_data.get('food_id', instance.food_id)
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.created = validated_data.get('created', instance.created)