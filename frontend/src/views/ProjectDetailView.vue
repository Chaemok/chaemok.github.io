<script setup>
const API_URL = import.meta.env.VITE_API_URL
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const project = ref(null)
const isLoading = ref(true)

onMounted(async () => {
  try {
    const id = route.params.id 
    const res = await fetch(`${API_URL}/api/projects/${id}/`)
    if (res.ok) {
      project.value = await res.json()
    }
  } catch (err) { console.error(err) } finally { isLoading.value = false }
})
</script>

<template>
  <div class="detail-container">
    <div v-if="isLoading" class="loading-state">로딩 중...</div>

    <div v-else-if="project" class="content-wrapper">
      <header class="detail-header">
        <h1 class="title">{{ project.title }}</h1>
        <div class="actions">
          <a v-if="project.github_url" :href="project.github_url" target="_blank" class="btn-github">
            GitHub Repository
          </a>
        </div>
      </header>

      <div class="image-box">
        <img v-if="project.image" :src="`https://chaemok.onrender.com${project.image}`" alt="project img" />
        
        <div v-else class="no-image">
          <span>{{ project.title }}</span>
        </div>
      </div>

      <article class="description">
        <p>{{ project.description }}</p>
      </article>

      <div class="footer-nav">
        <router-link to="/projects" class="btn-back">← 목록으로 돌아가기</router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.detail-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 60px 20px;
  animation: fadeIn 0.4s ease;
}

.detail-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 40px;
  flex-wrap: wrap;
  gap: 20px;
}

.title {
  font-size: 2.8rem;
  font-weight: 800;
  color: #1a1a1a;
  margin: 0;
  line-height: 1.2;
}

.btn-github {
  background: #24292e;
  color: white;
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.2s;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}
.btn-github:hover { background: #000; transform: translateY(-2px); }

/* 이미지 박스 스타일 */
.image-box {
  width: 100%;
  max-height: 500px;
  background: #f8f9fa;
  border-radius: 20px;
  overflow: hidden;
  margin-bottom: 50px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.08);
}
.image-box img { width: 100%; height: 100%; object-fit: cover; }

.no-image {
  width: 100%; height: 400px;
  background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
  display: flex; align-items: center; justify-content: center;
  color: white; font-size: 2rem; font-weight: 700; opacity: 0.8;
}

/* 본문 스타일 (가독성 중요) */
.description {
  font-size: 1.15rem;
  line-height: 1.9;
  color: #444;
  margin-bottom: 80px;
  white-space: pre-line; /* 줄바꿈 유지 */
}

/* 목록으로 돌아가기 버튼 */
.btn-back {
  display: inline-block;
  padding: 12px 30px;
  border: 1px solid #ddd;
  border-radius: 50px;
  color: #666;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.3s;
}
.btn-back:hover { background: #f1f1f1; color: #1a1a1a; border-color: #ccc; }

.loading-state { text-align: center; padding: 60px; color: #888; }

@keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

@media (max-width: 768px) {
  .title { font-size: 2rem; }
  .detail-header { flex-direction: column; align-items: flex-start; }
  .image-box { height: 250px; }
}
</style>