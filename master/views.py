from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import tasksSerializers
from .models import task

@api_view(['GET', 'POST'])
def tasksListAPI(request):
    if request.method == 'GET':
        querySet = task.objects.all()
        serializer = tasksSerializers(querySet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = tasksSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def taskDetailAPI(request, task_id):

    try:
        querySet = task.objects.get(id=task_id)
    except task.DoesNotExist:
        return Response({'message': "Data Not Found"},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = tasksSerializers(querySet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = tasksSerializers(querySet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        serializer = tasksSerializers(querySet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        querySet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
