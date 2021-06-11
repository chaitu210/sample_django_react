from django.shortcuts import render
from rest_framework import viewsets
from react.render import render_component
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.views import APIView
from .renderers import *
from .serializers import BookSerializer
from .models import Book
from rest_framework import permissions
from rest_framework.response import Response

# Create your views here.


class BookView(APIView):
    renderer_classes = (ReactTemplateHTMLRenderer, JSONRenderer)
    http_allowed_methods = ('GET', )
    template_name = 'home.html'
    component_path = 'assets/js/app.jsx'
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = (permissions.AllowAny,)


    def get(self, request, *args, **kwargs):
        """
        Return a list of all users.
        """
        serializer = BookSerializer(Book.objects.all(), many=True)
        return Response(serializer.data)


class BooksOverview(APIView):
    renderer_classes = (ReactTemplateHTMLRenderer, JSONRenderer)
    http_allowed_methods = ('GET', )
    template_name = 'charts.html'
    component_path = 'assets/js/charts.jsx'
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = (permissions.AllowAny,)


    def get(self, request, *args, **kwargs):
        """
        Return a list of all users.
        """
        result = []
        genres = list(set(Book.objects.all().values_list('genre', flat=True)))
        for each in genres:
            result.append(Book.objects.filter(genre=each).count())

        return Response({'genre': genres, 'values': result})
