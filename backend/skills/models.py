from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50)  # 기술 이름 (예: Python)
    level = models.CharField(max_length=20) # 수준 (예: Advanced)
    # [수정] JSON 데이터와 맞추기 위해 카테고리 필드 추가 (기본값 Etc)
    category = models.CharField(max_length=50, default='Etc') 

    def __str__(self):
        return self.name

# [삭제됨] Project 모델은 projects 앱으로 이동했으므로 여기서 제거했습니다.

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
    content = models.TextField() 
    tags = models.CharField(max_length=100, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at'] 

    def __str__(self):
        return self.title
    
class Guestbook(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at'] 

    def __str__(self):
        return f"{self.name}: {self.message[:20]}"
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.name}: {self.subject}"