from rest_framework import serializers
from .models import Skill, Timeline, Post, Guestbook,Contact

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'  # 모든 필드를 JSON으로 바꿈!

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


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'