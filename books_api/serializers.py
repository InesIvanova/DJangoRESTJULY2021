from rest_framework import serializers
from .models import BookModel
from rest_framework.permissions import IsAuthenticated


class BookSerializer(serializers.ModelSerializer):
    def validate(self, data):
        self.validate_title(data["title"])
        return data

    def validate_title(self, title):
        if title:
            if not title[0].isupper():
                raise serializers.ValidationError("Title must start with capital")
        return title

    class Meta:
        model = BookModel
        fields = "__all__"
