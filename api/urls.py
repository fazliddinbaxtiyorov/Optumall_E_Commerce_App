from django.urls import path
from .views import ShowAllProducts, CreateNewProduct, UpdateProductById, DeleteProductById

urlpatterns = [
    path('api/products', ShowAllProducts.as_view()),
    path('api/new', CreateNewProduct.as_view()),
    path('api/<int:id>/update', UpdateProductById.as_view()),
    path('api/delete/<int:id>/cart', DeleteProductById.as_view()),
]
