<template>
  <div class="home-container">
    <!-- 导航栏 -->
    <nav class="nav-bar">
      <div class="nav-brand">
        <div class="brand-icon">
          <svg class="icon-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/>
            <ellipse cx="12" cy="12" rx="4" ry="10" stroke="currentColor" stroke-width="2"/>
            <path d="M2 12H22" stroke="currentColor" stroke-width="2"/>
          </svg>
        </div>
        <span class="brand-text">Voyage<span class="brand-highlight">AI</span></span>
      </div>
      
      <div class="nav-links">
        <router-link to="/inspiration" class="nav-link">发现灵感</router-link>
        <router-link to="/guide" class="nav-link">目的地指南</router-link>
        <router-link to="/community" class="nav-link">社区足迹</router-link>
        <router-link to="/about" class="nav-link">关于我们</router-link>
      </div>
      
      <div class="nav-actions">
        <button 
          class="btn btn-outline theme-toggle"
          @click="toggleTheme"
          title="切换主题"
        >
          <svg v-if="!isDark" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
          </svg>
          <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/>
          </svg>
        </button>
        <button class="btn btn-outline">登录</button>
        <button class="btn btn-primary">开启探索</button>
      </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-bg">
        <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=light%20blue%20gradient%20ocean%20waves%20background%2C%20soft%20clouds%2C%20serene%20sea%20view%2C%20peaceful%20atmosphere%2C%20pastel%20colors%2C%20high%20quality&image_size=landscape_16_9" alt="远航背景" class="hero-bg-img">
        <div class="hero-overlay"></div>
      </div>
      
      <div class="hero-content">
        <h1 class="hero-title serif">
          远航<span class="gradient-text">AI</span>
        </h1>
        <p class="hero-subtitle gradient-text">
          让每一次思考都更有方向...
        </p>
        
        <!-- 智能输入区域 -->
        <div class="search-card glass-card">
          <div class="search-fields">
            <div class="field-group">
              <label class="field-label">出发地</label>
              <div class="field-input-wrapper">
                <svg class="field-icon text-emerald" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/>
                  <circle cx="12" cy="10" r="3"/>
                </svg>
                <input 
                  v-model="form.start" 
                  type="text" 
                  :class="['field-input', { 'error': errors.start }]" 
                  placeholder="哪个城市出发？"
                >
              </div>
              <div v-if="errors.start" class="error-message">{{ errors.start }}</div>
            </div>
            
            <div class="field-divider"></div>
            
            <div class="field-group">
              <label class="field-label">目的地</label>
              <div class="field-input-wrapper">
                <svg class="field-icon text-blue" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="12" cy="12" r="10"/>
                  <polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/>
                </svg>
                <input 
                  v-model="form.dest" 
                  type="text" 
                  :class="['field-input', { 'error': errors.dest }]" 
                  placeholder="想去哪里？"
                >
              </div>
              <div v-if="errors.dest" class="error-message">{{ errors.dest }}</div>
            </div>
            
            <div class="field-divider"></div>
            
            <div class="field-group">
              <label class="field-label">游玩天数</label>
              <div class="field-input-wrapper">
                <svg class="field-icon text-purple" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                  <line x1="16" y1="2" x2="16" y2="6"/>
                  <line x1="8" y1="2" x2="8" y2="6"/>
                  <line x1="3" y1="10" x2="21" y2="10"/>
                </svg>
                <input 
                  v-model="form.days" 
                  type="number" 
                  :class="['field-input', { 'error': errors.days }]" 
                  placeholder="几天时间？"
                  min="1"
                  max="30"
                >
              </div>
              <div v-if="errors.days" class="error-message">{{ errors.days }}</div>
            </div>
            
            <div class="field-divider"></div>
            
            <div class="field-group">
              <label class="field-label">预算范围</label>
              <div class="field-input-wrapper">
                <svg class="field-icon text-amber" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="2" y="5" width="20" height="14" rx="2"/>
                  <line x1="2" y1="10" x2="22" y2="10"/>
                </svg>
                <input 
                  v-model="form.budget" 
                  type="text" 
                  :class="['field-input', { 'error': errors.budget }]" 
                  placeholder="预算范围？"
                >
              </div>
              <div v-if="errors.budget" class="error-message">{{ errors.budget }}</div>
            </div>
          </div>
          
          <button 
            class="search-btn"
            @click="startPlanning"
            :disabled="loading"
          >
            <span v-if="!loading">帮我规划</span>
            <span v-else>规划中...</span>
            <svg class="btn-icon" :class="{ 'rotating': loading }" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M12 20h9M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>
            </svg>
          </button>
        </div>
      </div>
      
      <!-- 装饰元素 -->
      <div class="floating-icon icon-plane">
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M21 16v-2l-8-5V3.5c0-.83-.67-1.5-1.5-1.5S10 2.67 10 3.5V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z"/>
        </svg>
      </div>
      <div class="floating-icon icon-sparkle">
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 2L14.09 8.26L21 9.27L16 14.14L17.18 21.02L12 17.77L6.82 21.02L8 14.14L3 9.27L9.91 8.26L12 2Z"/>
        </svg>
      </div>
    </section>

    <!-- 功能卡片区域 -->
    <section class="features-section">
      <div class="features-grid">
        <div class="feature-card glass-card card-hover">
          <div class="feature-icon bg-emerald-light">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
            </svg>
          </div>
          <h3 class="feature-title">灵感发现</h3>
          <p class="feature-desc">通过智能算法，为您的旅行提供个性化灵感建议，发现不一样的风景。</p>
          <button class="feature-btn">
            立即体验
            <svg class="btn-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="5" y1="12" x2="19" y2="12"/>
              <polyline points="12 5 19 12 12 19"/>
            </svg>
          </button>
        </div>
        
        <div class="feature-card glass-card card-hover">
          <div class="feature-icon bg-blue-light">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10"/>
              <polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/>
            </svg>
          </div>
          <h3 class="feature-title">目的地指南</h3>
          <p class="feature-desc">详尽的目的地信息，深度解析当地文化、美食、景点，助您轻松规划行程。</p>
          <button class="feature-btn">
            查看指南
            <svg class="btn-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="5" y1="12" x2="19" y2="12"/>
              <polyline points="12 5 19 12 12 19"/>
            </svg>
          </button>
        </div>
        
        <div class="feature-card glass-card card-hover">
          <div class="feature-icon bg-purple-light">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/>
              <circle cx="9" cy="7" r="4"/>
              <path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/>
            </svg>
          </div>
          <h3 class="feature-title">社区足迹</h3>
          <p class="feature-desc">了解其他旅行者的足迹，分享经验，获取更多灵感和实用建议。</p>
          <button class="feature-btn">
            查看足迹
            <svg class="btn-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="5" y1="12" x2="19" y2="12"/>
              <polyline points="12 5 19 12 12 19"/>
            </svg>
          </button>
        </div>
      </div>
    </section>

    <!-- 底部导航栏 -->
    <footer class="footer">
      <div class="footer-content">
        <div class="footer-brand">
          <div class="brand-header">
            <div class="brand-icon">
              <svg class="icon-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/>
                <ellipse cx="12" cy="12" rx="4" ry="10" stroke="currentColor" stroke-width="2"/>
                <path d="M2 12H22" stroke="currentColor" stroke-width="2"/>
              </svg>
            </div>
            <span class="brand-text">Voyage<span class="brand-highlight">AI</span></span>
          </div>
          <p class="brand-desc">成立于 2026 年，我们致力于利用先进的 AI 技术为旅行者提供最纯粹的灵感发现体验。</p>
          <div class="social-links">
            <a href="#" class="social-link">
              <svg viewBox="0 0 24 24" fill="currentColor">
                <circle cx="8" cy="10" r="4"/>
                <circle cx="16" cy="10" r="4"/>
                <circle cx="7" cy="9" r="0.8"/>
                <circle cx="9" cy="9" r="0.8"/>
                <circle cx="8" cy="11" r="0.8"/>
              </svg>
            </a>
            <a href="#" class="social-link">
              <svg viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
                </svg>
            </a>
            <a href="#" class="social-link">
              <svg viewBox="0 0 24 24" fill="currentColor">
                <path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/>
                </svg>
            </a>
          </div>
        </div>

        <div class="footer-links">
          <div class="link-group">
            <h4 class="link-title">产品</h4>
            <a href="#" class="footer-link">行程规划</a>
            <a href="#" class="footer-link">智能推荐</a>
            <a href="#" class="footer-link">预算分析</a>
            <a href="#" class="footer-link">行前清单</a>
          </div>

          <div class="link-group">
            <h4 class="link-title">资源</h4>
            <a href="#" class="footer-link">目的地指南</a>
            <a href="#" class="footer-link">旅行灵感</a>
            <a href="#" class="footer-link">社区故事</a>
            <a href="#" class="footer-link">旅行攻略</a>
          </div>

          <div class="link-group">
            <h4 class="link-title">公司</h4>
            <a href="#" class="footer-link">关于我们</a>
            <a href="#" class="footer-link">联系我们</a>
            <a href="#" class="footer-link">隐私政策</a>
            <a href="#" class="footer-link">服务条款</a>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <p class="copyright">© 2024 VoyageAI. 保留所有权利。</p>
      </div>
    </footer>

    <!-- 加载遮罩层 -->
    <transition name="fade">
      <div v-if="loading" class="loading-overlay">
        <div class="loading-content">
          <div class="loading-spinner">
            <div class="spinner-ring"></div>
            <div class="spinner-icon">
              <svg viewBox="0 0 24 24" fill="currentColor">
                <circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2"/>
                <ellipse cx="12" cy="12" rx="4" ry="10" fill="none" stroke="currentColor" stroke-width="2"/>
                <line x1="2" y1="12" x2="22" y2="12" stroke="currentColor" stroke-width="2"/>
              </svg>
            </div>
          </div>
          <h2 class="loading-title serif">VoyageAI 正在思考...</h2>
          <p class="loading-text loader-dots">
            正在分析目的地实时交通与天气数据<span>.</span><span>.</span><span>.</span>
          </p>
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
      isDark: false,
      errors: {
        start: '',
        dest: '',
        days: '',
        budget: ''
      }
    }
  },
  mounted() {
    // 从localStorage读取主题设置
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
      this.isDark = savedTheme === 'dark';
    } else {
      // 默认浅色模式
      this.isDark = false;
    }
    this.applyTheme();
  },
  methods: {
    toggleTheme() {
      this.isDark = !this.isDark;
      this.applyTheme();
      // 保存到localStorage
      localStorage.setItem('theme', this.isDark ? 'dark' : 'light');
    },
    applyTheme() {
      if (this.isDark) {
        document.documentElement.classList.add('dark-mode');
      } else {
        document.documentElement.classList.remove('dark-mode');
      }
    },
    validateForm() {
      let isValid = true
      
      // 重置错误信息
      this.errors = {
        start: '',
        dest: '',
        days: '',
        budget: ''
      }

      // 验证出发地
      if (!this.form.start || this.form.start.trim() === '') {
        this.errors.start = '请输入出发地'
        isValid = false
      }

      // 验证目的地
      if (!this.form.dest || this.form.dest.trim() === '') {
        this.errors.dest = '请输入目的地'
        isValid = false
      }

      // 验证游玩天数
      if (!this.form.days) {
        this.errors.days = '请输入游玩天数'
        isValid = false
      } else if (this.form.days < 1) {
        this.errors.days = '游玩天数至少为1天'
        isValid = false
      } else if (this.form.days > 30) {
        this.errors.days = '游玩天数最多为30天'
        isValid = false
      }

      // 验证预算
      if (!this.form.budget || this.form.budget.trim() === '') {
        this.errors.budget = '请输入预算范围'
        isValid = false
      } else if (!/^\d+(-\d+)?(\+)?$/.test(this.form.budget.replace(/,/g, ''))) {
        this.errors.budget = '预算格式不正确，例如：5000-8000 或 10000+'
        isValid = false
      }

      return isValid
    },
    startPlanning() {
      if (!this.validateForm()) {
        return
      }

      this.loading = true
      this.loadingProgress = 0

      const interval = setInterval(() => {
        this.loadingProgress += Math.random() * 15
        if (this.loadingProgress >= 95) {
          this.loadingProgress = 95
          clearInterval(interval)
        }
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
          this.$router.push({
            name: 'Result',
            query: { data: JSON.stringify(response.data) }
          })
        }, 500)
      })
      .catch(error => {
        clearInterval(interval)
        this.loading = false
        console.error('生成行程失败:', error)
        alert('生成行程失败，请检查后端服务是否启动')
      })
    }
  }
}
</script>

