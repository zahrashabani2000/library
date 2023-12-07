from django.urls import path,include

from book import views
from borrower import views as borrower_view


urlpatterns = [
    path('login/', borrower_view.BorrowerLogin.as_view(), name='login'),
    path('book_info/', views.BookView.as_view({'get': 'list', 'post': 'create'}), name='book-info'),
    path('book_info/<int:pk>/', views.BookView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='book-CRUD'),
    path('', views.BookList.as_view()),
]
