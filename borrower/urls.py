from django.urls import path,include
from rest_framework.routers import DefaultRouter

from borrower import views

router = DefaultRouter()
router.register('borrowerSignUp', views.BorrowerSignUp) 
# // if i register this class it will show all borrower info 
router.register('feed', views.BorrowerProfileFeed, basename='borrower_feedItem')

urlpatterns = [
        path('', include(router.urls)),
]
