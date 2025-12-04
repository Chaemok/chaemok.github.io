<script setup>
const API_URL = import.meta.env.VITE_API_URL
import { ref, onMounted } from 'vue'

const projects = ref([])
const isLoading = ref(true)

// 이미지 경로 처리 함수 (필요 시 수정)
const getImageUrl = (url) => {
  if (!url) return null;
  // 만약 URL이 http로 시작하면 그대로 쓰고, 아니면 API_URL을 붙여줌
  if (url.startsWith('http')) return url;
  return `${API_URL}${url}`;
}

onMounted(async () => {
  try {
    const res = await fetch(`${API_URL}/api/projects/`)
    if (res.ok) {
      projects.value = await res.json()
    }
  } catch (err) {
    console.error("프로젝트 로딩 실패:", err)
  } finally {
    isLoading.value = false
  }
})
</script>

<template>
  <div class="project-page">
    
    <section class="page-header">
      <div class="container">
        <span class="badge">Portfolio</span>
        <h2 class="page-title">Projects</h2>
        <p class="page-desc">
          문제를 해결하며 성장했던 기록들입니다.<br>
          Django와 Vue.js를 활용한 주요 프로젝트를 소개합니다.
        </p>
      </div>
    </section>

    <section class="project-list-section">
      <div class="container">
        
        <div v-if="isLoading" class="loading-state">
          <div class="spinner"></div>
        </div>
        
        <div v-else-if="projects.length === 0" class="empty-state">
          등록된 프로젝트가 없습니다.
        </div>

        <div v-else class="project-grid">
          <article v-for="p in projects" :key="p.id" class="project-card">
            <router-link :to="`/projects/${p.id}`" class="card-link">
              
              <div class="card-image-wrapper">
                <img 
                  v-if="p.image || p.image_url" 
                  :src="getImageUrl(p.image || p.image_url)" 
                  alt="Project Image" 
                  class="card-img"
                />
                <div v-else class="no-image-placeholder">
                  <span class="placeholder-text">{{ p.title.substring(0, 1) }}</span>
                </div>
              </div>

              <div class="card-content">
                <h3 class="card-title">{{ p.title }}</h3>
                <p class="card-desc">{{ p.description }}</p>
                
                <div class="card-footer">
                  <span class="btn-text">자세히 보기 &rarr;</span>
                </div>
              </div>

            </router-link>
          </article>
        </div>

      </div>
    </section>
  </div>
</template>

<style scoped>
/* 공통 레이아웃 */
.container { max-width: 1100px; margin: 0 auto; padding: 0 20px; }

/* 헤더 스타일 (AboutView와 통일감) */
.page-header {
  padding: 80px 0 50px;
  background-color: #fff;
}
.badge {
  display: inline-block; padding: 6px 12px;
  background-color: #e3f2fd; color: #1565c0;
  border-radius: 20px; font-size: 0.85rem; font-weight: 700;
  margin-bottom: 15px;
}
.page-title {
  font-size: 2.5rem; font-weight: 800; color: #212529;
  margin: 0 0 15px 0;
}
.page-desc {
  color: #555; font-size: 1.1rem; line-height: 1.6;
}

/* 그리드 레이아웃 (반응형 핵심) */
.project-list-section { padding-bottom: 100px; }

.project-grid {
  display: grid;
  /* 카드 최소 너비 320px, 공간 남으면 늘어남 */
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 30px;
}

/* 카드 디자인 */
.project-card {
  background: white;
  border: 1px solid #e9ecef;
  border-radius: 16px;
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  display: flex;
  flex-direction: column;
}

.project-card:hover {
  transform: translateY(-5px); /* 살짝 위로 뜸 */
  box-shadow: 0 12px 24px rgba(0,0,0,0.08); /* 그림자 */
  border-color: #42b883; /* 테두리 초록색 포인트 */
}

.card-link {
  text-decoration: none;
  color: inherit;
  display: flex;
  flex-direction: column;
  height: 100%;
}

/* 이미지 영역 (비율 고정) */
.card-image-wrapper {
  width: 100%;
  height: 200px; /* 높이 고정하여 들쑥날쑥 방지 */
  background-color: #f8f9fa;
  overflow: hidden;
  position: relative;
  border-bottom: 1px solid #f1f1f1;
}

.card-img {
  width: 100%; height: 100%;
  object-fit: cover; /* 비율 유지하며 꽉 채우기 */
  transition: transform 0.5s ease;
}

.project-card:hover .card-img {
  transform: scale(1.05); /* 마우스 올리면 이미지 살짝 확대 */
}

/* 이미지가 없을 때 대체 디자인 */
.no-image-placeholder {
  width: 100%; height: 100%;
  background: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
  display: flex; align-items: center; justify-content: center;
}
.placeholder-text {
  font-size: 3rem; font-weight: 800; color: #dee2e6;
}

/* 텍스트 내용 영역 */
.card-content {
  padding: 24px;
  flex-grow: 1; /* 높이 맞춤 */
  display: flex;
  flex-direction: column;
}

.card-title {
  font-size: 1.25rem; font-weight: 700; color: #212529;
  margin: 0 0 12px 0;
  line-height: 1.4;
}

.card-desc {
  font-size: 0.95rem; color: #666;
  line-height: 1.6;
  margin-bottom: 20px;
  /* 3줄 이상 넘어가면 ... 처리 (CSS Line Clamp) */
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

.card-footer {
  margin-top: auto; /* 버튼을 항상 바닥으로 */
}

.btn-text {
  font-size: 0.9rem; font-weight: 700; color: #42b883;
}

/* 로딩 & 빈 상태 */
.loading-state, .empty-state {
  text-align: center; padding: 60px 0; color: #868e96;
}
.spinner {
  width: 40px; height: 40px; margin: 0 auto;
  border: 4px solid #f3f3f3; border-top: 4px solid #42b883;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}
@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

/* 모바일 대응 */
@media (max-width: 768px) {
  .project-grid { grid-template-columns: 1fr; } /* 모바일은 1단 */
  .page-title { font-size: 2rem; }
}
</style>