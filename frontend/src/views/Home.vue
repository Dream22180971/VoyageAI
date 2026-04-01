<template>
  <div class="home-container" :class="{ 'light-mode': !isDark }">
    <!-- 导航栏 -->
    <nav class="navbar">
      <div class="nav-container">
        <router-link to="/" class="nav-logo">
          <span class="logo-icon">🗺️</span>
          <span class="logo-text">VoyageAI</span>
        </router-link>
        <div class="nav-links">
          <router-link to="/" class="nav-link active">首页</router-link>
          <router-link to="/inspiration" class="nav-link">灵感发现</router-link>
          <router-link to="/guide" class="nav-link">目的地指南</router-link>
          <router-link to="/community" class="nav-link">社区足迹</router-link>
          <router-link to="/about" class="nav-link">关于我们</router-link>
        </div>
        <button class="theme-toggle" @click="toggleTheme" :title="isDark ? '切换浅色' : '切换深色'">
          <span v-if="isDark">🌙</span>
          <span v-else>☀️</span>
        </button>
      </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-content">
        <h1 class="hero-title">
          <span class="gradient-text">Voyage</span><span class="gradient-text-alt">AI</span>
        </h1>
        <p class="hero-subtitle">AI 驱动的智能旅行规划，让每一次出发都充满期待</p>

        <!-- 表单区域 -->
        <div class="form-card">
          <div class="form-fields">
            <div class="field-group">
              <label class="field-label">📍 出发地</label>
              <input
                v-model="form.start"
                type="text"
                class="field-input"
                :class="{ error: errors.start }"
                placeholder="哪个城市出发？"
              >
              <span v-if="errors.start" class="error-msg">{{ errors.start }}</span>
            </div>

            <div class="field-group">
              <label class="field-label">🌏 目的地</label>
              <input
                v-model="form.dest"
                type="text"
                class="field-input"
                :class="{ error: errors.dest }"
                placeholder="想去哪里？"
              >
              <span v-if="errors.dest" class="error-msg">{{ errors.dest }}</span>
            </div>

            <div class="field-group">
              <label class="field-label">📅 天数</label>
              <input
                v-model="form.days"
                type="number"
                class="field-input"
                :class="{ error: errors.days }"
                placeholder="几天？"
                min="1" max="30"
              >
              <span v-if="errors.days" class="error-msg">{{ errors.days }}</span>
            </div>

            <div class="field-group">
              <label class="field-label">💰 预算</label>
              <input
                v-model="form.budget"
                type="text"
                class="field-input"
                :class="{ error: errors.budget }"
                placeholder="预算范围？"
              >
              <span v-if="errors.budget" class="error-msg">{{ errors.budget }}</span>
            </div>
          </div>

          <button class="plan-btn" @click="startPlanning" :disabled="loading">
            <span v-if="!loading">🤖 AI 帮我规划</span>
            <span v-else>✨ 规划中...</span>
          </button>
        </div>
      </div>
    </section>

    <!-- 功能卡片 -->
    <section class="features">
      <div class="container">
        <h2 class="section-title">✨ 探索 VoyageAI</h2>
        <div class="features-grid">
          <router-link to="/inspiration" class="feature-card">
            <div class="feature-emoji">💭</div>
            <h3>灵感发现</h3>
            <p>不知道去哪？让 AI 为你推荐个性化旅行灵感</p>
            <span class="feature-arrow">→</span>
          </router-link>
          <router-link to="/guide" class="feature-card">
            <div class="feature-emoji">📖</div>
            <h3>目的地指南</h3>
            <p>深度解析当地文化、美食、景点，出行前必看</p>
            <span class="feature-arrow">→</span>
          </router-link>
          <router-link to="/community" class="feature-card">
            <div class="feature-emoji">🌏</div>
            <h3>社区足迹</h3>
            <p>看旅行者们的故事，获取真实实用的旅行建议</p>
            <span class="feature-arrow">→</span>
          </router-link>
        </div>
      </div>
    </section>

    <!-- 数据统计 -->
    <section class="stats-section">
      <div class="container">
        <div class="stats-bar">
          <div class="stat">
            <div class="stat-num">12,847+</div>
            <div class="stat-label">旅行者</div>
          </div>
          <div class="stat">
            <div class="stat-num">38,291+</div>
            <div class="stat-label">行程方案</div>
          </div>
          <div class="stat">
            <div class="stat-num">218+</div>
            <div class="stat-label">覆盖城市</div>
          </div>
          <div class="stat">
            <div class="stat-num">99.2%</div>
            <div class="stat-label">满意度</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 底部 -->
    <footer class="footer">
      <div class="container">
        <div class="footer-content">
          <div class="footer-brand">
            <router-link to="/" class="nav-logo">
              <span class="logo-icon">🗺️</span>
              <span class="logo-text">VoyageAI</span>
            </router-link>
            <p class="footer-desc">AI 驱动的智能旅行规划系统，让旅行变得简单、高效且充满惊喜。</p>
          </div>
          <div class="footer-links">
            <div class="link-group">
              <h4>产品</h4>
              <router-link to="/">行程规划</router-link>
              <router-link to="/inspiration">智能推荐</router-link>
              <router-link to="/guide">目的地指南</router-link>
              <router-link to="/about">关于我们</router-link>
            </div>
            <div class="link-group">
              <h4>社区</h4>
              <router-link to="/community">旅行故事</router-link>
              <router-link to="/inspiration">灵感发现</router-link>
              <router-link to="/guide">旅行攻略</router-link>
              <router-link to="/about">联系我们</router-link>
            </div>
          </div>
        </div>
        <div class="footer-bottom">
          <p>© 2026 VoyageAI — 智能旅行规划系统</p>
        </div>
      </div>
    </footer>

    <!-- 加载遮罩 -->
    <transition name="fade">
      <div v-if="loading" class="loading-overlay">
        <div class="loading-content">
          <div class="loading-spinner">
            <div class="spinner-ring"></div>
            <div class="spinner-center">🗺️</div>
          </div>
          <h2 class="loading-title">VoyageAI 正在思考...</h2>
          <p class="loading-text">正在分析目的地与天气数据<span class="dots">...</span></p>
          <div class="loading-progress">
            <div class="progress-bar" :style="{ width: loadingProgress + '%' }"></div>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      form: {
        start: '南京',
        dest: '北京',
        days: 5,
        budget: '5000'
      },
      loading: false,
      loadingProgress: 0,
      isDark: true,
      errors: {
        start: '',
        dest: '',
        days: '',
        budget: ''
      }
    }
  },
  mounted() {
    const savedTheme = localStorage.getItem('theme')
    this.isDark = savedTheme ? savedTheme === 'dark' : true
    this.applyTheme()
  },
  methods: {
    toggleTheme() {
      this.isDark = !this.isDark
      this.applyTheme()
      localStorage.setItem('theme', this.isDark ? 'dark' : 'light')
    },
    applyTheme() {
      if (this.isDark) {
        document.documentElement.classList.add('dark-mode')
      } else {
        document.documentElement.classList.remove('dark-mode')
      }
    },
    validateForm() {
      let isValid = true
      this.errors = { start: '', dest: '', days: '', budget: '' }
      if (!this.form.start || !this.form.start.trim()) { this.errors.start = '请输入出发地'; isValid = false }
      if (!this.form.dest || !this.form.dest.trim()) { this.errors.dest = '请输入目的地'; isValid = false }
      if (!this.form.days) { this.errors.days = '请输入天数'; isValid = false }
      else if (this.form.days < 1) { this.errors.days = '至少1天'; isValid = false }
      else if (this.form.days > 30) { this.errors.days = '最多30天'; isValid = false }
      if (!this.form.budget || !this.form.budget.trim()) { this.errors.budget = '请输入预算'; isValid = false }
      else if (!/^\d+(-\d+)?(\+)?$/.test(this.form.budget.replace(/,/g, ''))) { this.errors.budget = '格式如: 5000-8000'; isValid = false }
      return isValid
    },
    startPlanning() {
      if (!this.validateForm()) return
      this.loading = true
      this.loadingProgress = 0
      const interval = setInterval(() => {
        this.loadingProgress += Math.random() * 15
        if (this.loadingProgress >= 95) { this.loadingProgress = 95; clearInterval(interval) }
      }, 300)
      axios.post('/api/plan', {
        start: this.form.start,
        dest: this.form.dest,
        days: parseInt(this.form.days),
        budget: this.form.budget
      })
      .then(response => {
        clearInterval(interval)
        this.loadingProgress = 100
        setTimeout(() => {
          this.loading = false
          this.$router.push({ name: 'Result', query: { data: JSON.stringify(response.data) } })
        }, 500)
      })
      .catch(error => {
        clearInterval(interval)
        this.loading = false
        console.error('生成行程失败:', error)
        alert('生成行程失败，请稍后重试')
      })
    }
  }
}
</script>

