from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ComputerSerializer,RoomSerializer
from rest_framework import status
from rest_framework.parsers import FileUploadParser,MultiPartParser,FormParser,JSONParser
from .models import computer,Rooms
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.renderers import JSONRenderer
# Create your views here.

class ComputerView(APIView):
    parser_classes = [MultiPartParser,FormParser]
    renderer_classes = [JSONRenderer]
    def post(self,request):
        serializer = ComputerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors)
    
    def get(self,request):
        qs = computer.objects.all()
        serializer = ComputerSerializer(qs,many = True)
        return Response(serializer.data)

@api_view(['POST','GET'])
@renderer_classes([JSONRenderer])
def addNewRooms(request):
    if request.method == 'POST':
        if isinstance(request.data,list):
            serializer = RoomSerializer(data=request.data,many=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors)
        elif isinstance(request.data,dict):
            serializer = RoomSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
             qs = Rooms.objects.all()
             serialializer = RoomSerializer(qs,many=True)
             return Response(serialializer.data)
    
    
