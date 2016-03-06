from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from models import Book, BookCase
from serializers import BookSerializer 
from utils.views import CreateRetrieveAPIView


class BookDetail(CreateRetrieveAPIView):
    """
    API endpoint for Book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookList(APIView):
    """
    List all books or creates a new one
    """
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
