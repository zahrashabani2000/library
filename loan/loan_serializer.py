from rest_framework import serializers
import datetime
from django.core.exceptions import ValidationError


from loan import models

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BookInstance
        fields = '__all__'


class RenewBokkSerializer(serializers.Serializer):
    renewal_data = serializers.DateField()

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_data']
        
        if data < datetime.date.today():
            raise ValidationError('Invalid date - renewal in past')
        
        if data> datetime.date.today() + datetime.timedelta(weeks=2):
            raise ValidationError('invalid date - renewal more then 2 weeks ahead')
       
        return data