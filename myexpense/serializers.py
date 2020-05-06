from rest_framework import serializers
from .models import *

class MyExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeExpense
        fields = '__all__'