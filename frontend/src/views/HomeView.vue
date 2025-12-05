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
/* =========================================
   1. 공통 스타일 (PC 및 기본 레이아웃)
   ========================================= */
.home-container {
  width: 100%;
  overflow-x: hidden; /* 가로 스크롤 방지 */
}

.container { 
  max-width: 1100px; 
  margin: 0 auto; 
  padding: 0 24px; 
}

/* Hero 섹션 (메인 화면) */
.hero-section {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 85vh;          /* PC: 화면 꽉 차게 시원한 느낌 */
  background-color: #fff;
  padding: 60px 0;
}

.text-box {
  width: 100%;
  max-width: 720px;
  margin: 0 auto;
  text-align: left;          /* PC: 왼쪽 정렬 (세련된 느낌) */
}

.badge {
  display: inline-block; 
  padding: 8px 18px;
  background-color: #f8f9fa; 
  color: #495057;
  border: 1px solid #e9ecef;
  border-radius: 50px; 
  font-size: 0.95rem; 
  font-weight: 700;
  margin-bottom: 24px;
  letter-spacing: -0.5px;
}

.hero-title {
  font-size: 3.5rem;         /* PC: 너무 크지 않게 3.5rem으로 조정 (기존 4rem에서 축소) */
  font-weight: 800;
  color: #212529;
  line-height: 1.2;
  margin-bottom: 32px;
  letter-spacing: -1.5px;
}

.highlight {
  color: #42b883;            /* Vue Green */
}

.hero-subtitle {
  font-size: 1.2rem;
  color: #495057;
  line-height: 1.7;
  margin-bottom: 40px;
  word-break: keep-all;      /* 단어 중간에 끊기지 않게 */
}

.hero-buttons {
  display: flex;
  gap: 16px;
  justify-content: flex-start; /* PC: 버튼 왼쪽 정렬 */
}

.btn {
  padding: 16px 32px;
  border-radius: 12px;
  font-weight: 700;
  font-size: 1.05rem;
  text-decoration: none;
  transition: all 0.2s ease;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.btn-primary {
  background: #212529; color: white; border: 1px solid #212529;
}
.btn-primary:hover {
  background: #42b883; border-color: #42b883; transform: translateY(-3px);
  box-shadow: 0 4px 12px rgba(66, 184, 131, 0.3);
}

.btn-outline {
  background: white; color: #495057; border: 1px solid #dee2e6;
}
.btn-outline:hover {
  background: #f8f9fa; border-color: #adb5bd; color: #212529; transform: translateY(-3px);
}

/* Skills 섹션 스타일 */
.skills-section { padding: 100px 0; background: #f8f9fa; }
.section-title { font-size: 2.2rem; font-weight: 800; text-align: center; margin-bottom: 12px; color: #1a1a1a; letter-spacing: -1px; }
.section-desc { text-align: center; color: #666; margin-bottom: 60px; font-size: 1.1rem; }
.skill-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 24px; }
.skill-card { background: white; padding: 24px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); transition: transform 0.2s; border: 1px solid #f1f3f5; }
.skill-card:hover { transform: translateY(-5px); border-color: #42b883; }
.skill-name { font-weight: 700; color: #333; font-size: 1.15rem; display: block; margin-bottom: 16px; }
.progress-bar { width: 100%; height: 8px; background: #e9ecef; border-radius: 4px; overflow: hidden; }
.progress-fill { height: 100%; border-radius: 4px; }
.progress-fill.advanced { width: 90%; background: #42b883; }
.progress-fill.intermediate { width: 65%; background: #fbc02d; }
.progress-fill.beginner { width: 30%; background: #ff7043; }


/* =========================================
   2. 모바일 전용 스타일 (스마트폰 최적화)
   화면 폭이 768px 이하일 때만 적용됨
   ========================================= */
@media (max-width: 768px) {
  
  /* 높이 및 정렬 재조정 */
  .hero-section {
    min-height: auto;        /* 강제 높이 해제 (스크롤 자연스럽게) */
    padding: 80px 0 60px 0;  /* 위아래 여백 넉넉히 */
    text-align: center;      /* 전체 가운데 정렬 */
  }

  .text-box {
    text-align: center;      /* 글자 가운데 정렬 */
    padding: 0 16px;
    margin: 0 auto;
  }

  /* 폰트 크기 최적화 (너무 크지 않게) */
  .hero-title {
    font-size: 2.5rem;       /* 모바일 제목 크기 축소 */
    line-height: 1.3;
    margin-bottom: 20px;
  }
  
  .hero-subtitle {
    font-size: 1rem;         /* 본문 크기 살짝 축소 */
    line-height: 1.6;
    margin-bottom: 40px;
    color: #6c757d;
  }

  /* 요소 배치 재조정 */
  .badge {
    margin: 0 auto 20px auto; /* 뱃지 가운데 정렬 */
  }

  /* 버튼: 위아래로 쌓아서 누르기 편하게 */
  .hero-buttons {
    flex-direction: column;  /* 세로 배치 */
    width: 100%;
    gap: 12px;
  }

  .btn {
    width: 100%;             /* 버튼 꽉 채우기 */
    padding: 16px;
  }
  
  /* 스킬 카드 2열 배치 */
  .skill-grid {
    grid-template-columns: repeat(2, 1fr); 
    gap: 16px;
  }
  
  .skills-section {
    padding: 60px 0;
  }
}
</style>