#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. 라이브러리 설치
pip install -r requirements.txt

# 2. 정적 파일 모으기
python manage.py collectstatic --no-input

# 3. DB 마이그레이션
python manage.py migrate

# 4. (추가됨) 슈퍼유저 자동 생성
python create_superuser.py

# 5. (추가됨) 타임라인 데이터 자동 로드
# (데이터가 이미 있으면 덮어씌웁니다. 안전합니다.)
python manage.py loaddata data/timelines.json