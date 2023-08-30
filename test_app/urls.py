from django.urls import path

from test_app.views import OrderListView, UserLoginView, OrderDeleteView, UserLogoutView

urlpatterns = [
    path('', OrderListView.as_view(), name='orders'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('order-dalete/<int:pk>', OrderDeleteView.as_view(), name='order_delete'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