<style scoped>
/* CSS变量定义 */
:root {
  /* 浅色模式 */
  --bg-primary: #ffffff;
  --bg-secondary: #ffffff;
  --bg-nav: rgba(255, 255, 255, 0.95);
  --bg-card: rgba(255, 255, 255, 0.95);
  --bg-overlay: rgba(255, 255, 255, 0.3);
  
  --text-primary: #1e293b;
  --text-secondary: #64748b;
  --text-light: #e2e8f0;
  --text-white: #ffffff;
  
  --border-color: rgba(226, 232, 240, 0.8);
  --shadow-color: rgba(0, 0, 0, 0.05);
  
  --primary-color: #10B981;
  --secondary-color: #3B82F6;
}

/* 深色模式 */
html.dark-mode {
  --bg-primary: #020617;
  --bg-secondary: #0f172a;
  --bg-nav: rgba(15, 23, 42, 0.95);
  --bg-card: rgba(30, 41, 59, 0.98);
  --bg-overlay: rgba(15, 23, 42, 0.6);
  
  --text-primary: #ffffff;
  --text-secondary: #e2e8f0;
  --text-light: #cbd5e1;
  --text-white: #ffffff;
  
  --border-color: rgba(255, 255, 255, 0.15);
  --shadow-color: rgba(0, 0, 0, 0.3);
  
  --primary-color: #60a5fa;
  --secondary-color: #a78bfa;
}

