<template>
  <div class="page-container">
    <nav class="nav-bar">
      <div class="nav-brand">
        <div class="brand-icon"><svg class="icon-svg" viewBox="0 0 24 24" fill="none"><path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 00-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z" fill="currentColor"/></svg></div>
        <router-link to="/" class="brand-text-link"><span class="brand-text">Voyage<span class="brand-highlight">AI</span></span></router-link>
      </div>
      <div class="nav-links">
        <router-link to="/" class="nav-link">首页</router-link>
        <router-link to="/inspiration" class="nav-link">发现灵感</router-link>
        <router-link to="/guide" class="nav-link">目的地指南</router-link>
        <router-link to="/community" class="nav-link">社区足迹</router-link>
        <router-link to="/about" class="nav-link">关于我们</router-link>
      </div>
      <div class="nav-actions">
        <button class="btn btn-outline theme-toggle" @click="toggleTheme">
          <svg v-if="!isDark" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
          <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
        </button>
        <button class="btn btn-primary">开启探索</button>
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
        </div>
      </transition>
    </nav>

    <!-- Hero -->
    <section class="page-hero">
      <div class="hero-gradient"></div>
      <div class="hero-content">
        <h1 class="page-title serif">关于 <span class="gradient-text">VoyageAI</span></h1>
        <p class="page-subtitle">AI 驱动的智能旅行规划，让每一次出发都充满期待</p>
      </div>
    </section>

    <!-- 项目介绍 -->
    <section class="content-section">
      <div class="section-inner">
        <h2 class="section-title">🚀 项目简介</h2>
        <p class="section-text">VoyageAI 是一款基于人工智能的智能旅行规划系统。只需输入出发地、目的地、旅行天数和预算，AI 便会为你生成一份个性化的行程方案——涵盖每日活动安排、预算分析、天气预警以及行前准备清单。</p>
        <p class="section-text">我们致力于让旅行规划变得简单、高效且充满惊喜，无论你是背包客、家庭出游还是商务旅行，VoyageAI 都能为你量身定制最适合的行程。</p>
      </div>
    </section>

    <!-- 核心功能 -->
    <section class="content-section section-alt">
      <div class="section-inner">
        <h2 class="section-title">✨ 核心功能</h2>
        <div class="features-grid">
          <div class="feature-card glass-card card-hover">
            <div class="feature-icon bg-emerald-light"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg></div>
            <h3 class="feature-name">AI 智能规划</h3>
            <p class="feature-desc">基于 DeepSeek 大模型，深度理解用户需求，生成个性化行程方案</p>
          </div>
          <div class="feature-card glass-card card-hover">
            <div class="feature-icon bg-blue-light"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/></svg></div>
            <h3 class="feature-name">实时天气预警</h3>
            <p class="feature-desc">集成 OpenWeatherMap API，提供目的地实时天气及出行建议</p>
          </div>
          <div class="feature-card glass-card card-hover">
            <div class="feature-icon bg-amber-light"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div>
            <h3 class="feature-name">智能预算分析</h3>
            <p class="feature-desc">自动拆分交通、住宿、餐饮、门票等费用，预算一目了然</p>
          </div>
          <div class="feature-card glass-card card-hover">
            <div class="feature-icon bg-purple-light"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg></div>
            <h3 class="feature-name">行前准备清单</h3>
            <p class="feature-desc">根据目的地气候和行程特点，自动生成个性化打包清单</p>
          </div>
          <div class="feature-card glass-card card-hover">
            <div class="feature-icon bg-indigo-light"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg></div>
            <h3 class="feature-name">深色模式</h3>
            <p class="feature-desc">支持浅色/深色主题切换，主题偏好自动保存，舒适阅读</p>
          </div>
          <div class="feature-card glass-card card-hover">
            <div class="feature-icon bg-pink-light"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 20V10M12 20V4M6 20v-6"/></svg></div>
            <h3 class="feature-name">数据可视化</h3>
            <p class="feature-desc">使用 ECharts 图表展示预算分布，直观清晰</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 技术栈 -->
    <section class="content-section">
      <div class="section-inner">
        <h2 class="section-title">🛠️ 技术栈</h2>
        <div class="tech-grid">
          <div class="tech-column glass-card">
            <h3>后端</h3>
            <ul class="tech-list">
              <li><strong>FastAPI</strong> — 高性能异步 Python Web 框架</li>
              <li><strong>DeepSeek API</strong> — AI 行程生成引擎</li>
              <li><strong>OpenWeatherMap</strong> — 实时天气数据</li>
              <li><strong>SQLAlchemy</strong> — ORM 数据库管理</li>
              <li><strong>SQLite</strong> — 轻量级数据存储</li>
            </ul>
          </div>
          <div class="tech-column glass-card">
            <h3>前端</h3>
            <ul class="tech-list">
              <li><strong>Vue 3</strong> — 现代化前端框架</li>
              <li><strong>Vite</strong> — 极速构建工具</li>
              <li><strong>Vue Router</strong> — 单页应用路由</li>
              <li><strong>Axios</strong> — HTTP 请求</li>
              <li><strong>ECharts</strong> — 数据可视化</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- 底部 -->
    <footer class="footer">
      <div class="footer-content">
        <div class="footer-brand">
          <div class="brand-header">
            <div class="brand-icon"><svg class="icon-svg" viewBox="0 0 24 24" fill="none"><path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 00-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z" fill="currentColor"/></svg></div>
            <router-link to="/" class="brand-text-link"><span class="brand-text">Voyage<span class="brand-highlight">AI</span></span></router-link>
          </div>
          <p class="brand-desc">成立于 2026 年，我们致力于利用先进的 AI 技术为旅行者提供最纯粹的灵感发现体验。</p>
        </div>
        <div class="footer-links">
          <div class="link-group"><h4 class="link-title">产品</h4><router-link to="/" class="footer-link">行程规划</router-link><router-link to="/inspiration" class="footer-link">智能推荐</router-link><router-link to="/guide" class="footer-link">预算分析</router-link><router-link to="/community" class="footer-link">行前清单</router-link></div>
          <div class="link-group"><h4 class="link-title">资源</h4><router-link to="/guide" class="footer-link">目的地指南</router-link><router-link to="/inspiration" class="footer-link">旅行灵感</router-link><router-link to="/community" class="footer-link">社区故事</router-link><router-link to="/about" class="footer-link">旅行攻略</router-link></div>
          <div class="link-group"><h4 class="link-title">公司</h4><router-link to="/about" class="footer-link">关于我们</router-link><router-link to="/about" class="footer-link">联系我们</router-link><router-link to="/about" class="footer-link">隐私政策</router-link><router-link to="/about" class="footer-link">服务条款</router-link></div>
        </div>
      </div>
      <div class="footer-bottom"><p class="copyright">© 2026 VoyageAI — 智能旅行规划系统</p></div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'About',
  data() { return { isDark: false, menuOpen: false } },
  mounted() { const t = localStorage.getItem('theme'); this.isDark = t ? t === 'dark' : false; this.applyTheme() },
  methods: {
    toggleTheme() { this.isDark = !this.isDark; this.applyTheme(); localStorage.setItem('theme', this.isDark ? 'dark' : 'light') },
    applyTheme() { this.isDark ? document.documentElement.classList.add('dark-mode') : document.documentElement.classList.remove('dark-mode') }
  }
}
</script>

