from rest_framework import serializers
from .models import Day_Store
class Day_StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Day_Store
        fields = ('id', 'Title', 'Description', 'Date', 'Completed')