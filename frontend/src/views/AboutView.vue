<script setup>
import { ref, onMounted } from 'vue'

const timelines = ref([])
const isLoading = ref(true)

onMounted(async () => {
  try {
    // Django API 호출
    const res = await fetch('https://chaemok.onrender.com/api/timelines/')
    if (res.ok) {
      timelines.value = await res.json()
    }
  } catch (err) {
    console.error(err)
  } finally {
    isLoading.value = false
  }
})
</script>

<template>
  <div class="about-container">
    <div class="header-section">
      <h1>🚀 My Journey</h1>
      <p>저의 성장 과정과 경험을 소개합니다.</p>
    </div>

    <div class="timeline-wrapper">
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
            <h3>{{ item.title }}</h3>
            <p>{{ item.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.about-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 60px 20px;
}

.header-section { text-align: center; margin-bottom: 60px; }
.header-section h1 { font-size: 2.5rem; color: #2c3e50; margin-bottom: 10px; }
.header-section p { color: #666; }

/* 타임라인 스타일 */
.timeline {
  position: relative;
  border-left: 2px solid #e9ecef; /* 깔끔한 회색 라인 */
  padding-left: 30px;
  margin-left: 20px;
}

.timeline-item {
  position: relative;
  margin-bottom: 50px;
  opacity: 0; /* 애니메이션 시작 전 투명 */
}

.timeline-dot {
  position: absolute;
  left: -39px;
  top: 0;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: #42b883; /* Vue 초록색 */
  border: 4px solid white; /* 흰색 테두리로 깔끔하게 */
  box-shadow: 0 0 0 2px #e9ecef;
}

.timeline-date {
  font-size: 0.9rem;
  font-weight: 700;
  color: #42b883;
  margin-bottom: 8px;
}

.timeline-content h3 {
  margin: 0 0 10px 0;
  font-size: 1.25rem;
  color: #333;
}

.timeline-content p {
  margin: 0;
  color: #666;
  line-height: 1.6;
}

/* 깔끔한 등장 애니메이션 (아래에서 위로) */
.animate-up {
  animation: fadeInUp 0.6s ease-out forwards;
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.loading { text-align: center; color: #999; }
</style>  