from rest_framework import viewsets
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import BookInstance
from loan import loan_serializer


class BookInstanceViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    """after login user can borrow books in book-instances and see book detail using uuid of book"""

    login_url = 'login'
    redirect_field_name = 'book-instances'

    serializer_class = loan_serializer.LoanSerializer
    queryset = BookInstance.objects.all()
    

