from rest_framework import serializers
from .models import SMS



class SMS_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SMS
        fields = ['body']