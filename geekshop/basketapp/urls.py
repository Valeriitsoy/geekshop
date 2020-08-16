from django.urls import path

from basketapp import views

app_name = 'basketapp'

urlpatterns = [
    path('', views.basket, name='view'),
    path('add/<int:pk>', views.basket_add, name='add'),
    path('edit/<int:pk>/<int:quantity>/', views.basket_edit, name='edit'),
    path('remove/<int:pk>', views.basket_remove, name='remove'),
]