<style scoped>
:root { --bg-primary:#fff;--bg-secondary:#fff;--bg-nav:rgba(255,255,255,0.95);--bg-card:rgba(255,255,255,0.95);--text-primary:#1e293b;--text-secondary:#64748b;--border-color:rgba(226,232,240,0.8);--shadow-color:rgba(0,0,0,0.05);--primary-color:#10B981;--secondary-color:#3B82F6; }
html.dark-mode { --bg-primary:#020617;--bg-secondary:#0f172a;--bg-nav:rgba(15,23,42,0.95);--bg-card:rgba(30,41,59,0.98);--text-primary:#fff;--text-secondary:#e2e8f0;--border-color:rgba(255,255,255,0.15);--shadow-color:rgba(0,0,0,0.3);--primary-color:#60a5fa;--secondary-color:#a78bfa; }
.page-container { min-height:100vh; background:var(--bg-primary); }

/* 导航栏 */
.nav-bar { position:fixed;top:0;left:0;right:0;z-index:1000;display:flex;align-items:center;justify-content:space-between;padding:1rem 2rem;background:var(--bg-nav);backdrop-filter:blur(20px);border-bottom:1px solid var(--border-color);box-shadow:0 4px 20px var(--shadow-color); }
.nav-brand { display:flex;align-items:center;gap:0.75rem; }
.brand-icon { width:40px;height:40px;background:linear-gradient(135deg,#10B981,#059669);border-radius:12px;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 12px rgba(16,185,129,0.3); }
.icon-svg { width:24px;height:24px;color:white; }
.brand-text-link { text-decoration:none; }
.brand-text { font-size:1.5rem;font-weight:700;color:var(--text-primary);letter-spacing:-0.5px; }
.brand-highlight { background:linear-gradient(135deg,#10B981,#3B82F6);-webkit-background-clip:text;-webkit-text-fill-color:transparent; }
.nav-links { display:flex;gap:2rem; }
.nav-link { font-size:0.95rem;font-weight:500;color:var(--text-secondary);text-decoration:none;transition:color 0.3s;position:relative; }
.nav-link:hover,.nav-link.router-link-exact-active { color:var(--primary-color); }
.nav-link::after { content:'';position:absolute;bottom:-4px;left:0;width:0;height:2px;background:linear-gradient(90deg,#10B981,#3B82F6);transition:width 0.3s; }
.nav-link:hover::after,.nav-link.router-link-exact-active::after { width:100%; }
.nav-actions { display:flex;gap:0.75rem; }
.btn { padding:0.6rem 1.25rem;border-radius:9999px;font-size:0.9rem;font-weight:600;cursor:pointer;transition:all 0.3s;border:none; }
.btn-outline { background:transparent;border:1.5px solid var(--border-color);color:var(--text-primary); }
.btn-outline:hover { border-color:var(--primary-color);color:var(--primary-color); }
.theme-toggle { padding:0.6rem;min-width:auto;border-radius:50%;display:flex;align-items:center;justify-content:center; }
.theme-toggle svg { width:20px;height:20px; }
.btn-primary { background:linear-gradient(135deg,#10B981,#059669);color:white;box-shadow:0 4px 14px rgba(16,185,129,0.35); }
.btn-primary:hover { transform:translateY(-2px);box-shadow:0 6px 20px rgba(16,185,129,0.45); }

/* Hero */
.page-hero { position:relative;padding:9rem 2rem 4rem;text-align:center;overflow:hidden; }
.hero-gradient { position:absolute;inset:0;background:linear-gradient(135deg,#ecfdf5 0%,#dbeafe 30%,#ede9fe 60%,#fce7f3 100%); }
html.dark-mode .hero-gradient { background:linear-gradient(135deg,#0f172a 0%,#1e293b 50%,#334155 100%); }
.hero-content { position:relative;z-index:10; }
.page-title { font-size:clamp(2.5rem,5vw,3.5rem);font-weight:700;color:#1e293b;margin-bottom:1rem;font-family:'Georgia',serif; }
html.dark-mode .page-title { color:#fff; }
.gradient-text { background:linear-gradient(135deg,#10B981,#3B82F6);-webkit-background-clip:text;-webkit-text-fill-color:transparent; }
html.dark-mode .gradient-text { background:linear-gradient(135deg,#6ee7b7,#60a5fa);-webkit-background-clip:text;-webkit-text-fill-color:transparent; }
.page-subtitle { font-size:1.15rem;color:#64748b;max-width:600px;margin:0 auto; }
html.dark-mode .page-subtitle { color:#94a3b8; }

/* 内容区 */
.content-section { padding:4rem 2rem; }
.section-alt { background:var(--bg-secondary); }
.section-inner { max-width:1000px;margin:0 auto; }
.section-title { font-size:1.6rem;font-weight:700;color:var(--text-primary);text-align:center;margin-bottom:2rem; }
.section-text { font-size:1rem;color:var(--text-secondary);line-height:1.8;text-align:center;max-width:700px;margin:0 auto 1.2rem; }

/* 功能卡片 */
.features-grid { display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.5rem; }
.feature-card { padding:2rem;border-radius:1.5rem;text-align:center;background:var(--bg-card);border:1px solid var(--border-color);transition:all 0.4s; }
.feature-card:hover { transform:translateY(-6px);box-shadow:0 16px 32px -8px var(--shadow-color); }
.feature-icon { width:52px;height:52px;border-radius:14px;display:flex;align-items:center;justify-content:center;margin:0 auto 1rem; }
.feature-icon svg { width:26px;height:26px;color:white; }
.bg-emerald-light { background:linear-gradient(135deg,#10B981,#34D399); }
.bg-blue-light { background:linear-gradient(135deg,#3B82F6,#60A5FA); }
.bg-amber-light { background:linear-gradient(135deg,#F59E0B,#FBBF24); }
.bg-purple-light { background:linear-gradient(135deg,#8B5CF6,#A78BFA); }
.bg-indigo-light { background:linear-gradient(135deg,#6366F1,#818CF8); }
.bg-pink-light { background:linear-gradient(135deg,#EC4899,#F472B6); }
.feature-name { font-size:1.1rem;font-weight:700;color:var(--text-primary);margin-bottom:0.5rem; }
.feature-desc { font-size:0.9rem;color:var(--text-secondary);line-height:1.6; }

/* 技术栈 */
.tech-grid { display:grid;grid-template-columns:1fr 1fr;gap:2rem; }
.tech-column { padding:2rem;border-radius:1.5rem;background:var(--bg-card);border:1px solid var(--border-color); }
.tech-column h3 { font-size:1.15rem;color:var(--primary-color);margin-bottom:1rem;text-align:center; }
.tech-list { list-style:none;padding:0; }
.tech-list li { padding:0.6rem 0;color:var(--text-secondary);font-size:0.95rem;border-bottom:1px solid var(--border-color); }
.tech-list li:last-child { border-bottom:none; }
.tech-list li strong { color:var(--text-primary); }

/* 底部 */
.footer { background:var(--bg-secondary);padding:4rem 2rem 2rem;border-top:1px solid var(--border-color); }
.footer-content { max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 3fr;gap:4rem; }
.footer-brand { display:flex;flex-direction:column;gap:1rem; }
.brand-header { display:flex;align-items:center;gap:1rem; }
.brand-desc { color:var(--text-secondary);font-size:0.95rem;line-height:1.6;max-width:300px; }
.footer-links { display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:2rem; }
.link-group { display:flex;flex-direction:column;gap:1rem; }
.link-title { font-size:1.1rem;font-weight:700;color:var(--text-primary);margin-bottom:0.5rem; }
.footer-link { color:var(--text-secondary);text-decoration:none;font-size:0.95rem;transition:all 0.3s;display:block; }
.footer-link:hover { color:var(--primary-color);transform:translateX(4px); }
.footer-bottom { max-width:1200px;margin:3rem auto 0;padding-top:2rem;border-top:1px solid var(--border-color);text-align:center; }
.copyright { color:var(--text-secondary);font-size:0.9rem; }

@media (max-width:768px) {
  .nav-links { display:none; }
  .tech-grid { grid-template-columns:1fr; }
  .footer-content { grid-template-columns:1fr;gap:2rem; }
  .footer-links { grid-template-columns:repeat(2,1fr); }
}

.hamburger{display:none;flex-direction:column;gap:5px;padding:0.5rem;cursor:pointer;background:none;border:none;}
.hamburger span{display:block;width:22px;height:2px;background:var(--text-primary);border-radius:2px;transition:all 0.3s;}
.hamburger.active span:nth-child(1){transform:rotate(45deg) translate(5px,5px);}
.hamburger.active span:nth-child(2){opacity:0;}
.hamburger.active span:nth-child(3){transform:rotate(-45deg) translate(5px,-5px);}
.mobile-menu{display:none;}
</style>
