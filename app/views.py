from django.shortcuts import render
from .serializers import ListSerializer
from .models import List

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


def index(request):
    return render(request, 'index.html')

@api_view(['GET'])
def listview(request):
    lists = List.objects.all()

    serializer = ListSerializer(lists, many=True)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def listadd(request):
    if request.method == 'POST':
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT']) 
def listupdate(request, id):
    try:
        tasklist = List.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = ListSerializer(data=request.data, instance=tasklist)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
def listdetail(request, id):
    try:
        tasklist = List.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ListSerializer(instance=tasklist)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def listdelete(request, id):
    try:
        tasklist = List.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    tasklist.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
