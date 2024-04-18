# from rest_framework import serializers
# from .models import Movie

# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         # fields = ['name', 'img', 'summary']
#         fields = '__all__'

from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'img', 'summary']
        extra_kwargs = {
            'img': {'required': False},
            'summary': {'required': False},
            'name': {'required': False}
        }

    def validate(self, data):
        if not any([data.get('name'), data.get('img'), data.get('summary')]):
            raise serializers.ValidationError("At least one of 'name', 'img', or 'summary' is required.")
        return data