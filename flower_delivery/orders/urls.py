from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('list/', views.order_list, name='order_list'),
    path('detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('update_status/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('reorder/<int:order_id>/', views.reorder, name='reorder'),
    path('all/', views.all_orders, name='all_orders'),
]
