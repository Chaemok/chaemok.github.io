from django.contrib import admin
from .models import Skill, Project, Timeline, Post, Guestbook

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Timeline)
admin.site.register(Post)
admin.site.register(Guestbook)