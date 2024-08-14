from .models import *
from rest_framework import serializers

class BankModel(serializers.Serializer):
    class Meta:
        models=BankModel
        fields=["id","bank_name","bank_address"]


class UserModel(serializers.Serializer):
    class Meta:
        models=UserModel
        fields=["id","user_name","user_email","user_contact"]
