from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


app_name = "pineapple"

urlpatterns = [
    path('order-list/', views.order_list_view, name='order-list'),
    path('order-detail/<int:pk>', views.order_detail_view, name='order-detail'),
    path('order-create/', views.order_create_view, name='order-create'),
    path('order-update/<int:pk>', views.order_update_view, name='order-update'),
    path('comment-create/', views.comment_create_view, name='comment-create'),
    path('seller-comment-list/<int:pk>', views.seller_comment_list_view, name='seller-comment-list'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

 
