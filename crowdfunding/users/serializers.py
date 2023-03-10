from rest_framework import serializers
from .models import CustomUser
from datetime import datetime
# from dateutil.relativedelta import relativedelta, MO

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length = 200)
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)
    image = serializers.URLField()
    bio = serializers.CharField(max_length=300)
    # date_of_birthday = serializers.DateField()
    # def validate_date_of_birthday(self, validated_data):
    #     age = relativedelta(datetime.now(), date_of_birthday).years
    #     if age < 18:
    #         raise serializers.ValidationError('Unfortunately you must be at least 18 years old to register :(')
    #     return CustomUser.objects.create_user(**validated_data)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

 
    
