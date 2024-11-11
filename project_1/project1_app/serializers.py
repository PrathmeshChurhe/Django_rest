from rest_framework import serializers
from .models import Data, Contact, Newsletter

class dataSer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'

class dataContact(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class datanews(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'