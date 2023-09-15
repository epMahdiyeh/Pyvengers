from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

app_name = "pineapple"

urlpatterns = [
    path('subscription-create/', views.subscription_create_view, name='subscription-create'),
    path('subscription-list/', views.subscription_list_view, name='subscription-list'),

    path('order-list/', views.order_list_view, name='order-list'),
    path('order-detail/<int:pk>', views.order_detail_view, name='order-detail'),
    path('order-create/', views.order_create_view, name='order-create'),
    path('order-update/<int:pk>', views.order_update_view, name='order-update'),

    path("seller-list", views.seller_list_view, name="seller-list"),
    path("seller-detail/<str:certificate_code>", views.seller_detail_view, name="seller-detail"),
    path("seller-create", views.seller_create_view, name="seller-create"),
    path("seller-update/<str:certificate_code>", views.seller_update_view, name="seller-update"),

    path('comment-create/', views.comment_create_view, name='comment-create'),
    path('seller-comment-list/<str:certificate_code>/', views.seller_comment_list_view, name='seller-comment-list'),

    path('pineapples/', views.pineapple_list_view, name='pineapple-list'),
    path('pineapples/<int:pk>/', views.pineapple_detail_view, name='pineapple-detail'),
    path('pineapples/create/', views.pineapple_create_view, name='pineapple-create'),
    path('pineapples/<int:pk>/update/', views.pineapple_update_view, name='pineapple-update'),
    path('seller/<int:seller_id>/pineapples/', views.seller_pineapple_list_view, name='seller-pineapple-list'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
