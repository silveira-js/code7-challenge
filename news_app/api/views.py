from django.shortcuts import render
import rest_framework
from .models import Author, News
from .serializers import AuthorSerializer, NewsSerializer
from rest_framework import viewsets
from django.db.models import Q
# Create your views here.

class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    
    def get_queryset(self):
        parameter = self.request.GET.get("q", "")

        if parameter:
            list_of_authors = []
            authors = Author.objects.filter(Q(first_name__icontains=parameter) | Q(last_name__icontains=parameter))
            for author in authors:
                list_of_authors.append(author.id)
            return News.objects.filter(Q(title__icontains=parameter) | Q(text__icontains=parameter) | Q(author__in = list_of_authors))
        return super().get_queryset()
