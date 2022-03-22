from rest_framework import serializers
from UseApp.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userId',
                  'userName',
                  'password')