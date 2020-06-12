from django.shortcuts import render
from .models import Posts
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostsSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@api_view(['GET'])
def posts(request):
    posts=Posts.objects.all()
    if len(posts)!=0:
        serializer=PostsSerializer(posts,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['POST'])
def add_post(request):
    serializer=PostsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['GET'])
def get_post_by_id(request,pk):
    post=Posts.objects.filter(id=pk).first()
    serializer=PostsSerializer(post,many=False)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_posts_for_user(request,artist_id):
    post=Posts.objects.filter(artist_id=artist_id)
    serializer=PostsSerializer(post,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_post(request, pk):
    post=Posts.objects.filter(id=pk)
    post.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def update_post(request, pk):
    post=Posts.objects.filter(id=pk).first()
    serializer=PostsSerializer(instance=post,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

