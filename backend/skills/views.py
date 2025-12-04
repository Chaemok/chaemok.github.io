# backend/skills/views.py
import os
import requests
from dotenv import load_dotenv
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework import status
# ⚠️ 중요: Contact 모델 import 확인
from .models import Skill, Timeline, Post, Guestbook, Contact
# ⚠️ 중요: ContactSerializer import 확인
from .serializers import SkillSerializer, TimelineSerializer, PostSerializer, GuestbookSerializer, ContactSerializer

load_dotenv()
# 1. 관리자만 수정 가능 (Skills, Projects, Timelines, Posts)
# ----------------------------------------------------------------

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def skill_list(request):
    if request.method == 'GET':
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def skill_detail(request, pk):
    try:
        skill = Skill.objects.get(pk=pk)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Skill.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def timeline_list(request):
    timelines = Timeline.objects.all()
    serializer = TimelineSerializer(timelines, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

# 2. 누구나 쓰기 가능 (Guestbook, Contact)
# ----------------------------------------------------------------

@api_view(['GET', 'POST'])
@permission_classes([AllowAny]) # 누구나 가능
def guestbook_list(request):
    if request.method == 'GET':
        guestbooks = Guestbook.objects.all()
        serializer = GuestbookSerializer(guestbooks, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = GuestbookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_discord_alert(name, email, subject, message):
    # ⚠️ 수정됨: 직접 적는 대신 os.environ.get으로 꺼내오기
    WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

    # URL이 없으면(설정 안 했으면) 그냥 전송 안 하고 끝내기 (에러 방지)
    if not WEBHOOK_URL:
        print("디스코드 웹훅 URL이 설정되지 않았습니다.")
        return

    content = f"📢 **포트폴리오 연락 도착!**\n\n👤 **이름:** {name}\n📧 **메일:** {email}\n📝 **제목:** {subject}\n💬 **내용:** {message}"
    
    data = {"content": content}
    
    try:
        requests.post(WEBHOOK_URL, json=data)
    except Exception as e:
        print(f"디스코드 전송 실패: {e}")

@api_view(['POST'])
@permission_classes([AllowAny])
def contact_create(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save() # 1. DB에 저장
        
        # 2. 디스코드 알림 발송! (비동기로 처리하면 더 좋지만 일단 단순하게)
        data = serializer.validated_data
        send_discord_alert(
            data.get('name'), 
            data.get('email'), 
            data.get('subject'), 
            data.get('message')
        )
        
        return Response({"message": "메시지가 전송되었습니다!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status  # 상태 코드(201 Created 등) 쓰려고 추가
# from .models import Skill, Project, Timeline, Post, Guestbook
# from .serializers import SkillSerializer, ProjectSerializer, TimelineSerializer, PostSerializer, GuestbookSerializer

# # GET(조회)뿐만 아니라 POST(생성)도 허용한다고 명시!
# @api_view(['GET', 'POST'])
# def skill_list(request):
#     # 1. 조회 (GET): 기존과 동일
#     if request.method == 'GET':
#         skills = Skill.objects.all()
#         serializer = SkillSerializer(skills, many=True)
#         return Response(serializer.data)

#     # 2. 생성 (POST): 새로 추가된 부분!
#     elif request.method == 'POST':
#         # 사용자가 보낸 데이터(request.data)를 번역기(Serializer)에 넣음
#         serializer = SkillSerializer(data=request.data)
        
#         # 데이터가 올바른지 검사 (빈칸은 없는지, 길이가 너무 길지 않은지)
#         if serializer.is_valid():
#             serializer.save()  # DB에 저장!
#             # 성공했다는 신호(201)와 저장된 데이터를 돌려줌
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         # 이상한 데이터면 에러 메시지 보냄
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # (기존 skill_list 함수 밑에 추가)

# @api_view(['DELETE'])
# def skill_detail(request, pk):
#     try:
#         # 1. DB에서 pk(ID)에 해당하는 스킬을 찾는다.
#         skill = Skill.objects.get(pk=pk)
        
#         # 2. 찾았으면 지운다.
#         skill.delete()
        
#         # 3. 잘 지웠다고 신호(204 No Content)를 보낸다.
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     except Skill.DoesNotExist:
#         # 없으면 404 에러 보낸다.
#         return Response(status=status.HTTP_404_NOT_FOUND)

# @api_view(['GET'])
# def project_list(request):
#     projects = Project.objects.all()
#     serializer = ProjectSerializer(projects, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def project_detail(request, pk):
#     try:
#         project = Project.objects.get(pk=pk)
#         serializer = ProjectSerializer(project)
#         return Response(serializer.data)
#     except Project.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
# @api_view(['GET'])
# def timeline_list(request):
#     timelines = Timeline.objects.all()
#     serializer = TimelineSerializer(timelines, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def post_list(request):
#     posts = Post.objects.all()
#     serializer = PostSerializer(posts, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def post_detail(request, pk):
#     try:
#         post = Post.objects.get(pk=pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     except Post.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    

# @api_view(['GET', 'POST'])
# def guestbook_list(request):
#     if request.method == 'GET':
#         guestbooks = Guestbook.objects.all()
#         serializer = GuestbookSerializer(guestbooks, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = GuestbookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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