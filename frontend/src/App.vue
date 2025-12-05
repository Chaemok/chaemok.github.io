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
  <div class="app-layout">
    <header>
      <div class="wrapper">
        <div class="logo">
          <RouterLink to="/" @click="closeMenu">Chaemok.Dev</RouterLink>
        </div>

        <nav class="desktop-nav">
          <RouterLink to="/">Home</RouterLink>
          <RouterLink to="/about">About</RouterLink>
          <RouterLink to="/projects">Projects</RouterLink>
          <RouterLink to="/contact">Contact</RouterLink>
        </nav>

        <button class="hamburger-btn" @click="toggleMenu">
          ☰
        </button>
      </div>

      <nav class="mobile-nav" :class="{ 'open': isMenuOpen }">
        <RouterLink to="/" @click="closeMenu">Home</RouterLink>
        <RouterLink to="/about" @click="closeMenu">About</RouterLink>
        <RouterLink to="/projects" @click="closeMenu">Projects</RouterLink>
        <RouterLink to="/contact" @click="closeMenu">Contact</RouterLink>
      </nav>
    </header>

    <main class="main-content">
      <RouterView />
    </main>

    <footer class="app-footer">
      <div class="footer-content">
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
</template>

<style scoped>
/* 전체 레이아웃 잡기 (푸터를 바닥에 붙이기 위함) */
.app-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* 화면 전체 높이 */
}

.main-content {
  flex: 1; /* 남은 공간을 다 차지해서 푸터를 밀어냄 */
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

/* 👇 푸터 스타일 추가 */
.app-footer {
  background-color: #f8f9fa; /* 연한 회색 배경 */
  padding: 40px 0;
  margin-top: auto; /* 내용이 짧아도 바닥에 붙게 함 */
  text-align: center;
  border-top: 1px solid #eee;
}

.footer-content p {
  color: #868e96;
  font-size: 0.9rem;
  margin-bottom: 10px;
}


.portfolio-notice {
  font-size: 0.8rem;      /* 아주 작은 글씨 */
  color: #adb5bd;         /* 연한 회색 */
  margin-bottom: 8px;     /* 저작권 문구와 간격 띄우기 */
  word-break: keep-all;   /* 한글 단어 끊김 방지 */
  line-height: 1.4;
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

/* 모바일 반응형 (768px 이하) */
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