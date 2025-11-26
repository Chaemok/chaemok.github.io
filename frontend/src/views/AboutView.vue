<script setup>
import { ref, onMounted } from 'vue'

// 1. 프로필 사진 Asset Import (경로와 파일명 확인하세요)
import profileImage from '@/assets/leechaemok.jpg'

const timelines = ref([])
const isLoading = ref(true)

const API_URL = import.meta.env.VITE_API_URL

// 2. 타임라인 데이터 API 호출
onMounted(async () => {
  try {
    // 배포된 Render 주소로 API 요청 (https://chaemok.onrender.com/api/timelines/)
    // 이제 API_URL이 개발 환경에서는 127.0.0.1:8000, 배포 환경에서는 render.com이 됩니다.
    const res = await fetch(`${API_URL}/api/timelines/`)
    if (res.ok) {
      timelines.value = await res.json()
    }
  } catch (err) {
    console.error("타임라인 API 호출 오류:", err)
  } finally {
    isLoading.value = false
  }
})
</script>

<template>
  <div class="about-container">
    
    <section class="profile-section">
      <div class="profile-img-box">
        <img :src="profileImage" alt="profile" class="profile-img" />
      </div>
      <div class="profile-text">
        <h2>"꾸준히 생각하는 개발자, <span class="highlight">이채목</span>입니다"</h2>
        <p>
          사용자의 불편함을 기술로 해결할 때 가장 큰 희열을 느낍니다.<br>
          Django의 논리적인 구조와 Vue.js의 직관적인 인터랙션을 좋아하며,<br>
          동료와 함께 성장하는 문화를 지향합니다.
        </p>
      </div>
    </section>

    <hr class="divider">

    <section class="history-section">
      <h3>🚀 My Journey</h3>
      
      <div v-if="isLoading" class="loading">로딩 중...</div>
      
      <div v-else class="timeline">
        <div 
          v-for="(item, index) in timelines" 
          :key="item.id" 
          class="timeline-item animate-up"
          :style="{ animationDelay: `${index * 0.1}s` }"
        >
          <div class="timeline-date">
            {{ item.start_date }} ~ {{ item.end_date || '현재' }}
          </div>
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <h4>{{ item.title }}</h4>
            <p>{{ item.description }}</p>
          </div>
        </div>
      </div>
    </section>
    
    <hr class="divider">

    <section class="contact-section">
      <h3>📬 Contact</h3>
      <div class="contact-links">
        <a href="mailto:lcm9211@naver.com" class="contact-pill">📧 Email</a>
        <a href="https://github.com/chaemok" target="_blank" class="contact-pill">🐱 GitHub</a>
        <a href="https://instagram.com/2chaemogi" target="_blank" class="contact-pill">📝 Instagram</a>
      </div>
    </section>

  </div>
</template>

<style scoped>
/* 애니메이션 정의 */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.about-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 60px 20px;
  animation: fadeIn 0.5s ease;
}

/* 프로필 섹션 */
.profile-section { display: flex; align-items: center; gap: 50px; margin-bottom: 60px; }
.profile-img-box { flex-shrink: 0; }
.profile-img { width: 200px; height: 200px; border-radius: 50%; object-fit: cover; box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
.profile-text h2 { font-size: 2rem; margin-bottom: 20px; color: #2c3e50; line-height: 1.3; }
.profile-text p { font-size: 1.1rem; color: #555; line-height: 1.8; }
.highlight { color: #42b883; font-weight: 800; }
.divider { border: 0; height: 1px; background: #eee; margin: 60px 0; }

/* 타임라인 스타일 */
.history-section h3, .contact-section h3 { font-size: 1.8rem; color: #2c3e50; margin-bottom: 40px; text-align: center; }

.timeline { border-left: 3px solid #e9ecef; padding-left: 30px; margin-left: 20px; }
.timeline-item { position: relative; margin-bottom: 40px; opacity: 0; /* 애니메이션 시작점 */ }

/* 애니메이션 적용 */
.animate-up { animation: fadeInUp 0.6s ease-out forwards; }

.timeline-item::before { position: absolute; left: -38px; top: 5px; width: 14px; height: 14px; background: #42b883; border-radius: 50%; border: 3px solid white; box-shadow: 0 0 0 3px #eee; content: ''; }
.timeline-date { font-size: 0.9rem; color: #888; margin-bottom: 5px; font-weight: 600; }
.timeline-content h4 { font-size: 1.2rem; margin: 0 0 10px 0; color: #333; }
.timeline-content p { color: #666; line-height: 1.6; }

/* Contact 스타일 */
.contact-links { display: flex; justify-content: center; gap: 20px; }
.contact-pill { padding: 10px 25px; background: white; border: 1px solid #ddd; border-radius: 50px; text-decoration: none; color: #555; font-weight: 600; transition: all 0.3s; }
.contact-pill:hover { background: #42b883; color: white; border-color: #42b883; transform: translateY(-3px); }

@media (max-width: 768px) {
  .profile-section { flex-direction: column; text-align: center; gap: 30px; }
  .profile-text h2 { font-size: 1.5rem; }
}
</style>