from django.urls import path, include
from rest_framework.routers import DefaultRouter

from loan import views
from borrower import views as borrower_view

urlpatterns = [
    # Other URL patterns
    path('login/', borrower_view.BorrowerLogin.as_view(), name='login'),
    path('book-instances/', views.BookInstanceViewSet.as_view({'get': 'list', 'post': 'create'}), name='bookinstance-list-create'),
    path('book-instances/<uuid:pk>/', views.BookInstanceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='bookinstance-detail'),
]