<template>
  <div class="home-container">
    <!-- 导航栏 -->
    <nav class="nav-bar">
      <div class="nav-brand">
        <div class="brand-icon">
          <svg class="icon-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 00-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z" fill="currentColor"/>
          </svg>
        </div>
        <router-link to="/" class="brand-text-link">
          <span class="brand-text">Voyage<span class="brand-highlight">AI</span></span>
        </router-link>
      </div>
      <div class="nav-links">
        <router-link to="/" class="nav-link">首页</router-link>
        <router-link to="/inspiration" class="nav-link">发现灵感</router-link>
        <router-link to="/guide" class="nav-link">目的地指南</router-link>
        <router-link to="/community" class="nav-link">社区足迹</router-link>
        <router-link to="/about" class="nav-link">关于我们</router-link>
      </div>
      <div class="nav-actions">
        <button class="btn btn-outline theme-toggle" @click="toggleTheme" :title="isDark ? '切换浅色' : '切换深色'">
          <svg v-if="!isDark" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
          <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
        </button>
        <button class="btn btn-primary desktop-only">开启探索</button>
        <button class="hamburger" @click="menuOpen = !menuOpen" :class="{ active: menuOpen }">
          <span></span><span></span><span></span>
        </button>
      </div>
      <transition name="menu">
        <div class="mobile-menu" v-if="menuOpen" @click="menuOpen = false">
          <router-link to="/" class="mobile-link">首页</router-link>
          <router-link to="/inspiration" class="mobile-link">发现灵感</router-link>
          <router-link to="/guide" class="mobile-link">目的地指南</router-link>
          <router-link to="/community" class="mobile-link">社区足迹</router-link>
          <router-link to="/about" class="mobile-link">关于我们</router-link>
          <button class="btn btn-primary mobile-cta" @click="$router.push('/'); menuOpen = false">开启探索</button>
        </div>
      </transition>
    </nav>

    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-bg">
        <div class="hero-gradient"></div>
      </div>
      <div class="hero-content">
        <h1 class="hero-title serif">
          远航<span class="gradient-text">AI</span>
        </h1>
        <p class="hero-subtitle gradient-text">让每一次思考都更有方向...</p>

        <div class="search-card glass-card">
          <div class="search-fields">
            <div class="field-group">
              <label class="field-label">出发地</label>
              <div class="field-input-wrapper">
                <svg class="field-icon text-emerald" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
                <input v-model="form.start" type="text" :class="['field-input', { error: errors.start }]" placeholder="哪个城市出发？">
              </div>
              <div v-if="errors.start" class="error-message">{{ errors.start }}</div>
            </div>
            <div class="field-divider"></div>
            <div class="field-group">
              <label class="field-label">目的地</label>
              <div class="field-input-wrapper">
                <svg class="field-icon text-blue" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>
                <input v-model="form.dest" type="text" :class="['field-input', { error: errors.dest }]" placeholder="想去哪里？">
              </div>
              <div v-if="errors.dest" class="error-message">{{ errors.dest }}</div>
            </div>
            <div class="field-divider"></div>
            <div class="field-group">
              <label class="field-label">游玩天数</label>
              <div class="field-input-wrapper">
                <svg class="field-icon text-purple" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                <input v-model="form.days" type="number" :class="['field-input', { error: errors.days }]" placeholder="几天时间？" min="1" max="30">
              </div>
              <div v-if="errors.days" class="error-message">{{ errors.days }}</div>
            </div>
            <div class="field-divider"></div>
            <div class="field-group">
              <label class="field-label">预算范围</label>
              <div class="field-input-wrapper">
                <svg class="field-icon text-amber" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="5" width="20" height="14" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/></svg>
                <input v-model="form.budget" type="text" :class="['field-input', { error: errors.budget }]" placeholder="预算范围？">
              </div>
              <div v-if="errors.budget" class="error-message">{{ errors.budget }}</div>
            </div>
          </div>
          <button class="search-btn" @click="startPlanning" :disabled="loading">
            <span v-if="!loading">帮我规划</span>
            <span v-else>规划中...</span>
            <svg class="btn-icon" :class="{ rotating: loading }" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
          </button>
        </div>
      </div>
    </section>

    <!-- 功能卡片区域 -->
    <section class="features-section">
      <div class="features-grid">
        <router-link to="/inspiration" class="feature-card glass-card card-hover">
          <div class="feature-icon bg-purple-light">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
          </div>
          <h3 class="feature-title">灵感发现</h3>
          <p class="feature-desc">通过智能算法，为您的旅行提供个性化灵感建议，发现不一样的风景。</p>
          <span class="feature-btn-text">立即体验 →</span>
        </router-link>
        <router-link to="/guide" class="feature-card glass-card card-hover">
          <div class="feature-icon bg-purple-light">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 3l-.16.03L15 5.1 9 3 3.36 4.9c-.21.07-.36.25-.36.48V20.5c0 .28.22.5.5.5l.16-.03L9 18.9l6 2.1 5.64-1.9c.21-.07.36-.25.36-.48V3.5c0-.28-.22-.5-.5-.5zM15 19l-6-2.11V5l6 2.11V19z"/></svg>
          </div>
          <h3 class="feature-title">目的地指南</h3>
          <p class="feature-desc">详尽的目的地信息，深度解析当地文化、美食、景点，助您轻松规划行程。</p>
          <span class="feature-btn-text">查看指南 →</span>
        </router-link>
        <router-link to="/community" class="feature-card glass-card card-hover">
          <div class="feature-icon bg-purple-light">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
          </div>
          <h3 class="feature-title">社区足迹</h3>
          <p class="feature-desc">了解其他旅行者的足迹，分享经验，获取更多灵感和实用建议。</p>
          <span class="feature-btn-text">查看足迹 →</span>
        </router-link>
      </div>
    </section>

    <!-- 底部 -->
    <footer class="footer">
      <div class="footer-content">
        <div class="footer-brand">
          <div class="brand-header">
            <div class="brand-icon">
              <svg class="icon-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 00-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z" fill="currentColor"/>
              </svg>
            </div>
            <router-link to="/" class="brand-text-link"><span class="brand-text">Voyage<span class="brand-highlight">AI</span></span></router-link>
          </div>
          <p class="brand-desc">成立于 2026 年，我们致力于利用先进的 AI 技术为旅行者提供最纯粹的灵感发现体验。</p>
          <div class="social-links">
            <a href="#" class="social-link"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg></a>
            <a href="#" class="social-link"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></a>
          </div>
        </div>
        <div class="footer-links">
          <div class="link-group">
            <h4 class="link-title">产品</h4>
            <router-link to="/" class="footer-link">行程规划</router-link>
            <router-link to="/inspiration" class="footer-link">智能推荐</router-link>
            <router-link to="/guide" class="footer-link">预算分析</router-link>
            <router-link to="/community" class="footer-link">行前清单</router-link>
          </div>
          <div class="link-group">
            <h4 class="link-title">资源</h4>
            <router-link to="/guide" class="footer-link">目的地指南</router-link>
            <router-link to="/inspiration" class="footer-link">旅行灵感</router-link>
            <router-link to="/community" class="footer-link">社区故事</router-link>
            <router-link to="/about" class="footer-link">旅行攻略</router-link>
          </div>
          <div class="link-group">
            <h4 class="link-title">公司</h4>
            <router-link to="/about" class="footer-link">关于我们</router-link>
            <router-link to="/about" class="footer-link">联系我们</router-link>
            <router-link to="/about" class="footer-link">隐私政策</router-link>
            <router-link to="/about" class="footer-link">服务条款</router-link>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="copyright">© 2026 VoyageAI. 保留所有权利。</p>
      </div>
    </footer>

    <!-- 加载遮罩层 -->
    <transition name="fade">
      <div v-if="loading" class="loading-overlay">
        <div class="loading-content">
          <div class="loading-spinner">
            <div class="spinner-ring"></div>
            <div class="spinner-icon">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 00-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z"/></svg>
            </div>
          </div>
          <h2 class="loading-title serif">VoyageAI 正在思考...</h2>
          <p class="loading-text loader-dots">正在分析目的地实时交通与天气数据<span>.</span><span>.</span><span>.</span></p>
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
      form: { start: '南京', dest: '北京', days: 5, budget: '5000' },
      loading: false,
      loadingProgress: 0,
      isDark: false,
      menuOpen: false,
      errors: { start: '', dest: '', days: '', budget: '' }
    }
  },
  mounted() {
    const savedTheme = localStorage.getItem('theme')
    this.isDark = savedTheme ? savedTheme === 'dark' : false
    this.applyTheme()
  },
  methods: {
    toggleTheme() {
      this.isDark = !this.isDark
      this.applyTheme()
      localStorage.setItem('theme', this.isDark ? 'dark' : 'light')
    },
    applyTheme() {
      if (this.isDark) { document.documentElement.classList.add('dark-mode') }
      else { document.documentElement.classList.remove('dark-mode') }
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
        start: this.form.start, dest: this.form.dest,
        days: parseInt(this.form.days), budget: this.form.budget
      }).then(response => {
        clearInterval(interval); this.loadingProgress = 100
        setTimeout(() => { this.loading = false; const encoded = btoa(unescape(encodeURIComponent(JSON.stringify(response.data)))); this.$router.push({ name: 'Result', query: { d: encoded } }) }, 500)
      }).catch(error => {
        clearInterval(interval); this.loading = false
        console.error('生成行程失败:', error); alert('生成行程失败，请稍后重试')
      })
    }
  }
}
</script>

