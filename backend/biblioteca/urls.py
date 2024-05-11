from django.urls import path
from .views import index, login_view, principal

urlpatterns = [
    path('', index, name='index'),  # Rota para a raiz do servidor
    path('principal/', principal, name='principal'),  # Rota para a view 'principal'
    path('login/', login_view, name='login_view'),  # Rota para a view 'login_view'
]
