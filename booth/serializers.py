from rest_framework import serializers
from .models import Booth, Menu, Image


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'menu', 'image', 'price', 'is_soldout']


class BoothListSerializer(serializers.ModelSerializer):
    day = serializers.StringRelatedField(many=True, read_only=True)
    is_liked = serializers.BooleanField(default=False)
    
    class Meta:
        model = Booth
        fields = ['id', 'user', 'day', 'college', 'name', 'number', 'thumnail', 'description', 'is_liked', 'created_at', 'updated_at']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']


class BoothDetailSerializer(serializers.ModelSerializer):
    day = serializers.StringRelatedField(many=True, read_only=True)
    menus = MenuSerializer(read_only=True, many=True)
    images = ImageSerializer(read_only=True, many=True)
    is_liked = serializers.BooleanField(default=False)
    
    class Meta:
        model = Booth
        fields = ['id', 'user', 'day', 'college', 'name', 'number', 'thumnail', 'notice', 'description', 'images', 'menus', 'is_liked', 'like', 'created_at', 'updated_at']
