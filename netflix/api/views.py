from rest_framework.response import Response
from netflix.models import Movies
from .serializers import MovieSerializers, UserSerializers
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
@api_view(['POST'])
def api_signup(request):
    serializer = UserSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success":True,
            "message":"User Is Created By Successfuly"
        },status=status.HTTP_201_CREATED)
    return Response(data={
        "success":False,
        "errors":serializer.errors
    },status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def index(request):
    movies = Movies.objects.all()
    serializes = MovieSerializers(instance=movies,many=True)
    return Response(data=serializes.data,status=status.HTTP_200_OK)
@api_view(['POST'])
def create(request):
    serializer = MovieSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success":True,
            "message":"Movie Is Created By Successfuly"
        },status=status.HTTP_201_CREATED)
    return Response(data={
        "success":False,
        "errors":serializer.errors
    },status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated,])
class MovieUpdate(generics.ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializers