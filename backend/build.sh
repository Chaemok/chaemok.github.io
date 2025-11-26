#!/usr/bin/env bash
# 에러 나면 즉시 멈춰라
set -o errexit

# 1. 라이브러리 설치
pip install -r requirements.txt

# 2. 정적 파일(CSS, JS) 모으기
python manage.py collectstatic --no-input

# 3. DB 마이그레이션 (중요!)
python manage.py migrate