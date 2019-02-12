from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )
from .models import Trangle

# class SnippetSerializer(ModelSerializer):
#     class Meta:
#         model = Trangle
#         fields = ['id','url', 'a', 'b',
#                  'c', 'output', ]

class SnippetSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='comments-api:thread')
    class Meta:
        model = Trangle
        fields = [
            'url',
            'id',
            'a',
            'b',
            'c',
            'output',
            
        ]
    
    