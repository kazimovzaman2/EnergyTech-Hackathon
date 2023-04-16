from rest_framework import serializers
from .models import User, Data, DataDate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'abonet_code', )


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'


class DataDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataDate
        fields = '__all__'
