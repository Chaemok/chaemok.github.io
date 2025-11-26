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
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-%uex^@w(%@=mvej!v%6#fko9ryxdz@xttmcdjbd(h3=w+)^q2m')

# 'RENDER' 환경 변수가 설정되어 있지 않으면 DEBUG=True (로컬)
DEBUG = 'RENDER' not in os.environ

# 배포 환경에서만 허용 호스트 설정 (Render의 호스트 이름이 자동으로 포함됨)
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
]

# --- 4. 미들웨어 ---

MIDDLEWARE = [
    # CORS 설정은 보안 설정 바로 다음에 위치해야 합니다.
    'corsheaders.middleware.CorsMiddleware', 
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoise는 정적 파일 관리를 위해 DEBUG=False일 때 필요하며, MIDDLEWARE에 추가되어야 합니다.
    # 하지만 Whitenoise는 STATICFILES_STORAGE 설정을 통해 로드되므로,
    # 여기서는 DEBUG=False일 때 필요한 WhiteNoise 설정을 추가합니다. (이전 build.sh를 위해 필요함)
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
        'DIRS': [], # DIRS는 현재 비워둡니다.
        'APP_DIRS': True, # 이 설정을 통해 Django가 각 앱(skills, admin 등) 폴더의 templates 폴더를 찾습니다.
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

# (템플릿, WSGI 설정은 생략 - 그대로 유지)
WSGI_APPLICATION = 'config.wsgi.application'


# --- 5. 데이터베이스 설정 ---

# Render에 DATABASE_URL 환경 변수가 있다면 PostgreSQL로 자동 연결, 없으면 SQLite 사용
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL', f'sqlite:///{BASE_DIR / "db.sqlite3"}'),
        conn_max_age=600
    )
}


# (비밀번호 유효성, 국제화 설정은 생략 - 그대로 유지)
LANGUAGE_CODE = 'ko-kr' # 한국어로 변경
TIME_ZONE = 'Asia/Seoul' # 시간대 한국으로 변경
USE_I18N = True
USE_TZ = True


# --- 6. 정적 파일 및 미디어 설정 ---

STATIC_URL = '/static/'

# DEBUG=False일 때만 STATIC_ROOT를 설정 (collectstatic을 위해 필요)
if not DEBUG:
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
else:
    # 로컬 개발 환경에서는 'staticfiles'를 사용하지 않음
    STATIC_ROOT = None 
    

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- 7. CORS 설정 (Frontend 통신) ---

if DEBUG:
    # 로컬 개발 시 CORS 모두 허용
    CORS_ALLOW_ALL_ORIGINS = True
else:
    # 배포 시에는 특정 주소만 허용하는 것이 원칙 (Render/Vercel 주소)
    # 현재는 쉬운 배포를 위해 임시로 모두 허용하거나, Vercel 주소만 명시
    # Vercel 주소가 환경변수로 넘어온다고 가정하고 처리하는게 좋습니다.
    # 현재는 *로 설정합니다.
    CORS_ALLOW_ALL_ORIGINS = False
    CORS_ALLOWED_ORIGINS = [
        "https://chaemok-portfolio.vercel.app",  # 👈 본인의 Vercel 최종 주소
        # "https://chaemok.vercel.app",          # (혹시 다른 주소도 쓴다면 추가)
    ]
    
# CSRF 보호 설정 (Admin 로그인 및 데이터 전송을 위해 필요)
# 로컬 주소 + 배포된 주소(Render 백엔드, Vercel 프론트엔드) 모두 등록
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://chaemok.onrender.com",  # Render 백엔드 주소
    "https://chaemok-portfolio.vercel.app",  # Vercel 프론트엔드 주소
]