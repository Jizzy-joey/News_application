from rest_framework import serializers
from .models import News


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        read_only_fields = ("author")