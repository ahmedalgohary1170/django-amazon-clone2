from django.urls import path

from .views import ProductDetail,ProductList



urlpatterns = [
    path('',ProductList.as_view()),
    path('detail/<slug:slug>',ProductDetail.as_view()),
]
