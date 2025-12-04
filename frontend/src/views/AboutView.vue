<script setup>
import { ref, onMounted } from 'vue'

// 프로필 사진 경로 (본인 경로에 맞게 확인 필요)
import profileImage from '@/assets/leechaemok.jpg'

const timelines = ref([])
const isLoading = ref(true)
const API_URL = import.meta.env.VITE_API_URL

onMounted(async () => {
  try {
    const res = await fetch(`${API_URL}/api/timelines/`)
    if (res.ok) {
      timelines.value = await res.json()
    }
  } catch (err) {
    console.error("타임라인 로딩 실패:", err)
  } finally {
    isLoading.value = false
  }
})
</script>

<template>
  <div class="about-container">
    
    <section class="profile-section">
      <div class="profile-img-box">
        <img :src="profileImage" alt="이채목 프로필" class="profile-img" />
      </div>
      <div class="profile-text">
        <span class="badge">About Me</span>
        
        <h2 class="profile-title">
          복잡함은 <span class="highlight">덜어내고</span> 효율을 <span class="highlight">더합니다.</span>
        </h2>
        
        <p class="profile-greeting">
          안녕하세요, 주니어 개발자 <strong>이채목</strong>입니다.
        </p>

        <p class="profile-desc">
          단순한 기능 구현에 그치지 않고, <strong>반복되는 작업을 코드로 해결하여</strong> 
          실질적인 가치를 만드는 데 집중합니다.<br>
          혼자만의 속도보다는 <strong>팀의 방향성</strong>을 중요하게 생각하며, 
          적극적인 소통을 통해 <strong>함께 성장하는 개발자</strong>가 되겠습니다.
        </p>
      </div>
    </section>

    <div class="divider"></div>

    <section class="history-section">
      <h3 class="section-title">🚀 My Journey</h3>
      
      <div v-if="isLoading" class="loading-text">이력을 불러오는 중...</div>
      
      <div v-else class="timeline">
        <div 
          v-for="(item, index) in timelines" 
          :key="item.id" 
          class="timeline-item"
          :style="{ animationDelay: `${index * 0.2}s` }"
        >
          <div class="timeline-marker"></div>
          <div class="timeline-content">
            <span class="timeline-date">{{ item.start_date }} ~ {{ item.end_date || '현재' }}</span>
            <h4 class="timeline-title">{{ item.title }}</h4>
            <p class="timeline-desc">{{ item.description }}</p>
          </div>
        </div>
      </div>
    </section>
    
    <div class="divider"></div>

    <section class="contact-section">
      <h3 class="section-title">📬 Contact & Channel</h3>
      <div class="contact-links">
        
        <a href="mailto:lcm9211@naver.com" class="contact-card email">
          <svg class="icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75" />
          </svg>
          <span class="text">Email 보내기</span>
        </a>

        <a href="https://github.com/chaemok" target="_blank" class="contact-card github">
          <svg class="icon" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405 1.02 0 2.04.135 3 .405 2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
          </svg>
          <span class="text">GitHub 방문</span>
        </a>

        <a href="https://instagram.com/2chaemogi" target="_blank" class="contact-card instagram">
          <svg class="icon" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
          </svg>
          <span class="text">Instagram</span>
        </a>
        
      </div>
    </section>

  </div>
</template>

<style scoped>
/* 애니메이션 정의: 아래에서 위로 부드럽게 올라옴 */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

.about-container {
  max-width: 950px;
  margin: 0 auto;
  padding: 80px 20px;
  animation: fadeIn 0.5s ease;
}

/* 프로필 섹션 (기존 스타일 유지) */
.profile-section {
  display: flex; align-items: center; gap: 70px; margin-bottom: 80px;
}
.profile-img-box { flex-shrink: 0; }
.profile-img {
  width: 240px; height: 240px; border-radius: 50%;
  object-fit: cover; box-shadow: 0 20px 40px rgba(0,0,0,0.08); border: 4px solid white;
}
.profile-text { flex-grow: 1; }
.badge {
  display: inline-block; padding: 6px 14px;
  background: #f1f3f5; color: #495057; border-radius: 20px;
  font-size: 0.85rem; font-weight: 700; margin-bottom: 15px;
}
.profile-title {
  font-size: 2.4rem; font-weight: 800; color: #212529;
  line-height: 1.3; margin-bottom: 20px; word-break: keep-all;
}
.highlight { color: #42b883; }
.profile-greeting { font-size: 1.2rem; color: #343a40; margin-bottom: 12px; }
.profile-desc { font-size: 1.05rem; color: #555; line-height: 1.7; margin-top: 0; }
.profile-desc strong { 
  color: #212529; font-weight: 700; 
  background: linear-gradient(to top, #e6fcf5 50%, transparent 50%);
}
.divider { height: 1px; background: #e9ecef; margin: 70px 0; }
.section-title {
  font-size: 1.8rem; font-weight: 800; color: #212529;
  text-align: center; margin-bottom: 50px;
}

/* 타임라인 스타일 (수정됨) */
.timeline {
  position: relative;
  border-left: 2px solid #e9ecef;
  margin-left: 20px;
  padding-left: 30px;
}

/* 타임라인 아이템: 초기 상태는 안 보이게 처리 */
.timeline-item {
  position: relative;
  margin-bottom: 50px;
  opacity: 0; /* 시작할 때 투명 */
  /* 애니메이션 적용: forwards는 애니메이션 끝난 상태(보임) 유지 */
  animation: fadeInUp 0.8s cubic-bezier(0.22, 1, 0.36, 1) forwards; 
}
.timeline-item:last-child { margin-bottom: 0; }

.timeline-marker {
  position: absolute; left: -37px; top: 6px;
  width: 12px; height: 12px;
  background: white; border: 3px solid #42b883;
  border-radius: 50%;
  z-index: 1;
  box-shadow: 0 0 0 3px #f8f9fa; /* 마커 주변 흰색 테두리 효과 */
}

.timeline-date {
  display: inline-block;
  font-size: 0.9rem; font-weight: 700; color: #42b883;
  margin-bottom: 6px;
  background: #e6fcf5; padding: 2px 8px; border-radius: 4px;
}
.timeline-title {
  font-size: 1.35rem; font-weight: 700; color: #343a40; margin: 0 0 8px;
}
.timeline-desc {
  font-size: 1rem; color: #495057; line-height: 1.6;
}

/* 연락처 카드 스타일 (수정됨) */
.contact-links {
  display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;
}
.contact-card {
  display: flex; align-items: center; gap: 12px;
  background: white; border: 1px solid #dee2e6;
  padding: 16px 32px; border-radius: 50px;
  text-decoration: none; color: #495057; font-weight: 600;
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

/* 아이콘 사이즈 조절 */
.icon { width: 22px; height: 22px; }

/* 호버 효과: 각 브랜드 색상으로 변경 */
.contact-card:hover { transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.08); }

/* Email Hover */
.contact-card.email:hover { border-color: #fab005; color: #fab005; }
/* GitHub Hover */
.contact-card.github:hover { border-color: #24292e; color: #24292e; }
/* Instagram Hover */
.contact-card.instagram:hover { border-color: #e1306c; color: #e1306c; }

.loading-text { text-align: center; color: #adb5bd; padding: 40px; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

/* 모바일 반응형 */
@media (max-width: 768px) {
  .profile-section { flex-direction: column; text-align: center; gap: 30px; }
  .profile-img { width: 180px; height: 180px; }
  .profile-title { font-size: 1.8rem; }
  .contact-links { flex-direction: column; width: 100%; }
  .contact-card { justify-content: center; width: 100%; }
}
</style>