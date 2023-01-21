from rest_framework import serializers
from .models import CustomUser
from datetime import datetime
from dateutil.relativedelta import relativedelta, MO

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length = 200)
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)
    date_of_birthday = serializers.DateField()

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    def validate_date_of_birthday(self, date_of_birthday):
        age = relativedelta(datetime.now(), date_of_birthday).years

        if age < 18:
            raise serializers.ValidationError('Unfortunately you must be at least 18 years old to register :(')
        else:
            return date_of_birthday
    
