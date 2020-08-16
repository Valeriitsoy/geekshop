from django.urls import path
from django.conf.urls.static import static
import adminapp.views as adminapp


app_name = 'adminapp'

urlpatterns = [
    path('users/create/', adminapp.UsersCreateView.as_view(), name='user_create'),
    path('users/read/', adminapp.UsersListView.as_view(), name='users'),
    path('users/delete/<int:pk>/', adminapp.UserDeleteView.as_view(), name='user_delete'),
    path('users/update/<int:pk>/', adminapp.UsersUpdateView.as_view(), name='user_update'),

    path('categories/create/', adminapp.ProductCategoryCreateView.as_view(), name='category_create'),
    path('categories/read/', adminapp.ProductCategoryListView.as_view(), name='categories'),
    path('categories/delete/<int:pk>/', adminapp.ProductCategoryDeleteView.as_view(), name='category_delete'),
    path('categories/update/<int:pk>/', adminapp.ProductCategoryUpdateView.as_view(), name='category_update'),

    path('products/create/category/<int:pk>/', adminapp.ProductCreateView.as_view(), name='product_create'),
    path('products/read/<int:pk>/', adminapp.ProductDetailsView.as_view(), name='product_read'),
    path('products/read/category/<int:pk>/', adminapp.ProductListView.as_view(), name='products'),
    path('products/delete/<int:pk>/', adminapp.ProductDeleteView.as_view(), name='product_delete'),
    path('products/update/<int:pk>/', adminapp.ProductUpdateView.as_view(), name='product_update'),
]

