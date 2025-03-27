from rest_framework.serializers import ModelSerializer
from .models import Computer,Rooms
from rest_framework import serializers


class ComputerSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(write_only=True)
    image = serializers.SerializerMethodField()
    video = serializers.FileField(write_only=True, required=False)
    document = serializers.FileField(write_only=True, required=False)
    id = serializers.ReadOnlyField()
    video_url = serializers.SerializerMethodField()
    document_url = serializers.SerializerMethodField()

    

    class Meta:
        model = Computer
        fields = ['id','name', 'avatar', 'video', 'document', 'image', 'video_url', 'document_url', 'description']

    def get_image(self, obj):
        return obj.avatar.url if obj.avatar else None

    def get_video_url(self, obj):
        return obj.video.url if obj.video else None

    def get_document_url(self, obj):
        return obj.document.url if obj.document else None
    

class RoomSerializer(ModelSerializer):
    updated_at = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()
    class Meta:
        model= Rooms
        fields = ['name','description','updated_at','created_at']