from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'nome', 'sobrenome', 'phone', 'email','photo']


class MemberSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'nome']