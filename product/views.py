from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ComputerSerializer,RoomSerializer
from rest_framework import status
from rest_framework.parsers import FileUploadParser,MultiPartParser,FormParser,JSONParser
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.renderers import JSONRenderer
from .exceptions import APIException
from .models import *

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
        qs = Computer.objects.all()
        if qs is None:
            raise APIException()
        else:
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
    
class ComputerDetailView(APIView):
    def get(self, request, pk):
        try:
            computer = Computer.objects.get(id=pk)
            serializer = ComputerSerializer(computer)
            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Computer.DoesNotExist:
            raise APIException(
    message="Computer not found",
    status_code=404,
    code="computer_not_found",
    hint="Check if the computer ID is correct",
    extra={"requested_id": pk}
)

        except Exception as e:
            raise APIException("Something unexpected happened", status_code=500)
