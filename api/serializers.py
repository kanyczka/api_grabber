from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UrlText


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class UrlTextSerializer(serializers.ModelSerializer):

    class Meta:
        model = UrlText
        fields = ('id', 'url_path', 'text', 'upload_date')
        read_only_fields = ('url', 'text', 'upload_date')



