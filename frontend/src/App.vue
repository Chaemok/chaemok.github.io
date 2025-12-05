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
  <header>
    <div class="wrapper">
      <div class="logo">
        <RouterLink to="/" @click="closeMenu">Chaemok.Dev</RouterLink>
      </div>

      <nav class="desktop-nav">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink> <RouterLink to="/projects">Projects</RouterLink>
        <RouterLink to="/contact">Contact</RouterLink>
      </nav>

      <button class="hamburger-btn" @click="toggleMenu">
        ☰
      </button>
    </div>

    <nav class="mobile-nav" :class="{ 'open': isMenuOpen }">
      <RouterLink to="/" @click="closeMenu">Home</RouterLink>
      <RouterLink to="/about" @click="closeMenu">About</RouterLink> <RouterLink to="/projects" @click="closeMenu">Projects</RouterLink>
      <RouterLink to="/contact" @click="closeMenu">Contact</RouterLink>
    </nav>
  </header>

  <RouterView />
</template>

<style scoped>
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