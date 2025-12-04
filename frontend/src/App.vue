<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="layout">
    <header class="app-header">
      <div class="header-container">
        <RouterLink to="/" class="logo">Chaemok.Dev</RouterLink>
        
        <nav class="nav-menu">
          <RouterLink to="/projects" class="nav-link">Projects</RouterLink>
          <RouterLink to="/about" class="nav-link">About</RouterLink>
          <RouterLink to="/contact">Contact</RouterLink>
        </nav>
      </div>
    </header>

    <main class="app-main">
      <RouterView />
    </main>

    <footer class="app-footer">
      <p>© 2025 Lee Chaemok. All rights reserved. </p>
    </footer>
  </div>
</template>

<style scoped>
/* 레이아웃 잡기 */
.layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

/* 헤더 스타일 */
.app-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background-color: rgba(255, 255, 255, 0.9); /* 살짝 투명해서 고급스러움 */
  backdrop-filter: blur(10px); /* 뒤에 내용이 흐릿하게 비침 */
  border-bottom: 1px solid #f1f1f1;
  height: 70px;
  display: flex;
  align-items: center;
}

.header-container {
  width: 100%;
  max-width: 1100px; /* HomeView 컨테이너와 너비 맞춤 */
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* 로고 스타일 */
.logo {
  font-size: 1.4rem;
  font-weight: 800;
  color: #2c3e50;
  letter-spacing: -0.5px;
}

/* 네비게이션 링크 스타일 */
.nav-menu {
  display: flex;
  gap: 30px;
}

.nav-link {
  font-size: 1rem;
  font-weight: 500;
  color: #555;
  position: relative;
}

.nav-link:hover, .router-link-active {
  color: #2c3e50;
  font-weight: 700;
}

/* 메인 컨텐츠 영역 */
.app-main {
  flex: 1; /* 푸터를 바닥으로 밀어내기 위함 */
  width: 100%;
}

/* 푸터 스타일 */
.app-footer {
  text-align: center;
  padding: 40px 0;
  font-size: 0.9rem;
  color: #999;
  border-top: 1px solid #eee;
  margin-top: auto;
}
</style>