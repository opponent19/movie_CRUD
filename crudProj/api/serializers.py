from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = ['name', 'img', 'summary']
        fields = '__all__'