from rest_framework.serializers import ModelSerializer

from payments.models import Item


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price']