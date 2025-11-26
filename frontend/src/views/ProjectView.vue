<script setup>
import { ref, onMounted } from 'vue'

const projects = ref([])
const isLoading = ref(true)
// Django 서버에서 데이터 가져오기
onMounted(async () => {
  try {
    const res = await fetch('https://chaemok-backend.onrender.com/api/projects/')
    projects.value = await res.json()
  } catch (err) { console.error(err) } finally { isLoading.value = false }
})
</script>

<template>
  <div class="project-page">
    <section class="page-header">
      <div class="container">
        <h2 class="page-title">💻 Projects</h2>
        <p class="page-desc">지금까지 진행한 주요 프로젝트입니다.</p>
      </div>
    </section>

    <section class="project-list-section">
      <div class="container">
        <div v-if="isLoading" class="loading">데이터를 불러오는 중...</div>
        
        <div v-else class="project-grid">
          <div v-for="p in projects" :key="p.id" class="project-card">
            <div class="card-image">
              <img v-if="p.image_url" :src="p.image_url" alt="project cover" />
              <div v-else class="no-image">No Image</div>
            </div>
            <div class="card-body">
              <h3 class="project-title">
                <router-link :to="`/projects/${p.id}`">{{ p.title }}</router-link>
              </h3>
              <p class="project-desc">{{ p.description }}</p>
              <a v-if="p.github_url" :href="p.github_url" target="_blank" class="btn-link">
                GitHub 보러가기 →
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.container { max-width: 1200px; margin: 0 auto; padding: 0 30px; }

/* 페이지 헤더 */
.page-header { background: #f9fafb; padding: 60px 0; text-align: center; border-bottom: 1px solid #eee; }
.page-title { font-size: 2.5rem; font-weight: 700; color: #2c3e50; margin-bottom: 10px; }
.page-desc { color: #777; }

/* 프로젝트 리스트 섹션 */
.project-list-section { padding: 60px 0; background: white; }

.project-grid {
  display: grid;
  /* PC에서는 3열, 태블릿 2열, 모바일 1열 자동 조정 */
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 30px;
}

.project-card {
  background: white;
  border: 1px solid #eee;
  border-radius: 12px;
  overflow: hidden;
  transition: all 0.3s ease;
  display: flex; flex-direction: column;
}
.project-card:hover { transform: translateY(-10px); box-shadow: 0 15px 30px rgba(0,0,0,0.1); border-color: transparent; }

.card-image { height: 200px; overflow: hidden; background: #f1f1f1; }
.card-image img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s; }
.project-card:hover .card-image img { transform: scale(1.05); }
.no-image { width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; color: #aaa; font-weight: 600; }

.card-body { padding: 25px; flex-grow: 1; display: flex; flex-direction: column; }
.project-title { font-size: 1.4rem; margin: 0 0 15px; color: #2c3e50; }
.project-desc { color: #555; line-height: 1.6; margin-bottom: 25px; flex-grow: 1; /* 설명이 짧아도 버튼 위치 맞춤 */ }

.btn-link {
  display: inline-block; text-align: center;
  padding: 12px 0; background: #2c3e50; color: white; border-radius: 8px;
  font-weight: 600; transition: background 0.3s;
}
.btn-link:hover { background: #42b883; }

.loading { text-align: center; padding: 50px; color: #777; }

@media (min-width: 1024px) { .container { padding: 0; } }

/* style scoped 안에 추가 */
.project-title a {
  text-decoration: none;
  color: inherit; /* 원래 색상 유지 */
  transition: color 0.2s;
}
.project-title a:hover {
  color: #42b883; /* 마우스 올리면 초록색 */
}
</style>

<!-- <script setup>
  import { ref, onMounted } from 'vue'

  const projects = ref([])
  const isLoading = ref(true)

  onMounted(async () => {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/projects/')
      projects.value = await res.json()
    } catch (err) { console.error(err) } finally { isLoading.value = false }
  })
</script>

<template>
  <div class="page-container">
    <h2 class="page-title">💻 Projects</h2>
    
    <div v-if="isLoading">Loading...</div>
    <div v-else class="project-grid">
      <div v-for="p in projects" :key="p.id" class="project-card">
        <img v-if="p.image_url" :src="p.image_url" class="project-img" />
        <div v-else class="no-img">No Image</div>
        <div class="card-content">
          <h3>{{ p.title }}</h3>
          <p>{{ p.description }}</p>
          <a v-if="p.github_url" :href="p.github_url" target="_blank" class="btn-link">View GitHub</a>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .page-container { padding: 40px 0; animation: fadeIn 0.5s ease; }
  .page-title { font-size: 2rem; font-weight: 800; color: #2d3748; margin-bottom: 30px; }
  .project-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; }
  .project-card { background: white; border-radius: 15px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.05); transition: transform 0.3s; }
  .project-card:hover { transform: translateY(-5px); }
  .project-img { width: 100%; height: 180px; object-fit: cover; }
  .no-img { width: 100%; height: 180px; background: #cbd5e0; display: flex; align-items: center; justify-content: center; color: #fff; }
  .card-content { padding: 20px; }
  .card-content h3 { margin: 0 0 10px 0; font-size: 1.2rem; }
  .card-content p { color: #718096; font-size: 0.9rem; margin-bottom: 20px; line-height: 1.5; }
  .btn-link { display: inline-block; padding: 8px 16px; background: #2d3748; color: white; text-decoration: none; border-radius: 6px; font-size: 0.85rem; }
  @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
</style> -->