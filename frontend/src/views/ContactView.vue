<template>
  <div class="contact-container">
    <h1>Contact Me</h1>
    <p>궁금한 점이 있거나 제안하고 싶은 내용이 있다면 연락주세요!</p>

    <form @submit.prevent="submitForm" class="contact-form">
      <div class="form-group">
        <label for="name">이름</label>
        <input type="text" id="name" v-model="form.name" required placeholder="이름을 입력하세요" />
      </div>

      <div class="form-group">
        <label for="email">이메일</label>
        <input type="email" id="email" v-model="form.email" required placeholder="답변 받을 이메일" />
      </div>

      <div class="form-group">
        <label for="subject">제목</label>
        <input type="text" id="subject" v-model="form.subject" required placeholder="제목을 입력하세요" />
      </div>

      <div class="form-group">
        <label for="message">내용</label>
        <textarea id="message" v-model="form.message" required placeholder="내용을 입력하세요" rows="5"></textarea>
      </div>

      <button type="submit" class="submit-btn">보내기</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

// 1. 입력 데이터를 담을 변수 (Reactive)
const form = ref({
  name: '',
  email: '',
  subject: '',
  message: ''
});

// 2. 폼 제출 함수
const submitForm = async () => {
  try {
    // ⚠️ 주의: 배포 후에는 이 주소를 'https://chaemok-github-io.onrender.com/api/contact/' 로 바꿔야 합니다.
    // const API_URL = 'http://127.0.0.1:8000/api/contact/'; 
    const API_URL = 'https://chaemok-githib-io.onrender.com/api/contact/';
    const response = await axios.post(API_URL, form.value);
    
    if (response.status === 201) {
      alert('메시지가 성공적으로 전송되었습니다! 🚀');
      // 폼 초기화
      form.value = { name: '', email: '', subject: '', message: '' };
    }
  } catch (error) {
    console.error('Error sending message:', error);
    alert('전송에 실패했습니다. 잠시 후 다시 시도해주세요.');
  }
};
</script>

<style scoped>
.contact-container {
  max_width: 600px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}

.contact-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  margin-top: 2rem;
  text-align: left;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

input, textarea {
  padding: 0.8rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
}

.submit-btn {
  padding: 1rem;
  background-color: #42b883; /* Vue Green */
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1.1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.submit-btn:hover {
  background-color: #3aa876;
}
</style>