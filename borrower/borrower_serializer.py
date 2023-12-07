from rest_framework import serializers

from borrower import models

class BorrowerSerializer(serializers.ModelSerializer):
    """This serializer handles registration of borrower(sign up)"""

    class Meta:
        model = models.Borrower
        fields = ['id', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password':{
            'write_only':True,
            'style':{'input_type':'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new borrower"""

        user = models.Borrower.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )

        return user


class BorrowerFeedItemSerializer(serializers.ModelSerializer):
    """after login this serializer can be call and handles feed item of borrower"""

    class Meta:
        model = models.BorrowerFeedItem
        fields = ('id', 'borrower_info', 'membership_type', 'registery_date')
        extra_kwargs = {'borrower_info': {'read_only':True}}
