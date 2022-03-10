from django.urls import path

from eshop import views


urlpatterns = [
    path('list/', views.ProductListView.as_view(), name="list_view"),
    path('detail/<int:pk>/', views.ProductDetailView.as_view()),
    path('create/', views.ProductCreateView.as_view(), name="create_view"),
    path('update/<int:pk>/', views.ProductUpdateView.as_view()),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view()),
]