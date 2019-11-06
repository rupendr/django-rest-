
from rest_framework import serializers
from search.models import Category,Electric


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fileds='__all__'

class ElectricSerializer(serializers.ModelSerializer):
    class Meta:
        model=Electric
        fileds=['name','price']