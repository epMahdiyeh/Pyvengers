from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (pineapple_list_view,pineapple_detail_view,pineapple_create_view,pineapple_update_view,seller_pineapple_list_view)

app_name = "pineapple"

urlpatterns = [
    path('order-list/', views.order_list_view, name='order-list'),
    path('order-detail/<int:pk>', views.order_detail_view, name='order-detail'),
    path('order-create/', views.order_create_view, name='order-create'),
    path('order-update/<int:pk>', views.order_update_view, name='order-update'),

    path("seller-list", views.seller_list_view, name="seller-list"),
    path("seller-detail/<str:certificate_code>", views.seller_detail_view, name="seller-detail"),
    path("seller-create", views.seller_create_view, name="seller-create"),
    path("seller-update/<str:certificate_code>", views.seller_update_view, name="seller-update"),
    path('comment-create/', views.comment_create_view, name='comment-create'),
    path('seller-comment-list/<int:pk>', views.seller_comment_list_view, name='seller-comment-list'),


    path('pineapples/', pineapple_list_view.as_view(), name='pineapple-list'),
    path('pineapples/<int:pk>/', pineapple_detail_view.as_view(), name='pineapple-detail'),
    path('pineapples/create/', pineapple_create_view.as_view(), name='pineapple-create'),
    path('pineapples/<int:pk>/update/', pineapple_update_view.as_view(), name='pineapple-update'),
    path('seller/<int:seller_id>/pineapples/', seller_pineapple_list_view.as_view(), name='seller-pineapple-list'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

 
