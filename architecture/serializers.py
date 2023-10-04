from rest_framework import serializers
from .models import User, Product, ProductAccess, Lesson, ViewingHistory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAccess
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class ViewingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewingHistory
        fields = '__all__'
