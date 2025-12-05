<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'

// 1. 메뉴가 열렸는지 닫혔는지 상태를 저장하는 변수
const isMenuOpen = ref(false)

// 2. 햄버거 버튼 누르면 열렸다 닫혔다 하는 함수
const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

// 3. 메뉴 클릭하면 닫히게 하는 함수 (모바일에서 이동 후 메뉴 닫기 위함)
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
        <RouterLink to="/projects">Projects</RouterLink>
        <RouterLink to="/contact">Contact</RouterLink>
      </nav>

      <button class="hamburger-btn" @click="toggleMenu">
        ☰
      </button>
    </div>

    <nav class="mobile-nav" :class="{ 'open': isMenuOpen }">
      <RouterLink to="/" @click="closeMenu">Home</RouterLink>
      <RouterLink to="/projects" @click="closeMenu">Projects</RouterLink>
      <RouterLink to="/contact" @click="closeMenu">Contact</RouterLink>
    </nav>
  </header>

  <RouterView />
</template>

<style scoped>
/* 헤더 전체 레이아웃 */
header {
  background-color: white;
  border-bottom: 1px solid #eee;
  position: sticky; /* 스크롤 내려도 상단 고정 */
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
  justify-content: space-between; /* 로고와 메뉴 양끝 정렬 */
}

.logo a {
  font-size: 1.5rem;
  font-weight: 800;
  color: #212529;
  text-decoration: none;
}

/* 데스크탑 메뉴 스타일 */
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

/* 햄버거 버튼 (기본적으로 숨김) */
.hamburger-btn {
  display: none; /* PC에서는 안 보임 */
  background: none;
  border: none;
  font-size: 1.8rem;
  cursor: pointer;
  color: #333;
}

/* 모바일 메뉴 박스 (기본적으로 숨김 + 디자인) */
.mobile-nav {
  display: none; /* 평소엔 숨김 */
  background-color: white;
  border-bottom: 1px solid #eee;
  flex-direction: column;
  padding: 10px 0;
}

.mobile-nav a {
  display: block; /* 한 줄에 하나씩 */
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

/* =========================================
   📱 반응형 (768px 이하 모바일 화면)
   ========================================= */
@media (max-width: 768px) {
  /* 데스크탑 메뉴 숨기기 */
  .desktop-nav {
    display: none;
  }

  /* 햄버거 버튼 보이기 */
  .hamburger-btn {
    display: block;
  }

  /* 모바일 메뉴가 'open' 클래스를 가지면 보이기 */
  .mobile-nav.open {
    display: flex; /* 열리면 보임 */
  }
}
</style>