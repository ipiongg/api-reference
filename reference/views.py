from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Trabalhos
from .serializers import TrabalhosSerializer
from rest_framework import permissions


class TrabalhosList(ListCreateAPIView):

    serializer_class = TrabalhosSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Trabalhos.objects.filter(owner=self.request.user)


class TrabalhosDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = TrabalhosSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Trabalhos.objects.filter(owner=self.request.user)
