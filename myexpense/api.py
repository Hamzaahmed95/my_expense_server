from myexpense.models import HomeExpense
from rest_framework import viewsets
from .serializers import MyExpenseSerializer

class MyExpenseViewSet(viewsets.ModelViewSet):
    queryset = HomeExpense.objects.all()
    serializer_class = MyExpenseSerializer