
from django.contrib import admin
from django.urls import path


from django_test.views import comer, saludo, plantilla

urlpatterns = [
    path('admin/', admin.site.urls),
    path("comer/", comer, name="view"),
    path("saludo/", saludo, name="view"),
    path('plantilla/', plantilla, name='plantilla')
    
]
