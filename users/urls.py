from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('product/<int:pk>', views.ProductDetail, name = 'product-detail'),



    #API endpoints
    path('api/product_list/', views.ProductListView.as_view(), name = 'product-list-api'),
    path('api/product/<int:pk>', views.ProductDetailView.as_view(), name = 'product-detail-api'),
    path('api/product_search', views.ProductSearchAPI.as_view(), name = 'product-search'),

]
