from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from books_api.restrictions import IsFullAdmin
from .models import BookModel
from .serializers import BookSerializer


class BookListCreate(ListAPIView):
    permission_classes = [IsAuthenticated, IsFullAdmin]
    def get(self, request):
        books = BookModel.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


    def post(self, request):
        book_serializer = BookSerializer(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)
        return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    def put(self, request, book_id):
        book = get_object_or_404(BookModel, pk=book_id)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


    def get(self, request, book_id):
        try:
            book = BookModel.objects.get(id=book_id)
            book_serializer = BookSerializer(book)
            return Response(book_serializer.data)
        except:
            return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, book_id):
        try:
            book = BookModel.objects.get(id=book_id)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)



