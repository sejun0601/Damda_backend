from rest_framework import serializers
from .models import Contact, ImageComponent

class ImageComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageComponent
        fields = ['image', 'diary']

class ContactSerializer(serializers.ModelSerializer):
    images = ImageComponentSerializer(many=True)

    class Meta:
        model = Contact
        fields = ['name', 'phone', 'images']

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        contact = Contact.objects.create(**validated_data)
        for image_data in images_data:
            ImageComponent.objects.create(contact=contact, **image_data)
        return contact