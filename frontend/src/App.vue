<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'

// 1. 메뉴 개폐 상태 변수
const isMenuOpen = ref(false)

// 2. 햄버거 버튼 토글 함수
const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

// 3. 메뉴 닫기 함수 (이동 후 닫기)
const closeMenu = () => {
  isMenuOpen.value = false
}
</script>

<template>
  <!-- 👇 여기 열린 태그가 맨 밑에서 닫혀야 합니다 -->
  <div class="app-layout">
    <header>
      <div class="wrapper">
        <div class="logo">
          <RouterLink to="/" @click="closeMenu">Chaemok.Dev</RouterLink>
        </div>

        <!-- 데스크탑 메뉴 -->
        <nav class="desktop-nav">
          <RouterLink to="/">Home</RouterLink>
          <RouterLink to="/about">About</RouterLink>
          <RouterLink to="/projects">Projects</RouterLink>
          <RouterLink to="/contact">Contact</RouterLink>
        </nav>

        <!-- 햄버거 버튼 -->
        <button class="hamburger-btn" @click="toggleMenu">
          ☰
        </button>
      </div>

      <!-- 모바일 메뉴 -->
      <nav class="mobile-nav" :class="{ 'open': isMenuOpen }">
        <RouterLink to="/" @click="closeMenu">Home</RouterLink>
        <RouterLink to="/about" @click="closeMenu">About</RouterLink>
        <RouterLink to="/projects" @click="closeMenu">Projects</RouterLink>
        <RouterLink to="/contact" @click="closeMenu">Contact</RouterLink>
      </nav>
    </header>

    <!-- 본문 -->
    <main class="main-content">
      <RouterView />
    </main>

    <!-- 푸터 -->
    <footer class="app-footer">
      <div class="footer-content">
        <!-- 안내 문구 -->
        <p class="portfolio-notice">
          본 사이트는 상업적 목적으로 제작되지 않았으며, 개인 포트폴리오 용도로 제작되었습니다.
        </p>

        <p>© 2025 Lee Chae-mok. All Rights Reserved.</p>
        
        <div class="social-links">
          <RouterLink to="/contact">Contact Me</RouterLink>
          <a href="mailto:lcm9211@naver.com">Email</a>
        </div>
      </div>
    </footer>
  </div> <!-- 👈 [중요] 아까 빠졌던 닫는 태그입니다! -->
</template>

<style scoped>
/* 전체 레이아웃 */
.app-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main-content {
  flex: 1;
}

/* 헤더 스타일 */
header {
  background-color: white;
  border-bottom: 1px solid #eee;
  position: sticky;
  top: 0;
  z-index: 1000;
}

.wrapper {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 20px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo a {
  font-size: 1.5rem;
  font-weight: 800;
  color: #212529;
  text-decoration: none;
}

/* 데스크탑 메뉴 */
.desktop-nav a {
  margin-left: 20px;
  text-decoration: none;
  color: #495057;
  font-weight: 500;
  transition: color 0.2s;
}

.desktop-nav a:hover, .desktop-nav a.router-link-active {
  color: #42b883;
}

/* 햄버거 버튼 */
.hamburger-btn {
  display: none;
  background: none;
  border: none;
  font-size: 1.8rem;
  cursor: pointer;
  color: #333;
}

/* 모바일 메뉴 박스 */
.mobile-nav {
  display: none;
  background-color: white;
  border-bottom: 1px solid #eee;
  flex-direction: column;
  padding: 10px 0;
}

.mobile-nav a {
  display: block;
  padding: 15px 20px;
  text-decoration: none;
  color: #333;
  font-weight: 600;
  border-bottom: 1px solid #f8f9fa;
}

.mobile-nav a:hover {
  background-color: #f8f9fa;
  color: #42b883;
}

/* 푸터 스타일 */
.app-footer {
  background-color: #f8f9fa;
  padding: 40px 0;
  margin-top: auto;
  text-align: center;
  border-top: 1px solid #eee;
}

.footer-content p {
  color: #868e96;
  font-size: 0.9rem;
  margin-bottom: 10px;
}

/* 저작권 안내 문구 스타일 */
.portfolio-notice {
  font-size: 0.8rem;
  color: #adb5bd;
  margin-bottom: 15px; /* 간격 조정 */
  word-break: keep-all;
  line-height: 1.4;
  padding: 0 10px; /* 모바일에서 글자가 너무 붙지 않게 */
}

.social-links a {
  color: #495057;
  margin: 0 10px;
  font-size: 0.9rem;
  font-weight: 600;
  text-decoration: none;
}

.social-links a:hover {
  color: #42b883;
  text-decoration: underline;
}

/* 모바일 반응형 */
@media (max-width: 768px) {
  .desktop-nav {
    display: none;
  }

  .hamburger-btn {
    display: block;
  }

  .mobile-nav.open {
    display: flex;
  }
}
</style>