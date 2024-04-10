


from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer


class MovieList(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                movie = Movie.objects.get(pk=pk)
                serializer = MovieSerializer(movie)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Movie.DoesNotExist:
                return Response({"message": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({"message": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Movie updated successfully.", "data": serializer.data},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({"message": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response({"message": "Movie deleted successfully."}, status=status.HTTP_204_NO_CONTENT)



