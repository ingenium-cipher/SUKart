from rest_framework import serializers
from .models import *

class ProductListSerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('__all__')

    def get_company(self, obj):
        return obj.company.name

    def get_category(self, obj):
        return obj.category.name        
