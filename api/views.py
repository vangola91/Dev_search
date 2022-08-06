from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project



@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET':'/api/projects'},
        {'GET':'/api/projects/id'},
        {'GET':'/api/projects/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},

    ]
    return Response(routes)

@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    seriailizer = ProjectSerializer(projects, many=True)
    return Response(seriailizer.data)\


@api_view(['GET'])
def getProject(request, pk):
    project = Project.objects.get(id=pk)
    seriailizer = ProjectSerializer(project, many=False)
    return Response(seriailizer.data)