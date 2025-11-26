from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50)  # 기술 이름 (예: Python)
    level = models.CharField(max_length=20) # 수준 (예: Advanced)

    def __str__(self):
        return self.name  # 관리자 페이지에서 이름으로 보이게 함


class Project(models.Model):
    title = models.CharField(max_length=100)      # 프로젝트 제목
    description = models.TextField()              # 상세 설명 (긴 글)
    image_url = models.URLField(blank=True)       # 이미지 주소 (일단 URL로 처리)
    github_url = models.URLField(blank=True)      # 깃허브 링크
    
    def __str__(self):
        return self.title
    

class Timeline(models.Model):
    start_date = models.CharField(max_length=20) # 예: "2024.07"
    end_date = models.CharField(max_length=20, blank=True, null=True) # 예: "현재"
    title = models.CharField(max_length=100)     # 예: "SSAFY 14기"
    description = models.TextField(blank=True)   # 설명
    
    # 최신순 정렬을 위한 진짜 날짜 필드 (화면엔 안 보임)
    order_date = models.DateField()

    class Meta:
        ordering = ['-order_date'] # 최신 날짜가 위로 오게 정렬

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    # 긴 글을 저장하기 위해 TextField 사용
    content = models.TextField() 
    # 포스트를 구분할 태그 (예: Python, Django, Vue)
    tags = models.CharField(max_length=100, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at'] # 최신 글이 위에 오도록 정렬

    def __str__(self):
        return self.title
    
    
class Guestbook(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at'] # 최신 글이 위로

    def __str__(self):
        return f"{self.name}: {self.message[:20]}"