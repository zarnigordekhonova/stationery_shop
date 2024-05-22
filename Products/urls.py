from django.urls import path
from .views import CategoryListView, ProductsDetailView, DetailView, AddReviewView, FilterProductsView

app_name = 'products'
urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('products/<int:pk>', ProductsDetailView.as_view(), name='pr_detail_view'),
    path('details/<int:pk>', DetailView.as_view(), name='details'),
    path('add_review/<int:pk>', AddReviewView.as_view(), name='add-review'),
    path('filter/', FilterProductsView.as_view(), name='filter')
]
