from rest_framework import serializers
import requests
from .models import User, ReportedURL


class URLSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=255)
    confirmed = serializers.BooleanField(default=False)

    def validate_url(self, value):
        try:
            requests.get(value, timeout=5)
        except Exception as e:
            raise serializers.ValidationError("Invalid url")
        return value
    

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'name', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
            'name': {
                'write_only': True,
            }
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class ReportedURLSSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportedURL
        fields =  ['url', 'user', 'reported_date', 'email', 'username', "confirmed"]
        extra_kwargs = {
            'user': {'write_only': True}
        }

    def get_email(self, obj):
        return obj.user.email
    
    def get_username(self, obj):
        return obj.user.username


    
