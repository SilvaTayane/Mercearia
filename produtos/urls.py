from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.visualizarloja, name='loja' ),
    path('<slug:categoria_slug>/', views.visualizarloja, name='produtos_por_categoria'),
    path('<slug:categoria_slug>/<slug:produto_slug>/', views.visualizarDetalheProduto, name='visualizarDetalheProduto'),
] 