.home-container {
  min-height: 100vh;
  background: var(--bg-primary);
}

/* 导航栏 */
.nav-bar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 2rem;
  background: var(--bg-nav);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border-color);
  box-shadow: 0 4px 20px var(--shadow-color);
}

.nav-brand {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.brand-icon {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #10B981, #059669);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.icon-svg {
  width: 24px;
  height: 24px;
  color: white;
}

.brand-text {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text-primary);
  letter-spacing: -0.5px;
}

.brand-highlight {
  background: linear-gradient(135deg, #10B981, #3B82F6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.nav-links {
  display: flex;
  gap: 2rem;
}

.nav-link {
  font-size: 0.95rem;
  font-weight: 500;
  color: var(--text-secondary);
  text-decoration: none;
  transition: color 0.3s ease;
  position: relative;
}

.nav-link:hover {
  color: #10B981;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 0;
  height: 2px;
  background: linear-gradient(90deg, #10B981, #3B82F6);
  transition: width 0.3s ease;
}

.nav-link:hover::after {
  width: 100%;
}

.nav-actions {
  display: flex;
  gap: 0.75rem;
}

.btn {
  padding: 0.6rem 1.25rem;
  border-radius: 9999px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
}

.btn-outline {
  background: transparent;
  border: 1.5px solid var(--border-color);
  color: var(--text-primary);
}

.btn-outline:hover {
  border-color: var(--primary-color);
  color: var(--primary-color);
  background: rgba(16, 185, 129, 0.1);
}

.theme-toggle {
  padding: 0.6rem;
  min-width: auto;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  z-index: 1001;
}

.theme-toggle svg {
  width: 20px;
  height: 20px;
}

.btn-primary {
  background: linear-gradient(135deg, #10B981, #059669);
  color: white;
  box-shadow: 0 4px 14px rgba(16, 185, 129, 0.35);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(16, 185, 129, 0.45);
}

/* Hero Section */
.hero-section {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 80px;
  overflow: hidden;
}

.hero-bg {
  position: absolute;
  inset: 0;
  z-index: 0;
}

.hero-bg-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    rgba(255, 255, 255, 0.3) 0%,
    rgba(255, 255, 255, 0.1) 100%
  );
}

html.dark-mode .hero-bg-img {
  display: none;
}

html.dark-mode .hero-bg {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
}

html.dark-mode .hero-overlay {
  background: linear-gradient(
    to bottom,
    rgba(15, 23, 42, 0.4) 0%,
    rgba(30, 41, 59, 0.6) 100%
  );
}

.hero-content {
  position: relative;
  z-index: 10;
  text-align: center;
  max-width: 900px;
  padding: 0 2rem;
}

.hero-title {
  font-size: clamp(3.5rem, 8vw, 5.5rem);
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 1.5rem;
  letter-spacing: -1.5px;
  font-family: 'Georgia', 'Times New Roman', serif;
  line-height: 1.1;
}

.gradient-text {
  background: linear-gradient(135deg, #10B981, #059669);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-subtitle {
  font-size: clamp(1.4rem, 3vw, 1.8rem);
  font-weight: 700;
  color: #10B981;
  margin-bottom: 3rem;
  opacity: 0.9;
  font-family: 'Georgia', 'Times New Roman', serif;
  line-height: 1.4;
}

/* 深色模式样式 */
html.dark-mode .brand-text {
  color: #ffffff !important;
}

html.dark-mode .brand-highlight {
  background: linear-gradient(135deg, #6ee7b7, #60a5fa) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
}

html.dark-mode .nav-link {
  color: #ffffff !important;
}

html.dark-mode .nav-link:hover {
  color: #60a5fa !important;
}

html.dark-mode .nav-link::after {
  background: linear-gradient(90deg, #60a5fa, #a78bfa) !important;
}

html.dark-mode .hero-title {
  color: #ffffff !important;
  text-shadow: 0 4px 12px rgba(0, 0, 0, 0.7) !important;
}

html.dark-mode .hero-subtitle {
  color: #a7f3d0 !important;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.6) !important;
}

html.dark-mode .gradient-text {
  background: linear-gradient(135deg, #a7f3d0, #6ee7b7) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
}

html.dark-mode .field-label {
  color: #ffffff !important;
}

html.dark-mode .field-input {
  color: #ffffff !important;
}

html.dark-mode .field-input::placeholder {
  color: #ffffff !important;
  opacity: 0.7 !important;
}

html.dark-mode .text-emerald { color: #6ee7b7 !important; }
html.dark-mode .text-blue { color: #60a5fa !important; }
html.dark-mode .text-purple { color: #a78bfa !important; }
html.dark-mode .text-amber { color: #fbbf24 !important; }

html.dark-mode .features-section {
  background: var(--bg-primary) !important;
}

html.dark-mode .footer {
  background: var(--bg-secondary) !important;
  border-top-color: var(--border-color) !important;
}

/* 搜索卡片 */
.search-card {
  padding: 1.5rem 2rem;
  border-radius: 2rem;
  max-width: 850px;
  margin: 0 auto;
  background: var(--bg-card);
  backdrop-filter: blur(20px);
  border: 1px solid var(--border-color);
  box-shadow: 0 8px 32px var(--shadow-color);
}

.search-fields {
  display: flex;
  align-items: stretch;
  gap: 0;
  margin-bottom: 1.25rem;
}

.field-group {
  flex: 1;
  padding: 0 1rem;
  text-align: left;
}

.field-group:first-child {
  padding-left: 0;
}

.field-group:last-child {
  padding-right: 0;
}

.field-label {
  display: block;
  font-size: 0.65rem;
  font-weight: 700;
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 1.5px;
  margin-bottom: 0.5rem;
}

.field-input-wrapper {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.field-icon {
  width: 18px;
  height: 18px;
  flex-shrink: 0;
}

.text-emerald { color: #10B981; }
.text-blue { color: #3B82F6; }
.text-purple { color: #8B5CF6; }
.text-amber { color: #F59E0B; }

.field-input {
  width: 100%;
  border: none;
  background: transparent;
  font-size: 1rem;
  font-weight: 500;
  color: var(--text-primary);
  padding: 0.25rem 0;
  outline: none;
}

.field-input::placeholder {
  color: var(--text-secondary);
}

.field-input.error {
  border-bottom: 2px solid #ef4444;
}

.error-message {
  font-size: 0.75rem;
  color: #ef4444;
  margin-top: 0.25rem;
  text-align: left;
}

.field-divider {
  width: 1px;
  background: linear-gradient(to bottom, transparent, var(--border-color), transparent);
  align-self: stretch;
}

.search-btn {
  width: 100%;
  padding: 1rem 2rem;
  background: linear-gradient(135deg, #10B981, #059669);
  color: white;
  border: none;
  border-radius: 9999px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  box-shadow: 0 4px 16px rgba(16, 185, 129, 0.35);
  transition: all 0.3s ease;
}

.search-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 24px rgba(16, 185, 129, 0.45);
}

.search-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.btn-icon {
  width: 20px;
  height: 20px;
  transition: transform 0.3s ease;
}

.btn-icon.rotating {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

/* 浮动装饰元素 */
.floating-icon {
  position: absolute;
  z-index: 5;
  opacity: 0.6;
  animation: float 6s ease-in-out infinite;
}

.floating-icon svg {
  width: 100%;
  height: 100%;
}

.icon-plane {
  bottom: 30%;
  left: -100px;
  width: 80px;
  height: 30px;
  color: #3B82F6;
  animation: fly 15s ease-in-out infinite;
}

@keyframes fly {
  0% {
    transform: translateX(-100px) translateY(0) rotate(0deg);
    opacity: 0;
  }
  10% {
    opacity: 0.8;
    transform: translateX(100px) translateY(-50px) rotate(5deg);
  }
  50% {
    transform: translateX(calc(50vw - 40px)) translateY(-100px) rotate(10deg);
  }
  90% {
    opacity: 0.8;
    transform: translateX(calc(100vw - 200px)) translateY(-50px) rotate(5deg);
  }
  100% {
    transform: translateX(calc(100vw + 100px)) translateY(0) rotate(0deg);
    opacity: 0;
  }
}

.icon-sparkle {
  top: 25%;
  right: 10%;
  width: 40px;
  height: 40px;
  color: #F59E0B;
  animation-delay: 1s;
}

@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-15px) rotate(5deg); }
}

/* 功能卡片区域 */
.features-section {
  padding: 6rem 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.feature-card {
  padding: 2.5rem;
  border-radius: 1.5rem;
  text-align: left;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  background: var(--bg-card);
  border: 1px solid var(--border-color);
}

.feature-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px -10px var(--shadow-color);
}

.feature-icon {
  width: 56px;
  height: 56px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.5rem;
}

.feature-icon svg {
  width: 28px;
  height: 28px;
  color: white;
}

.bg-emerald-light { background: linear-gradient(135deg, var(--primary-color), #34D399); }
.bg-blue-light { background: linear-gradient(135deg, var(--secondary-color), #60A5FA); }
.bg-purple-light { background: linear-gradient(135deg, #8B5CF6, #A78BFA); }

.feature-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.75rem;
}

.feature-desc {
  font-size: 0.95rem;
  color: var(--text-secondary);
  line-height: 1.7;
  margin-bottom: 1.5rem;
}

.feature-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: linear-gradient(135deg, #10B981, #059669);
  color: white;
  border: none;
  border-radius: 9999px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.feature-btn:hover {
  transform: translateX(4px);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.35);
}

.btn-arrow {
  width: 16px;
  height: 16px;
  transition: transform 0.3s ease;
}

.feature-btn:hover .btn-arrow {
  transform: translateX(4px);
}

/* 加载遮罩层 */
.loading-overlay {
  position: fixed;
  inset: 0;
  z-index: 9999;
  background: rgba(255, 255, 255, 0.98);
  backdrop-filter: blur(10px);
  display: flex;
  align-items: center;
  justify-content: center;
}

.loading-content {
  text-align: center;
}

.loading-spinner {
  position: relative;
  width: 120px;
  height: 120px;
  margin: 0 auto 2rem;
}

.spinner-ring {
  position: absolute;
  inset: 0;
  border: 4px solid #e2e8f0;
  border-top-color: #10B981;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.spinner-icon {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #10B981;
  animation: pulse 2s ease-in-out infinite;
}

.spinner-icon svg {
  width: 48px;
  height: 48px;
}

@keyframes pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.7; transform: scale(0.95); }
}

.loading-title {
  font-size: 1.75rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.75rem;
}

.loading-text {
  font-size: 1rem;
  color: #64748b;
  margin-bottom: 2rem;
}

.loading-progress {
  width: 300px;
  height: 4px;
  background: #e2e8f0;
  border-radius: 2px;
  overflow: hidden;
  margin: 0 auto;
}

.progress-bar {
  height: 100%;
  background: linear-gradient(90deg, #10B981, #3B82F6);
  border-radius: 2px;
  transition: width 0.3s ease;
}

/* 过渡动画 */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* 底部导航栏 */
.footer {
  background: var(--bg-secondary);
  padding: 4rem 2rem 2rem;
  border-top: 1px solid var(--border-color);
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 3fr;
  gap: 4rem;
  align-items: start;
}

.footer-brand {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.brand-header {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.brand-desc {
  color: var(--text-secondary);
  font-size: 0.95rem;
  line-height: 1.6;
  max-width: 300px;
}

.footer-links {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
  align-items: start;
}

.link-group {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.link-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.5rem;
}

.footer-link {
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 0.95rem;
  transition: all 0.3s ease;
}

.footer-link:hover {
  color: #10B981;
  transform: translateX(4px);
}

.social-links {
  display: flex;
  gap: 1rem;
  margin-top: 0.5rem;
  align-items: center;
}

.social-link {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: var(--bg-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-secondary);
  text-decoration: none;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px var(--shadow-color);
}

.social-link:hover {
  transform: translateY(-4px);
  color: #10B981;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.social-link svg {
  width: 20px;
  height: 20px;
}

.footer-bottom {
  max-width: 1200px;
  margin: 3rem auto 0;
  padding-top: 2rem;
  border-top: 1px solid var(--border-color);
  text-align: center;
}

.copyright {
  color: var(--text-secondary);
  font-size: 0.9rem;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .nav-links {
    display: none;
  }
  
  .nav-bar {
    padding: 1rem;
  }
  
  .hero-section {
    padding-top: 100px;
  }
  
  .search-fields {
    flex-direction: column;
    gap: 1rem;
  }
  
  .field-divider {
    display: none;
  }
  
  .field-group {
    padding: 0;
  }
  
  .search-card {
    padding: 1.5rem;
  }
  
  .floating-icon {
    display: none;
  }
  
  .features-section {
    padding: 4rem 1rem;
  }
  
  /* 移动端底部导航栏 */
  .footer {
    padding: 3rem 1rem 1.5rem;
  }
  
  .footer-content {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .footer-links {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
  }
  
  .footer-bottom {
    margin-top: 2rem;
    padding-top: 1.5rem;
  }
}
</style>
