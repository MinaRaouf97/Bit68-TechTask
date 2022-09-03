from rest_framework import serializers
from .models import User
import django.contrib.auth.password_validation as validators
import sys
from django.core import exceptions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name','email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):

        if self.partial != True:
            user = User(**data)
            password = data.get('password')
            errors = dict() 
            try:
                # validate the password and catch the exception
                validators.validate_password(password=password, user=user)
            except exceptions.ValidationError as e:
                errors['password'] = list(e.messages)
            if errors:
                raise serializers.ValidationError(errors)
        return super(UserSerializer, self).validate(data)
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance