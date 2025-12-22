from rest_framework import serializers
from .models import Profissional, Consulta


class ProfissionalSerializer(serializers.ModelSerializer):

    class Meta():
        model = Profissional
        fields = '__all__'

    def validate_nome(self, value):
        if not all(x.isalpha() or x.isspace() for x in value):
            raise serializers.ValidationError(
                'Nome deve ter'
                'apenas letras e espaços'
            )
        return value.title()

    def validate_profissao(self, value):
        if not all(x.isalpha() or x.isspace() for x in value):
            raise serializers.ValidationError(
                'Nome deve ter'
                'apenas letras e espaços'
            )
        return value.title()

    def validate_contato(self, value):
        if Profissional.objects.filter(contato=value).exists():
            raise serializers.ValidationError('Email já registrado')
        return value.title()


class ConsultaSerializer(serializers.ModelSerializer):

    class Meta():
        model = Consulta
        fields = '__all__'

    def validate_name(self, value):
        if not all(x.isalpha() or x.isspace() for x in value):
            raise serializers.ValidationError(
                'Nome deve ter'
                'apenas letras e espaços'
            )
        return value.title()
