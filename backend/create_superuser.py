import os
import django

# Django 환경 설정 불러오기
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
USERNAME = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin') # 기본값 admin
EMAIL = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
PASSWORD = os.environ.get('DJANGO_SUPERUSER_PASSWORD', '1234') # 기본값 1234

def create_superuser():
    if not User.objects.filter(username=USERNAME).exists():
        print(f"Creating superuser: {USERNAME}")
        User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
        print("Superuser created successfully!")
    else:
        print("Superuser already exists.")

if __name__ == "__main__":
    create_superuser()