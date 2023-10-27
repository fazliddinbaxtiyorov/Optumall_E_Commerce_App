from django.urls import path

from . import views


urlpatterns = [
    path('products', views.ShowAllProducts.as_view(), name='products'),
    path('new', views.CreateNewProduct.as_view(), name='new'),
    path('<int:id>/update', views.UpdateProductById.as_view(), name='update'),
    path('category/<str:category>', views.Category.as_view(), name='search-with-category'),
    path('product/<int:id>/delete', views.DeleteProductById.as_view(), name='delete'),
    path('search?product=<str:title>', views.ProductList.as_view(), name='search'),
]