<style scoped>
/* 深色主题（默认） */
.home-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #0f0c29 0%, #1a1a3e 50%, #24243e 100%);
  color: #e0e0e0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  transition: background 0.4s, color 0.4s;
}

/* 浅色主题 */
.home-container.light-mode {
  background: linear-gradient(135deg, #f5f7fa 0%, #e8ecf1 50%, #dde3ec 100%);
  color: #2d3748;
}

/* 导航栏 */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  background: rgba(15, 12, 41, 0.85);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  transition: background 0.4s, border-color 0.4s;
}

.light-mode .navbar {
  background: rgba(255, 255, 255, 0.85);
  border-bottom-color: rgba(0, 0, 0, 0.08);
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0.8rem 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  text-decoration: none;
  font-size: 1.3rem;
  font-weight: 700;
}

.logo-icon { font-size: 1.5rem; }

.logo-text {
  background: linear-gradient(135deg, #667eea, #764ba2);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.nav-links {
  display: flex;
  gap: 1.5rem;
}

.nav-link {
  color: #b0b0b0;
  text-decoration: none;
  font-size: 0.9rem;
  transition: color 0.3s;
}

.nav-link:hover,
.nav-link.active {
  color: #667eea;
}

.light-mode .nav-link {
  color: #718096;
}

.light-mode .nav-link:hover,
.light-mode .nav-link.active {
  color: #667eea;
}

.theme-toggle {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 1rem;
  transition: all 0.3s;
}

.theme-toggle:hover {
  background: rgba(255, 255, 255, 0.15);
  transform: rotate(20deg);
}

.light-mode .theme-toggle {
  background: rgba(0, 0, 0, 0.05);
  border-color: rgba(0, 0, 0, 0.1);
}

/* Hero */
.hero {
  padding: 9rem 2rem 4rem;
  text-align: center;
}

.hero-content {
  max-width: 800px;
  margin: 0 auto;
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 800;
  margin-bottom: 1rem;
  letter-spacing: -1px;
}

.gradient-text {
  background: linear-gradient(135deg, #667eea, #764ba2);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.gradient-text-alt {
  background: linear-gradient(135deg, #f093fb, #f5576c);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.light-mode .gradient-text {
  background: linear-gradient(135deg, #5a67d8, #6b46c1);
}

.light-mode .gradient-text-alt {
  background: linear-gradient(135deg, #ed64a6, #e53e3e);
}

.hero-subtitle {
  font-size: 1.15rem;
  color: #a0a0a0;
  margin-bottom: 2.5rem;
  line-height: 1.6;
}

.light-mode .hero-subtitle {
  color: #718096;
}

/* 表单 */
.form-card {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 20px;
  padding: 2rem;
  backdrop-filter: blur(10px);
  transition: all 0.4s;
}

.light-mode .form-card {
  background: rgba(255, 255, 255, 0.8);
  border-color: rgba(0, 0, 0, 0.08);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
}

.form-fields {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.field-group {
  text-align: left;
}

.field-label {
  display: block;
  font-size: 0.8rem;
  color: #909090;
  margin-bottom: 0.4rem;
  font-weight: 500;
}

.light-mode .field-label {
  color: #718096;
}

.field-input {
  width: 100%;
  padding: 0.7rem 0.8rem;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  color: #e0e0e0;
  font-size: 0.95rem;
  outline: none;
  transition: all 0.3s;
  box-sizing: border-box;
}

.field-input:focus {
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.15);
}

.field-input::placeholder {
  color: #555;
}

.field-input.error {
  border-color: #f56565;
}

.light-mode .field-input {
  background: rgba(0, 0, 0, 0.03);
  border-color: rgba(0, 0, 0, 0.12);
  color: #2d3748;
}

.light-mode .field-input::placeholder {
  color: #a0aec0;
}

.error-msg {
  display: block;
  font-size: 0.75rem;
  color: #f56565;
  margin-top: 0.3rem;
}

.plan-btn {
  width: 100%;
  padding: 0.9rem;
  border: none;
  border-radius: 14px;
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: #fff;
  font-size: 1.05rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.plan-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
}

.plan-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

/* 功能卡片 */
.features {
  padding: 4rem 2rem;
}

.container {
  max-width: 1000px;
  margin: 0 auto;
}

.section-title {
  font-size: 1.8rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 2rem;
  color: #fff;
}

.light-mode .section-title {
  color: #2d3748;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.feature-card {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 16px;
  padding: 2rem;
  text-align: center;
  text-decoration: none;
  color: inherit;
  transition: all 0.3s;
  position: relative;
}

.feature-card:hover {
  transform: translateY(-4px);
  background: rgba(255, 255, 255, 0.07);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.2);
}

.light-mode .feature-card {
  background: rgba(255, 255, 255, 0.7);
  border-color: rgba(0, 0, 0, 0.06);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
}

.light-mode .feature-card:hover {
  background: rgba(255, 255, 255, 0.9);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.1);
}

.feature-emoji {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.feature-card h3 {
  color: #fff;
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
}

.light-mode .feature-card h3 {
  color: #2d3748;
}

.feature-card p {
  color: #909090;
  font-size: 0.85rem;
  line-height: 1.6;
}

.light-mode .feature-card p {
  color: #718096;
}

.feature-arrow {
  display: inline-block;
  margin-top: 1rem;
  color: #667eea;
  font-size: 1.2rem;
  transition: transform 0.3s;
}

.feature-card:hover .feature-arrow {
  transform: translateX(4px);
}

/* 统计 */
.stats-section {
  padding: 3rem 2rem;
}

.stats-bar {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 16px;
  padding: 2rem;
}

.light-mode .stats-bar {
  background: rgba(255, 255, 255, 0.6);
  border-color: rgba(0, 0, 0, 0.06);
}

.stat {
  text-align: center;
}

.stat-num {
  font-size: 1.5rem;
  font-weight: 800;
  background: linear-gradient(135deg, #667eea, #f093fb);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.stat-label {
  font-size: 0.8rem;
  color: #888;
  margin-top: 0.3rem;
}

.light-mode .stat-label {
  color: #a0aec0;
}

/* 底部 */
.footer {
  padding: 3rem 2rem 2rem;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
}

.light-mode .footer {
  border-top-color: rgba(0, 0, 0, 0.06);
}

.footer-content {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 3rem;
  margin-bottom: 2rem;
}

.footer-brand {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.footer-desc {
  color: #909090;
  font-size: 0.9rem;
  line-height: 1.6;
  max-width: 300px;
}

.light-mode .footer-desc {
  color: #718096;
}

.footer-links {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

.link-group h4 {
  color: #d0d0d0;
  font-size: 1rem;
  margin-bottom: 0.8rem;
}

.light-mode .link-group h4 {
  color: #4a5568;
}

.link-group a {
  display: block;
  color: #888;
  text-decoration: none;
  font-size: 0.9rem;
  padding: 0.3rem 0;
  transition: color 0.3s;
}

.link-group a:hover {
  color: #667eea;
}

.light-mode .link-group a {
  color: #a0aec0;
}

.footer-bottom {
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  padding-top: 1.5rem;
  text-align: center;
}

.light-mode .footer-bottom {
  border-top-color: rgba(0, 0, 0, 0.06);
}

.footer-bottom p {
  color: #555;
  font-size: 0.85rem;
}

.light-mode .footer-bottom p {
  color: #a0aec0;
}

/* 加载遮罩 */
.loading-overlay {
  position: fixed;
  inset: 0;
  z-index: 9999;
  background: linear-gradient(135deg, #0f0c29 0%, #1a1a3e 50%, #24243e 100%);
  display: flex;
  align-items: center;
  justify-content: center;
}

.light-mode .loading-overlay {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
}

.loading-content {
  text-align: center;
}

.loading-spinner {
  position: relative;
  width: 100px;
  height: 100px;
  margin: 0 auto 2rem;
}

.spinner-ring {
  position: absolute;
  inset: 0;
  border: 3px solid rgba(102, 126, 234, 0.2);
  border-top-color: #667eea;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.spinner-center {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  animation: pulse 2s ease-in-out infinite;
}

.loading-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #fff;
  margin-bottom: 0.5rem;
}

.light-mode .loading-title {
  color: #2d3748;
}

.loading-text {
  color: #a0a0a0;
  margin-bottom: 2rem;
}

.light-mode .loading-text {
  color: #718096;
}

.loading-progress {
  width: 280px;
  height: 4px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 2px;
  overflow: hidden;
  margin: 0 auto;
}

.light-mode .loading-progress {
  background: rgba(0, 0, 0, 0.08);
}

.progress-bar {
  height: 100%;
  background: linear-gradient(90deg, #667eea, #f093fb);
  border-radius: 2px;
  transition: width 0.3s;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(0.9); }
}

.fade-enter-active, .fade-leave-active { transition: opacity 0.3s; }
.fade-enter-from, .fade-leave-to { opacity: 0; }

/* 响应式 */
@media (max-width: 768px) {
  .hero-title { font-size: 2.2rem; }
  .hero { padding: 7rem 1.5rem 3rem; }
  .form-fields { grid-template-columns: 1fr 1fr; }
  .features-grid { grid-template-columns: 1fr; }
  .stats-bar { grid-template-columns: 1fr 1fr; }
  .nav-links { gap: 0.8rem; }
  .nav-link { font-size: 0.78rem; }
  .footer-content { grid-template-columns: 1fr; gap: 2rem; }
}

@media (max-width: 480px) {
  .form-fields { grid-template-columns: 1fr; }
}
</style>
