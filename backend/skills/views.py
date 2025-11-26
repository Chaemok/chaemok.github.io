from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status  # 상태 코드(201 Created 등) 쓰려고 추가
from .models import Skill, Project, Timeline
from .serializers import SkillSerializer, ProjectSerializer, TimelineSerializer

# GET(조회)뿐만 아니라 POST(생성)도 허용한다고 명시!
@api_view(['GET', 'POST'])
def skill_list(request):
    # 1. 조회 (GET): 기존과 동일
    if request.method == 'GET':
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    # 2. 생성 (POST): 새로 추가된 부분!
    elif request.method == 'POST':
        # 사용자가 보낸 데이터(request.data)를 번역기(Serializer)에 넣음
        serializer = SkillSerializer(data=request.data)
        
        # 데이터가 올바른지 검사 (빈칸은 없는지, 길이가 너무 길지 않은지)
        if serializer.is_valid():
            serializer.save()  # DB에 저장!
            # 성공했다는 신호(201)와 저장된 데이터를 돌려줌
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # 이상한 데이터면 에러 메시지 보냄
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# (기존 skill_list 함수 밑에 추가)

@api_view(['DELETE'])
def skill_detail(request, pk):
    try:
        # 1. DB에서 pk(ID)에 해당하는 스킬을 찾는다.
        skill = Skill.objects.get(pk=pk)
        
        # 2. 찾았으면 지운다.
        skill.delete()
        
        # 3. 잘 지웠다고 신호(204 No Content)를 보낸다.
        return Response(status=status.HTTP_204_NO_CONTENT)

    except Skill.DoesNotExist:
        # 없으면 404 에러 보낸다.
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def project_list(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def timeline_list(request):
    timelines = Timeline.objects.all()
    serializer = TimelineSerializer(timelines, many=True)
    return Response(serializer.data)


# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Skill
# from .serializers import SkillSerializer

# @api_view(['GET'])
# def skill_list(request):
#     # 1. DB에서 모든 기술 데이터 가져오기 (QuerySet)
#     skills = Skill.objects.all()
    
#     # 2. JSON으로 번역하기 (many=True는 '여러 개'라는 뜻)
#     serializer = SkillSerializer(skills, many=True)
    
#     # 3. 번역된 데이터(serializer.data) 보내주기
#     return Response(serializer.data)



# # @api_view(['GET'])
# def skill_list(request):
#     # 나중에는 DB에서 가져올 데이터입니다.
#     data = [
#         {'id': 1, 'name': 'Python', 'level': 'Advanced'},
#         {'id': 2, 'name': 'Django', 'level': 'Intermediate'},
#         {'id': 3, 'name': 'Vue.js', 'level': 'Beginner'},
#     ]
#     return Response(data)