<style scoped>
:root {
  --bg-primary: #ffffff;
  --bg-secondary: #ffffff;
  --bg-nav: rgba(255, 255, 255, 0.95);
  --bg-card: rgba(255, 255, 255, 0.95);
  --text-primary: #1e293b;
  --text-secondary: #64748b;
  --border-color: rgba(226, 232, 240, 0.8);
  --shadow-color: rgba(0, 0, 0, 0.05);
  --primary-color: #10B981;
  --secondary-color: #3B82F6;
}
html.dark-mode {
  --bg-primary: #020617;
  --bg-secondary: #0f172a;
  --bg-nav: rgba(15, 23, 42, 0.95);
  --bg-card: rgba(30, 41, 59, 0.98);
  --text-primary: #ffffff;
  --text-secondary: #e2e8f0;
  --border-color: rgba(255, 255, 255, 0.15);
  --shadow-color: rgba(0, 0, 0, 0.3);
  --primary-color: #60a5fa;
  --secondary-color: #a78bfa;
}
.home-container { min-height: 100vh; background: var(--bg-primary); }

/* 导航栏 */
.nav-bar {
  position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
  display: flex; align-items: center; justify-content: space-between;
  padding: 1rem 2rem;
  background: var(--bg-nav); backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border-color);
  box-shadow: 0 4px 20px var(--shadow-color);
}
.nav-brand { display: flex; align-items: center; gap: 0.75rem; }
.brand-icon {
  width: 40px; height: 40px;
  background: linear-gradient(135deg, #10B981, #059669);
  border-radius: 12px; display: flex; align-items: center; justify-content: center;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}
.icon-svg { width: 24px; height: 24px; color: white; }
.brand-text-link { text-decoration: none; }
.brand-text { font-size: 1.5rem; font-weight: 700; color: var(--text-primary); letter-spacing: -0.5px; }
.brand-highlight { background: linear-gradient(135deg, #10B981, #3B82F6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }

.nav-links { display: flex; gap: 2rem; }
.nav-link {
  font-size: 0.95rem; font-weight: 500; color: var(--text-secondary);
  text-decoration: none; transition: color 0.3s; position: relative;
}
.nav-link:hover, .nav-link.router-link-exact-active { color: var(--primary-color); }
.nav-link::after {
  content: ''; position: absolute; bottom: -4px; left: 0; width: 0; height: 2px;
  background: linear-gradient(90deg, #10B981, #3B82F6); transition: width 0.3s;
}
.nav-link:hover::after, .nav-link.router-link-exact-active::after { width: 100%; }

.nav-actions { display: flex; gap: 0.75rem; }
.btn { padding: 0.6rem 1.25rem; border-radius: 9999px; font-size: 0.9rem; font-weight: 600; cursor: pointer; transition: all 0.3s; border: none; }
.btn-outline { background: transparent; border: 1.5px solid var(--border-color); color: var(--text-primary); }
.btn-outline:hover { border-color: var(--primary-color); color: var(--primary-color); background: rgba(16, 185, 129, 0.1); }
.theme-toggle { padding: 0.6rem; min-width: auto; border-radius: 50%; display: flex; align-items: center; justify-content: center; }
.theme-toggle svg { width: 20px; height: 20px; }
.btn-primary { background: linear-gradient(135deg, #10B981, #059669); color: white; box-shadow: 0 4px 14px rgba(16, 185, 129, 0.35); }
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(16, 185, 129, 0.45); }

/* Hero */
.hero-section {
  position: relative; min-height: 100vh; display: flex; align-items: center;
  justify-content: center; padding-top: 80px; overflow: hidden;
}
.hero-bg { position: absolute; inset: 0; z-index: 0; }
.hero-gradient {
  width: 100%; height: 100%;
  background: linear-gradient(135deg, #ecfdf5 0%, #dbeafe 30%, #ede9fe 60%, #fce7f3 100%);
}
html.dark-mode .hero-gradient {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
}
.hero-content { position: relative; z-index: 10; text-align: center; max-width: 900px; padding: 0 2rem; }
.hero-title {
  font-size: clamp(3.5rem, 8vw, 5.5rem); font-weight: 700; color: #1e293b;
  margin-bottom: 1.5rem; letter-spacing: -1.5px; font-family: 'Georgia', serif; line-height: 1.1;
}
html.dark-mode .hero-title { color: #fff; text-shadow: 0 4px 12px rgba(0,0,0,0.7); }
.gradient-text { background: linear-gradient(135deg, #10B981, #059669); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
html.dark-mode .gradient-text { background: linear-gradient(135deg, #6ee7b7, #60a5fa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.hero-subtitle { font-size: clamp(1.4rem, 3vw, 1.8rem); font-weight: 700; color: #10B981; margin-bottom: 3rem; opacity: 0.9; font-family: 'Georgia', serif; }
html.dark-mode .hero-subtitle { color: #a7f3d0; text-shadow: 0 2px 8px rgba(0,0,0,0.6); }

/* 表单 */
.search-card {
  padding: 1.5rem 2rem; border-radius: 2rem; max-width: 850px; margin: 0 auto;
  background: var(--bg-card); backdrop-filter: blur(20px);
  border: 1px solid var(--border-color); box-shadow: 0 8px 32px var(--shadow-color);
}
.search-fields { display: flex; align-items: stretch; gap: 0; margin-bottom: 1.25rem; }
.field-group { flex: 1; padding: 0 1rem; text-align: left; }
.field-group:first-child { padding-left: 0; }
.field-group:last-child { padding-right: 0; }
.field-label { display: block; font-size: 0.65rem; font-weight: 700; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 0.5rem; }
.field-input-wrapper { display: flex; align-items: center; gap: 0.5rem; }
.field-icon { width: 18px; height: 18px; flex-shrink: 0; }
.text-emerald { color: #10B981; } .text-blue { color: #3B82F6; } .text-purple { color: #8B5CF6; } .text-amber { color: #F59E0B; }
html.dark-mode .text-emerald { color: #6ee7b7; } html.dark-mode .text-blue { color: #60a5fa; } html.dark-mode .text-purple { color: #a78bfa; } html.dark-mode .text-amber { color: #fbbf24; }
.field-input { width: 100%; border: none; background: transparent; font-size: 1rem; font-weight: 500; color: var(--text-primary); padding: 0.25rem 0; outline: none; }
.field-input::placeholder { color: var(--text-secondary); }
.field-input.error { border-bottom: 2px solid #ef4444; }
.error-message { font-size: 0.75rem; color: #ef4444; margin-top: 0.25rem; text-align: left; }
.field-divider { width: 1px; background: linear-gradient(to bottom, transparent, var(--border-color), transparent); align-self: stretch; }
.search-btn {
  width: 100%; padding: 1rem 2rem;
  background: linear-gradient(135deg, #10B981, #059669); color: white; border: none; border-radius: 9999px;
  font-size: 1.1rem; font-weight: 600; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 0.5rem;
  box-shadow: 0 4px 16px rgba(16, 185, 129, 0.35); transition: all 0.3s;
}
.search-btn:hover:not(:disabled) { transform: translateY(-2px); box-shadow: 0 6px 24px rgba(16, 185, 129, 0.45); }
.search-btn:disabled { opacity: 0.7; cursor: not-allowed; }
.btn-icon { width: 20px; height: 20px; transition: transform 0.3s; }
.btn-icon.rotating { animation: spin 1s linear infinite; }
@keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

/* 功能卡片 */
.features-section { padding: 6rem 2rem; max-width: 1200px; margin: 0 auto; }
.features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }
.feature-card {
  padding: 2.5rem; border-radius: 1.5rem; text-align: left; text-decoration: none; color: inherit;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  background: var(--bg-card); border: 1px solid var(--border-color);
}
.feature-card:hover { transform: translateY(-8px); box-shadow: 0 20px 40px -10px var(--shadow-color); }
.feature-icon { width: 56px; height: 56px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; }
.feature-icon svg { width: 28px; height: 28px; color: white; }
.bg-emerald-light { background: linear-gradient(135deg, var(--primary-color), #34D399); }
.bg-blue-light { background: linear-gradient(135deg, var(--secondary-color), #60A5FA); }
.bg-purple-light { background: linear-gradient(135deg, #8B5CF6, #A78BFA); }
.feature-title { font-size: 1.5rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.75rem; }
.feature-desc { font-size: 0.95rem; color: var(--text-secondary); line-height: 1.7; margin-bottom: 1.5rem; }
.feature-btn-text { color: var(--primary-color); font-weight: 600; font-size: 0.9rem; }

/* 加载 */
.loading-overlay {
  position: fixed; inset: 0; z-index: 9999;
  background: var(--bg-nav); backdrop-filter: blur(10px);
  display: flex; align-items: center; justify-content: center;
}
.loading-content { text-align: center; }
.loading-spinner { position: relative; width: 120px; height: 120px; margin: 0 auto 2rem; }
.spinner-ring { position: absolute; inset: 0; border: 4px solid var(--border-color); border-top-color: #10B981; border-radius: 50%; animation: spin 1s linear infinite; }
.spinner-icon { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; color: #10B981; animation: pulse 2s ease-in-out infinite; }
.spinner-icon svg { width: 48px; height: 48px; }
@keyframes pulse { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.7; transform: scale(0.95); } }
.loading-title { font-size: 1.75rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.75rem; font-family: 'Georgia', serif; }
.loading-text { font-size: 1rem; color: var(--text-secondary); margin-bottom: 2rem; }
.loading-progress { width: 300px; height: 4px; background: var(--border-color); border-radius: 2px; overflow: hidden; margin: 0 auto; }
.progress-bar { height: 100%; background: linear-gradient(90deg, #10B981, #3B82F6); border-radius: 2px; transition: width 0.3s; }
.fade-enter-active, .fade-leave-active { transition: opacity 0.3s; }
.fade-enter-from, .fade-leave-to { opacity: 0; }

/* 底部 */
.footer { background: var(--bg-secondary); padding: 4rem 2rem 2rem; border-top: 1px solid var(--border-color); }
.footer-content { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 3fr; gap: 4rem; align-items: start; }
.footer-brand { display: flex; flex-direction: column; gap: 1rem; }
.brand-header { display: flex; align-items: center; gap: 1rem; }
.brand-desc { color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6; max-width: 300px; }
.social-links { display: flex; gap: 1rem; margin-top: 0.5rem; }
.social-link { width: 40px; height: 40px; border-radius: 50%; background: var(--bg-primary); display: flex; align-items: center; justify-content: center; color: var(--text-secondary); text-decoration: none; transition: all 0.3s; box-shadow: 0 2px 8px var(--shadow-color); }
.social-link:hover { transform: translateY(-4px); color: var(--primary-color); box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3); }
.social-link svg { width: 20px; height: 20px; }
.footer-links { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; }
.link-group { display: flex; flex-direction: column; gap: 1rem; }
.link-title { font-size: 1.1rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.5rem; }
.footer-link { color: var(--text-secondary); text-decoration: none; font-size: 0.95rem; transition: all 0.3s; display: block; }
.footer-link:hover { color: var(--primary-color); transform: translateX(4px); }
.footer-bottom { max-width: 1200px; margin: 3rem auto 0; padding-top: 2rem; border-top: 1px solid var(--border-color); text-align: center; }
.copyright { color: var(--text-secondary); font-size: 0.9rem; }

@media (max-width: 768px) {
  .nav-links { display: none; }
  .desktop-only { display: none; }
  .hamburger { display: flex; }
  .mobile-menu { display: flex; flex-direction: column; padding: 1rem 1.5rem; background: var(--bg-nav); backdrop-filter: blur(20px); border-top: 1px solid var(--border-color); }
  .mobile-link { padding: 0.8rem 0; font-size: 1rem; font-weight: 500; color: var(--text-primary); text-decoration: none; border-bottom: 1px solid var(--border-color); }
  .mobile-link:hover { color: var(--primary-color); }
  .mobile-cta { margin-top: 1rem; width: 100%; justify-content: center; }
  .menu-enter-active, .menu-leave-active { transition: all 0.3s ease; max-height: 400px; overflow: hidden; }
  .menu-enter-from, .menu-leave-to { max-height: 0; opacity: 0; }
  .search-fields { flex-direction: column; gap: 1rem; }
  .field-divider { display: none; }
  .field-group { padding: 0; }
  .features-section { padding: 4rem 1rem; }
  .footer-content { grid-template-columns: 1fr; gap: 2rem; }
  .footer-links { grid-template-columns: repeat(2, 1fr); gap: 1.5rem; }
}
.hamburger { display: none; flex-direction: column; gap: 5px; padding: 0.5rem; cursor: pointer; background: none; border: none; }
.hamburger span { display: block; width: 22px; height: 2px; background: var(--text-primary); border-radius: 2px; transition: all 0.3s; }
.hamburger.active span:nth-child(1) { transform: rotate(45deg) translate(5px, 5px); }
.hamburger.active span:nth-child(2) { opacity: 0; }
.hamburger.active span:nth-child(3) { transform: rotate(-45deg) translate(5px, -5px); }
.mobile-menu { display: none; }
</style>
