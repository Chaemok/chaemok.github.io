<script setup>
//const API_URL = import.meta.env.VITE_API_URL // 로컬에서
const API_URL = 'https://chaemok-github-io.onrender.com'
import { ref, onMounted } from 'vue'

const skills = ref([])

onMounted(async () => {
  try {
    const res = await fetch(`${API_URL}/api/skills/`)
    skills.value = await res.json()
  } catch (err) { console.error(err) }
})
</script>

<template>
  <div class="home-container">
    <section class="hero-section">
      <div class="container hero-content">
        <div class="text-box">
          <span class="badge">Junior Web Developer</span>
          
          <h1 class="hero-title">
            어제보다 더<br>
            <span class="highlight">똑똑한 서비스를 위해</span>
          </h1>
          
          <p class="hero-subtitle">
            안정적인 웹 기술 위에 새로운 가능성을 더합니다.<br>
            웹 개발의 기본기를 바탕으로, 앞으로는 <strong>AI 기술</strong>을 접목해<br>
            더 똑똑한 서비스를 만들고 싶습니다.<br>
            <strong>배움을 멈추지 않고, 어제보다 나은 코드를 고민합니다.</strong>
          </p>
          
          <div class="hero-buttons">
            <router-link to="/projects" class="btn btn-primary">프로젝트 보러가기</router-link>
            <router-link to="/about" class="btn btn-outline">저에 대해 더 알아보기</router-link>
          </div>
        </div>
      </div>
    </section>

    <section class="skills-section">
      <div class="container">
        <h2 class="section-title">🛠️ Technology</h2>
        <p class="section-desc">목적에 맞는 도구를 선택하고 학습합니다.</p>
        <div class="skill-grid">
          <div v-for="skill in skills" :key="skill.id" class="skill-card">
            <div class="skill-header">
              <span class="skill-name">{{ skill.name }}</span>
            </div>
            <div class="progress-bar">
               <div class="progress-fill" :class="skill.level ? skill.level.toLowerCase() : 'beginner'"></div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template> 

<style scoped>
/* 이 내용을 <style scoped> 안에 덮어씌우세요 */

.container { 
  max-width: 1100px; 
  margin: 0 auto; 
  padding: 0 20px; 
}

/* 1. Hero 섹션: 전체를 감싸는 배경 */
.hero-section {
  display: flex;
  align-items: center;       /* 수직 중앙 정렬 */
  justify-content: center;   /* 수평 중앙 정렬 */
  min-height: 80vh;          /* 화면 높이의 80%를 차지해서 시원하게 */
  background-color: #fff;
  padding: 0;                /* 패딩 제거 (min-height로 대체) */
}

/* 2. 텍스트 박스: 핵심! 박스는 가운데지만 글자는 왼쪽 */
.text-box {
  width: 100%;
  max-width: 680px;      /* 글자가 너무 퍼지지 않게 적당히 조임 */
  margin: 0 auto;        /* 박스 자체를 화면 가운데로 */
  text-align: left;      /* 글자는 왼쪽 정렬 (가독성 UP) */
}

.badge {
  display: inline-block; padding: 8px 16px;
  background-color: #f1f3f5; color: #495057; /* 색상을 조금 더 차분하게 변경 */
  border-radius: 30px; font-size: 0.9rem; font-weight: 700;
  margin-bottom: 24px;
}

.hero-title {
  font-size: 3.8rem;     /* 제목은 아주 크게 */
  font-weight: 800;
  color: #212529;
  line-height: 1.2;
  margin-bottom: 30px;
  letter-spacing: -1px;  /* 자간을 살짝 좁혀서 단단한 느낌 */
}

.highlight {
  color: #42b883;
  position: relative; /* 형광펜 효과 제거하고 깔끔하게 색상만 강조 */
}

.hero-subtitle {
  font-size: 1.15rem;
  color: #495057;
  line-height: 1.8;
  margin-bottom: 50px;
  word-break: keep-all;
}

/* 버튼 그룹: 왼쪽 정렬 */
.hero-buttons {
  display: flex;
  gap: 15px;
  justify-content: flex-start; /* 버튼도 왼쪽에서 시작 */
}

/* 버튼 스타일 */
.btn {
  padding: 15px 35px; /* 버튼 크기 좀 더 키움 */
  border-radius: 8px;
  font-weight: 700;
  font-size: 1rem;
  text-decoration: none;
  transition: all 0.2s ease;
}
.btn-primary {
  background: #212529; color: white; border: 1px solid #212529;
}
.btn-primary:hover {
  background: #42b883; border-color: #42b883; transform: translateY(-3px);
}
.btn-outline {
  background: white; color: #495057; border: 1px solid #dee2e6;
}
.btn-outline:hover {
  background: #f8f9fa; border-color: #adb5bd; color: #212529; transform: translateY(-3px);
}

/* Skills Section 등 나머지는 그대로 유지 */
.skills-section { padding: 100px 0; background: #f8f9fa; }
.section-title { font-size: 2.2rem; font-weight: 800; text-align: center; margin-bottom: 10px; color: #1a1a1a; }
.section-desc { text-align: center; color: #666; margin-bottom: 50px; font-size: 1.1rem; }
.skill-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 20px; }
.skill-card { background: white; padding: 20px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.04); transition: transform 0.2s; border: 1px solid #eee; }
.skill-card:hover { transform: translateY(-3px); border-color: #42b883; }
.skill-name { font-weight: 700; color: #333; font-size: 1.1rem; display: block; margin-bottom: 12px; }
.progress-bar { width: 100%; height: 6px; background: #eee; border-radius: 3px; overflow: hidden; }
.progress-fill { height: 100%; border-radius: 3px; }
.progress-fill.advanced { width: 90%; background: #42b883; }
.progress-fill.intermediate { width: 65%; background: #fbc02d; }
.progress-fill.beginner { width: 30%; background: #ff7043; }

/* 모바일 반응형 */
@media (max-width: 768px) {
  .hero-title { font-size: 2.8rem; }
  .text-box { text-align: center; } /* 모바일에서는 다시 가운데 정렬이 예쁨 */
  .hero-buttons { justify-content: center; }
}
</style>