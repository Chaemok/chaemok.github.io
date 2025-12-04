"""
Django settings for config project.
"""

from pathlib import Path
import os
import dj_database_url
from django.core.exceptions import ImproperlyConfigured

# --- 1. 경로 설정 ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- 2. 보안 및 환경 인지 ---

# Render 환경에서 'SECRET_KEY' 환경 변수를 가져오고, 없으면 로컬 기본값을 사용
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-default-key-for-dev')

# 'RENDER' 환경 변수가 설정되어 있지 않으면 DEBUG=True (로컬)로 동작
DEBUG = 'RENDER' not in os.environ

# 허용 호스트 설정 (Render 환경변수가 없으면 '*'로 모든 접속 허용)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')


# --- 3. 앱 정의 ---

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # 3rd Party Apps
    'rest_framework',
    'corsheaders',
    
    # My Apps
    'skills',
    'projects', 
]

# --- 4. 미들웨어 ---

MIDDLEWARE = [
    # CORS 미들웨어는 가능한 최상단에 위치
    'corsheaders.middleware.CorsMiddleware', 
    'django.middleware.security.SecurityMiddleware',
    
    # WhiteNoise: 정적 파일 서빙 (SecurityMiddleware 바로 다음 권장)
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# --- 5. 데이터베이스 설정 ---

# Render: DATABASE_URL 환경변수가 있으면 PostgreSQL 사용, 없으면 로컬 SQLite 사용
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL', f'sqlite:///{BASE_DIR / "db.sqlite3"}'),
        conn_max_age=600
    )
}


# --- 6. 언어 및 시간 설정 ---

LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_TZ = True


# --- 7. 정적 파일 설정 (WhiteNoise) ---

STATIC_URL = '/static/'

# 배포 환경(DEBUG=False)에서는 staticfiles 폴더에 모으고 WhiteNoise가 서빙
if not DEBUG:
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
else:
    STATIC_ROOT = None 
    

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- 8. CORS 및 CSRF 설정 (수정됨) ---

# [수정 1] CORS: 배포 초기 에러 방지를 위해 개발/배포 모두 '전체 허용'으로 설정
# 나중에 프론트엔드 도메인이 확정되면 그때 False로 바꾸고 구체적으로 적어주는 게 좋습니다.
CORS_ALLOW_ALL_ORIGINS = True

# [수정 2] CSRF: Render와 Vercel 도메인에서의 요청을 신뢰하도록 설정
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://*.onrender.com",     # Render의 모든 서브도메인 허용
    "https://*.vercel.app",       # Vercel의 모든 서브도메인 허용
]