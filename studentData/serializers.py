from random import random
from rest_framework import serializers
from .models import Certificate

class certificateSerializer(serializers.ModelSerializer):
    # def generate_unique_code():
    #     length = 7
    #     code = ''.join(random.choices(string.digits, k=length))
    #     return code
    # randomField = serializers.SerializerMethodField("generate_unique_code")
    class Meta:
        model = Certificate
        fields = '__all__'

    