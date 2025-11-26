<script setup>
import { ref, onMounted } from 'vue'

const skills = ref([])
// Django 서버에서 데이터 가져오기
onMounted(async () => {
  try {
    const res = await fetch('http://127.0.0.1:8000/api/skills/')
    skills.value = await res.json()
  } catch (err) { console.error(err) }
})
</script>

<template>
  <div class="home-container">
    <section class="hero-section">
      <div class="container">
        <h1 class="hero-title">
          안녕하세요,<br>
          신입 개발자 <span class="highlight">이채목</span>입니다.
        </h1>
        <p class="hero-subtitle">
          SSAFY 14기 Python Track.<br>
          Django의 견고함과 Vue.js의 유연함으로 가치 있는 웹 서비스를 만듭니다.
        </p>
        <div class="hero-buttons">
          <router-link to="/projects" class="btn btn-primary">프로젝트 보기</router-link>
          <a href="https://github.com/본인아이디" target="_blank" class="btn btn-outline">GitHub 방문</a>
        </div>
      </div>
    </section>

    <section class="skills-section">
      <div class="container">
        <h2 class="section-title">🛠️ My Tech Stacks</h2>
        <p class="section-desc">현재 활용 가능한 기술 스택입니다.</p>
        
        <div class="skill-grid">
          <div v-for="skill in skills" :key="skill.id" class="skill-card">
            <span class="skill-name">{{ skill.name }}</span>
            <span v-if="skill.level" class="skill-level" :class="skill.level.toLowerCase()">
              {{ skill.level }}
            </span>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* 공통 컨테이너 (너비 제한 및 중앙 정렬) */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 30px;
}

/* Hero 섹션 스타일 */
.hero-section {
  padding: 120px 0 100px; /* 상하 여백 시원하게 */
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); /* 은은한 그라데이션 배경 */
}

.hero-title {
  font-size: 3.5rem; /* 글자 크기 키움 */
  font-weight: 800;
  color: #2c3e50;
  line-height: 1.2;
  margin-bottom: 20px;
}

.highlight {
  color: #42b883; /* 포인트 컬러 */
  position: relative;
  z-index: 1;
}
.highlight::after {
  content: '';
  position: absolute;
  bottom: 5px; left: 0; width: 100%; height: 15px;
  background: rgba(66, 184, 131, 0.2); /* 형광펜 효과 */
  z-index: -1;
}

.hero-subtitle {
  font-size: 1.2rem;
  color: #555;
  line-height: 1.6;
  margin-bottom: 40px;
}

.hero-buttons { display: flex; gap: 15px; }

/* 버튼 스타일 */
.btn { padding: 12px 30px; border-radius: 8px; font-weight: 600; transition: all 0.3s; cursor: pointer;}
.btn-primary { background: #42b883; color: white; border: none; }
.btn-primary:hover { background: #3aa876; transform: translateY(-3px); box-shadow: 0 5px 15px rgba(66, 184, 131, 0.3); }
.btn-outline { background: transparent; color: #42b883; border: 2px solid #42b883; }
.btn-outline:hover { background: #42b883; color: white; }

/* Skills 섹션 스타일 */
.skills-section { padding: 80px 0; background: white; }
.section-title { font-size: 2rem; font-weight: 700; color: #2c3e50; margin-bottom: 10px; text-align: center;}
.section-desc { text-align: center; color: #777; margin-bottom: 40px; }

.skill-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); /* 반응형 그리드 */
  gap: 20px;
  justify-content: center;
}

.skill-card {
  background: #f9fafb;
  border: 1px solid #eee;
  padding: 20px;
  border-radius: 12px;
  text-align: center;
  transition: transform 0.3s, box-shadow 0.3s;
}
.skill-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.05);
  border-color: #42b883;
}

.skill-name { display: block; font-weight: 700; font-size: 1.1rem; color: #333; margin-bottom: 10px; }
.skill-level { font-size: 0.8rem; padding: 4px 10px; border-radius: 20px; background: #eee; color: #555; }
.skill-level.advanced { background: #e3f2fd; color: #1565c0; }
.skill-level.intermediate { background: #e8f5e9; color: #2e7d32; }
.skill-level.beginner { background: #fff3e0; color: #ef6c00; }

/* PC 화면 최적화 */
@media (min-width: 1024px) {
  .hero-title { font-size: 4.5rem; }
  .container { padding: 0; } /* 좌우 여백 제거 */
}
</style>
<!-- <script setup>
  import { ref, onMounted } from 'vue'

  const skills = ref([])
  const isLoading = ref(true)

  onMounted(async () => {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/skills/')
      skills.value = await res.json()
    } catch (err) { console.error(err) } finally { isLoading.value = false }
  })
</script>

<template>
  <div class="page-container">
    <section class="hero">
      <h1>안녕하세요,<br>주니어 개발자 <span class="highlight">이채목</span>입니다.</h1>
      <p>Developer</p>
    </section>

    <section class="section">
      <h2>🛠 Tech Stacks</h2>
      <div v-if="isLoading">Loading...</div>
      <div v-else class="skill-cloud">
        <span v-for="skill in skills" :key="skill.id" class="skill-tag">
          {{ skill.name }}
          <span v-if="skill.level" class="level-dot" :class="skill.level.toLowerCase()"></span>
        </span>
      </div>
    </section>
  </div>
</template>

<style scoped>
  .page-container { padding: 40px 0; animation: fadeIn 0.5s ease; }
  .hero { margin-bottom: 60px; text-align: left; }
  h1 { font-size: 2.5rem; font-weight: 800; color: #2d3748; line-height: 1.2; margin-bottom: 10px; }
  .highlight { color: #667eea; }
  .section h2 { font-size: 1.5rem; margin-bottom: 20px; color: #4a5568; }
  .skill-cloud { display: flex; flex-wrap: wrap; gap: 10px; }
  .skill-tag { background: #edf2f7; padding: 8px 16px; border-radius: 20px; font-weight: 600; color: #4a5568; display: flex; align-items: center; gap: 8px;}
  .level-dot { width: 8px; height: 8px; border-radius: 50%; }
  .level-dot.advanced { background: #48bb78; } .level-dot.intermediate { background: #ecc94b; } .level-dot.beginner { background: #ed8936; }
  @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
</style> -->