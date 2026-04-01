<template>
  <div class="about-page">
    <!-- 导航栏 -->
    <nav class="navbar">
      <div class="nav-container">
        <router-link to="/" class="nav-logo">
          <span class="logo-icon">🗺️</span>
          <span class="logo-text">VoyageAI</span>
        </router-link>
        <div class="nav-links">
          <router-link to="/" class="nav-link">首页</router-link>
          <router-link to="/inspiration" class="nav-link">发现灵感</router-link>
          <router-link to="/guide" class="nav-link">旅行攻略</router-link>
          <router-link to="/community" class="nav-link">社区</router-link>
          <router-link to="/about" class="nav-link active">关于我们</router-link>
        </div>
      </div>
    </nav>

    <!-- Hero 区域 -->
    <section class="hero">
      <div class="hero-content">
        <h1 class="hero-title">关于 <span class="highlight">VoyageAI</span></h1>
        <p class="hero-subtitle">AI 驱动的智能旅行规划，让每一次出发都充满期待</p>
      </div>
    </section>

    <!-- 项目介绍 -->
    <section class="section">
      <div class="container">
        <h2 class="section-title">🚀 项目简介</h2>
        <p class="section-text">
          VoyageAI 是一款基于人工智能的智能旅行规划系统。只需输入出发地、目的地、旅行天数和预算，
          AI 便会为你生成一份个性化的行程方案——涵盖每日活动安排、预算分析、天气预警以及行前准备清单。
        </p>
        <p class="section-text">
          我们致力于让旅行规划变得简单、高效且充满惊喜，无论你是背包客、家庭出游还是商务旅行，
          VoyageAI 都能为你量身定制最适合的行程。
        </p>
      </div>
    </section>

    <!-- 核心功能 -->
    <section class="section section-alt">
      <div class="container">
        <h2 class="section-title">✨ 核心功能</h2>
        <div class="features-grid">
          <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <h3>AI 智能规划</h3>
            <p>基于 DeepSeek 大模型，深度理解用户需求，生成个性化行程方案</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">🌤️</div>
            <h3>实时天气预警</h3>
            <p>集成 OpenWeatherMap API，提供目的地实时天气及出行建议</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">💰</div>
            <h3>智能预算分析</h3>
            <p>自动拆分交通、住宿、餐饮、门票等费用，预算一目了然</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">📋</div>
            <h3>行前准备清单</h3>
            <p>根据目的地气候和行程特点，自动生成个性化打包清单</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">🌙</div>
            <h3>深色模式</h3>
            <p>支持浅色/深色主题切换，主题偏好自动保存，舒适阅读</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h3>数据可视化</h3>
            <p>使用 ECharts 图表展示预算分布，直观清晰</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 技术栈 -->
    <section class="section">
      <div class="container">
        <h2 class="section-title">🛠️ 技术栈</h2>
        <div class="tech-grid">
          <div class="tech-column">
            <h3>后端</h3>
            <ul class="tech-list">
              <li><strong>FastAPI</strong> — 高性能异步 Python Web 框架</li>
              <li><strong>DeepSeek API</strong> — AI 行程生成引擎</li>
              <li><strong>OpenWeatherMap</strong> — 实时天气数据</li>
              <li><strong>SQLAlchemy</strong> — ORM 数据库管理</li>
              <li><strong>SQLite</strong> — 轻量级数据存储</li>
            </ul>
          </div>
          <div class="tech-column">
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

    <!-- 页脚 -->
    <footer class="footer">
      <div class="container">
        <p>© 2026 VoyageAI — 智能旅行规划系统</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
</script>

<style scoped>
.about-page {
  min-height: 100vh;
  background: linear-gradient(135deg, #0f0c29 0%, #1a1a3e 50%, #24243e 100%);
  color: #e0e0e0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
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
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0.8rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  text-decoration: none;
  font-size: 1.3rem;
  font-weight: 700;
}

.logo-icon {
  font-size: 1.5rem;
}

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

/* Hero */
.hero {
  padding: 10rem 2rem 4rem;
  text-align: center;
}

.hero-title {
  font-size: 3rem;
  font-weight: 800;
  margin-bottom: 1rem;
  background: linear-gradient(135deg, #fff, #c0c0c0);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.highlight {
  background: linear-gradient(135deg, #667eea, #764ba2, #f093fb);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-subtitle {
  font-size: 1.2rem;
  color: #a0a0a0;
  max-width: 600px;
  margin: 0 auto;
}

/* 通用 Section */
.section {
  padding: 4rem 2rem;
}

.section-alt {
  background: rgba(255, 255, 255, 0.02);
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

.section-text {
  font-size: 1.05rem;
  line-height: 1.8;
  color: #b0b0b0;
  text-align: center;
  max-width: 750px;
  margin: 0 auto 1.5rem;
}

/* 功能卡片 */
.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

.feature-card {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 16px;
  padding: 2rem;
  text-align: center;
  transition: transform 0.3s, background 0.3s;
}

.feature-card:hover {
  transform: translateY(-4px);
  background: rgba(255, 255, 255, 0.07);
}

.feature-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.feature-card h3 {
  font-size: 1.1rem;
  color: #fff;
  margin-bottom: 0.5rem;
}

.feature-card p {
  font-size: 0.9rem;
  color: #909090;
  line-height: 1.6;
}

/* 技术栈 */
.tech-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
}

.tech-column h3 {
  font-size: 1.2rem;
  color: #667eea;
  margin-bottom: 1rem;
  text-align: center;
}

.tech-list {
  list-style: none;
  padding: 0;
}

.tech-list li {
  padding: 0.5rem 0;
  color: #b0b0b0;
  font-size: 0.95rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.tech-list li strong {
  color: #d0d0d0;
}

/* 页脚 */
.footer {
  padding: 2rem;
  text-align: center;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  color: #606060;
  font-size: 0.85rem;
}

/* 响应式 */
@media (max-width: 768px) {
  .hero-title { font-size: 2rem; }
  .tech-grid { grid-template-columns: 1fr; gap: 2rem; }
  .nav-links { gap: 0.8rem; }
  .nav-link { font-size: 0.8rem; }
}
</style>
