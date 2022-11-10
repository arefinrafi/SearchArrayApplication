from django.contrib.auth.models import User
from .models import Khojsearch
from rest_framework import serializers

class KhojsearchSerializer(serializers.ModelSerializer):
    inputlist = serializers.ListField(child = serializers.IntegerField())
    
    def to_internal_value(self, data):
        data['inputlist'] = data['inputlist'].split(',') if data['inputlist'] else []
        return data

    class Meta:
        model = Khojsearch
        fields = ['timestamp', 'inputlist'] 
      

# class KhojsearchSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Khojsearch
#         fields = ['timestamp', 'inputlist'] 

class UserSerializer(serializers.ModelSerializer):
    payload = KhojsearchSerializer(many=True)
    class Meta:
        model = User
        fields = ['id','payload']

