from rest_framework import serializers
from .models import Skill, Project, Timeline, Post, Guestbook

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'  # 모든 필드를 JSON으로 바꿈!

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class GuestbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guestbook
        fields = '__all__'