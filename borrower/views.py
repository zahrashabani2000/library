from rest_framework import viewsets
from rest_framework import filters 
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from borrower import models
from borrower import borrower_serializer
from borrower import permissions


class BorrowerSignUp(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.UpdateOwnProfile,]
    serializer_class = borrower_serializer.BorrowerSerializer
    queryset = models.Borrower.objects.all()

    def list(self, request, *args, **kwargs):
        return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    


class BorrowerLogin(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class BorrowerProfileFeed(viewsets.ModelViewSet):
    """Handle creating, reading and updatin profile feed items"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = borrower_serializer.BorrowerFeedItemSerializer
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        self.queryset = models.BorrowerFeedItem.objects.filter(borrower_info=query)
        return self.queryset

    def perform_create(self, serializer):
        """sets the user profile to the logged in user"""
        serializer.save(borrower_info=self.request.user)
    
         