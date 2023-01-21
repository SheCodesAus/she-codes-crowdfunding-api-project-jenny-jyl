from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge, Favorite
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer, DeleteProjectSerializer
from django.http import Http404
from rest_framework import status, generics, permissions
from .permissions import IsOwnerOrReadOnly

class ProjectList(APIView):
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    # built in function IsAuthenticatedOrReadOnly which we can use
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)
    
    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance=project,
            data = data,
            partial=True
        )
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class PledgeList(generics.ListCreateAPIView):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer

    def perform_create(self, serializer):
        serializer.save(supporter=self.request.user)

class DeleteProject(APIView):
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    
    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404



# class FavoriteList(APIView):
#     queryset = Favorite.objects.all()
#     serializer_class = FavoriteSerializer

#     def get(self, request):
#         user = request.user
#         queryset = self.queryset.filter(user=user)
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)







    # def get(self, request):
    #     pledges = Pledge.objects.all()
    #     serializer = PledgeSerializer(pledges, many=True)
    #     return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = PledgeSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(
    #             serializer.data,
    #             status=status.HTTP_201_CREATED
    #         )
    #     return Response(
    #         serializer.errors,
    #         status=status.HTTP_400_BAD_REQUEST
    #     )
       
        
