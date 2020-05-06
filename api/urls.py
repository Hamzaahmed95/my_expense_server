from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('checkserver/',index,name='index'),
    path('auth/',include('authapp.urls')),
    path('my_expense/',include('myexpense.urls'))
]
