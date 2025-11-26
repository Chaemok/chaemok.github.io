<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router' // 주소창의 ID를 알아내는 도구

const route = useRoute()
const project = ref(null)
const isLoading = ref(true)

onMounted(async () => {
  try {
    // 주소창의 id(예: 1)를 가져와서 요청을 보냄
    const id = route.params.id 
    const res = await fetch(`https://chaemok.onrender.com/api/projects/${id}/`)
    
    if (res.ok) {
      project.value = await res.json()
    } else {
      alert("프로젝트를 찾을 수 없습니다.")
    }
  } catch (err) {
    console.error(err)
  } finally {
    isLoading.value = false
  }
})
</script>

<template>
  <div class="detail-container">
    <div v-if="isLoading" class="loading">로딩 중...</div>

    <div v-else-if="project" class="project-content">
      <header class="detail-header">
        <h1 class="title">{{ project.title }}</h1>
        <div class="links">
          <a v-if="project.github_url" :href="project.github_url" target="_blank" class="btn-github">
            GitHub 방문
          </a>
        </div>
      </header>

      <div class="image-box">
        <img v-if="project.image" :src="`https://chaemok.onrender.com${project.image}`" alt="project img" />
        <div v-else class="no-img">No Image</div>
      </div>

      <article class="description">
        <p>{{ project.description }}</p>
      </article>

      <div class="footer-btn">
        <router-link to="/projects" class="btn-back">← 목록으로</router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.detail-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 40px 20px;
  animation: fadeIn 0.5s ease;
}

.detail-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  border-bottom: 2px solid #eee;
  padding-bottom: 20px;
}

.title { font-size: 2.5rem; color: #2c3e50; margin: 0; }

.btn-github {
  background: #24292e; color: white; padding: 10px 20px;
  border-radius: 8px; font-weight: 600; font-size: 0.9rem;
}

.image-box {
  width: 100%; height: 400px; background: #f8f9fa;
  border-radius: 15px; overflow: hidden; margin-bottom: 40px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.05);
}
.image-box img { width: 100%; height: 100%; object-fit: cover; }
.no-img { width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; color: #aaa; }

.description {
  font-size: 1.1rem; line-height: 1.8; color: #444; margin-bottom: 50px;
  white-space: pre-line; /* 엔터키(줄바꿈)를 인식하게 함! */
}

.btn-back {
  display: inline-block; padding: 10px 25px; border: 1px solid #ddd;
  border-radius: 50px; color: #666; font-weight: 600; transition: all 0.3s;
}
.btn-back:hover { background: #f1f1f1; color: #333; }

@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

@media (max-width: 768px) {
  .detail-header { flex-direction: column; align-items: flex-start; gap: 15px; }
  .image-box { height: 250px; }
  .title { font-size: 2rem; }
}
</style>