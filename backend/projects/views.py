from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer

# 1. 프로젝트 전체 목록 조회
@api_view(['GET'])
def project_list(request):
    projects = Project.objects.all().order_by('-created_at') # 최신순 정렬
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

# 2. 프로젝트 상세 조회 (ID로 하나만 가져오기)
@api_view(['GET'])
def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)