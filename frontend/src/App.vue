<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="app-layout">
    <nav class="navbar">
      <div class="nav-container">
        <RouterLink to="/" class="logo">MOK</RouterLink>
        <div class="menu">
          <RouterLink to="/">Home</RouterLink>
          <RouterLink to="/about">Introduction</RouterLink> <RouterLink to="/projects">Projects</RouterLink>
        </div>

      </div>
    </nav>

    <main class="main-content">
      <RouterView />
    </main>

    <footer class="footer">
      <div class="footer-content">
        <p class="copyright">© 2025 Chaemok Lee.</p>
        <p class="tech-stack">포트폴리오용으로 제작되었으며, 상업적인 용도로 사용하지 않음을 밝힙니다.</p>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.app-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.navbar {
  position: fixed;
  top: 0; left: 0; width: 100%;
  height: 70px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid #eaeaea;
  z-index: 1000;
  display: flex;
  justify-content: center;
}

.nav-container {
  width: 100%;
  max-width: 1200px;
  padding: 0 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100%;
}

.logo { font-weight: 800; font-size: 1.5rem; color: #2c3e50; letter-spacing: -0.5px; }
.menu { display: flex; gap: 40px; }
.menu a { font-weight: 500; color: #555; font-size: 1rem; transition: color 0.3s; }
.menu a:hover, .menu a.router-link-active { color: #42b883; font-weight: 700; }

/* ✅ 여기가 핵심 수정사항입니다! */
.main-content {
  flex: 1;
  padding-top: 70px;
  width: 100%; /* 화면 꽉 채우기 */
  display: flex;     /* 내부 요소 정렬 보정 */
  flex-direction: column;
}

.footer {
  background-color: #f8f9fa;
  border-top: 1px solid #eaeaea;
  width: 100%;
  padding: 40px 0;
  margin-top: auto;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.copyright { font-weight: 600; color: #2c3e50; font-size: 1rem; }
.tech-stack { color: #888; font-size: 0.9rem; }

@media (max-width: 768px) {
  .nav-container, .footer-content { padding: 0 20px; }
  .footer-content { flex-direction: column; gap: 10px; text-align: center; }
}
</style>