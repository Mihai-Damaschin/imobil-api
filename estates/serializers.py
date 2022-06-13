from rest_framework import serializers

from common.serializers import MediaSerializer
from accounts.serializers import UserSerializer
from .models import Estate


class EstateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = '__all__'


class EstateSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    media = MediaSerializer(many=True)

    class Meta:
        model = Estate
        fields = '__all__'
