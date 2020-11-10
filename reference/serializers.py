from rest_framework.serializers import ModelSerializer
from .models import Trabalhos


class TrabalhosSerializer(ModelSerializer):
    class Meta:
        model = Trabalhos

        fields = ['nome', 'data_criacao', 'referencias']