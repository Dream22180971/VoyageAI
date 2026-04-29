<template>
  <div class="page-container">
    <nav class="nav-bar">
      <div class="nav-brand">
        <div class="brand-icon"><svg class="icon-svg" viewBox="0 0 24 24" fill="none"><path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 00-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z" fill="currentColor"/></svg></div>
        <router-link to="/" class="brand-text-link"><span class="brand-text">Voyage<span class="brand-highlight">AI</span></span></router-link>
        <span class="brand-slogan hide-mobile">发现未知，规划所爱</span>
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

    <section class="page-hero">
      <div class="hero-gradient"></div>
      <div class="hero-content">
        <h1 class="page-title serif">✨ <span class="gradient-text">灵感发现</span></h1>
        <p class="page-subtitle">不知道去哪？让灵感为你指引方向</p>
      </div>
    </section>

    <section class="content-section">
      <div class="section-inner">
        <h2 class="section-title">🌍 热门目的地</h2>
        <div class="card-grid">
          <div class="dest-card glass-card" v-for="dest in destinations" :key="dest.name" @click="$router.push('/')">
            <div class="dest-img" :style="{ background: dest.bg }"><span class="dest-emoji">{{ dest.emoji }}</span></div>
            <div class="dest-info"><h3>{{ dest.name }}</h3><p>{{ dest.desc }}</p><div class="dest-tags"><span class="tag" v-for="tag in dest.tags" :key="tag">{{ tag }}</span></div></div>
          </div>
        </div>
      </div>
    </section>

    <section class="content-section section-alt">
      <div class="section-inner">
        <h2 class="section-title">🎯 主题旅行</h2>
        <div class="theme-grid">
          <div class="theme-card glass-card" v-for="theme in themes" :key="theme.title" @click="$router.push('/')">
            <span class="theme-icon">{{ theme.icon }}</span>
            <h3>{{ theme.title }}</h3>
            <p>{{ theme.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="content-section">
      <div class="section-inner">
        <h2 class="section-title">📅 最佳出行时间</h2>
        <div class="timeline">
          <div class="timeline-item" v-for="item in seasons" :key="item.month">
            <div class="timeline-month">{{ item.month }}</div>
            <div class="timeline-content"><strong>{{ item.dest }}</strong><p>{{ item.reason }}</p></div>
          </div>
        </div>
      </div>
    </section>

    <footer class="footer">
      <div class="footer-content">
        <div class="footer-brand">
          <div class="brand-header"><div class="brand-icon"><svg class="icon-svg" viewBox="0 0 24 24" fill="none"><path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 00-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z" fill="currentColor"/></svg></div><router-link to="/" class="brand-text-link"><span class="brand-text">Voyage<span class="brand-highlight">AI</span></span></router-link></div>
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
  name: 'Inspiration',
  data() { return { isDark: false, menuOpen: false, destinations: [
    { name:'成都',emoji:'🐼',bg:'linear-gradient(135deg,#a18cd1,#fbc2eb)',desc:'天府之国，美食与文化的天堂',tags:['美食','文化','休闲'] },
    { name:'大理',emoji:'🏔️',bg:'linear-gradient(135deg,#667eea,#764ba2)',desc:'风花雪月，苍山洱海的诗意栖居',tags:['自然','摄影','文艺'] },
    { name:'西安',emoji:'🏯',bg:'linear-gradient(135deg,#f093fb,#f5576c)',desc:'千年古都，历史的厚重回响',tags:['历史','美食','人文'] },
    { name:'厦门',emoji:'🌊',bg:'linear-gradient(135deg,#4facfe,#00f2fe)',desc:'海上花园，文艺小资的海滨城市',tags:['海滨','文艺','美食'] },
    { name:'张家界',emoji:'⛰️',bg:'linear-gradient(135deg,#43e97b,#38f9d7)',desc:'奇峰林立，现实版的阿凡达世界',tags:['自然','探险','摄影'] },
    { name:'丽江',emoji:'🏘️',bg:'linear-gradient(135deg,#fa709a,#fee140)',desc:'古城悠悠，雪山下的浪漫邂逅',tags:['古城','雪山','民族'] }
  ], themes: [
    {icon:'🍜',title:'美食之旅',desc:'专程为一座城市的味道出发'},
    {icon:'⛰️',title:'户外探险',desc:'挑战自我，征服山川湖海'},
    {icon:'📸',title:'摄影采风',desc:'用镜头记录世间最美的风景'},
    {icon:'🏛️',title:'文化寻踪',desc:'穿越时空，感受历史与人文'},
    {icon:'🏖️',title:'海岛度假',desc:'阳光沙滩，享受慢时光'},
    {icon:'👨‍👩‍👧‍👦',title:'亲子出行',desc:'陪伴成长，探索世界的奇妙'}
  ], seasons: [
    {month:'3-5月',dest:'推荐：婺源、大理、张家界',reason:'春暖花开，油菜花海与山花烂漫'},
    {month:'6-8月',dest:'推荐：青海湖、呼伦贝尔、九寨沟',reason:'避暑胜地，草原辽阔湖光山色'},
    {month:'9-11月',dest:'推荐：北京、额济纳、稻城亚丁',reason:'秋高气爽，金秋色彩最浓郁'},
    {month:'12-2月',dest:'推荐：哈尔滨、三亚、丽江',reason:'冰雪世界或温暖避寒，各有精彩'}
  ] }},
  mounted() { const t=localStorage.getItem('theme');this.isDark=t?t==='dark':false;this.applyTheme() },
  methods: { toggleTheme(){this.isDark=!this.isDark;this.applyTheme();localStorage.setItem('theme',this.isDark?'dark':'light')}, applyTheme(){this.isDark?document.documentElement.classList.add('dark-mode'):document.documentElement.classList.remove('dark-mode')} }
}
</script>

<style scoped>
:root{--bg-primary:#fff;--bg-secondary:#fff;--bg-nav:rgba(255,255,255,0.95);--bg-card:rgba(255,255,255,0.95);--text-primary:#1e293b;--text-secondary:#64748b;--border-color:rgba(226,232,240,0.8);--shadow-color:rgba(0,0,0,0.05);--primary-color:#10B981;--secondary-color:#3B82F6;}
html.dark-mode{--bg-primary:#020617;--bg-secondary:#0f172a;--bg-nav:rgba(15,23,42,0.95);--bg-card:rgba(30,41,59,0.98);--text-primary:#fff;--text-secondary:#e2e8f0;--border-color:rgba(255,255,255,0.15);--shadow-color:rgba(0,0,0,0.3);--primary-color:#60a5fa;--secondary-color:#a78bfa;}
.page-container{min-height:100vh;background:var(--bg-primary);}
.nav-bar{position:fixed;top:0;left:0;right:0;z-index:1000;display:flex;align-items:center;justify-content:space-between;padding:1rem 2rem;background:rgba(2,6,23,0.40);backdrop-filter:blur(22px) saturate(1.15);border-bottom:1px solid rgba(255,255,255,0.12);box-shadow:0 10px 40px rgba(2,6,23,0.25);}
.nav-brand{display:flex;align-items:center;gap:0.75rem;}
.brand-icon{width:40px;height:40px;background:linear-gradient(135deg,#10B981,#059669);border-radius:12px;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 12px rgba(16,185,129,0.3);}
.icon-svg{width:24px;height:24px;color:white;}
.brand-text-link{text-decoration:none;}
.brand-text{font-size:1.5rem;font-weight:700;color:var(--text-primary);letter-spacing:-0.5px;}
.nav-bar .brand-text{color:rgba(255,255,255,0.92);}
.brand-slogan{margin-left:0.75rem;padding-left:0.75rem;border-left:1px solid rgba(255,255,255,0.14);color:rgba(226,232,240,0.78);font-size:0.85rem;font-weight:650;letter-spacing:0.02em;white-space:nowrap;}
.brand-highlight{background:linear-gradient(135deg,#10B981,#3B82F6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.nav-links{display:flex;gap:2rem;}
.nav-link{font-size:0.95rem;font-weight:600;color:rgba(226,232,240,0.80);text-decoration:none;transition:color 0.3s;position:relative;}
.nav-link:hover,.nav-link.router-link-exact-active{color:rgba(167,243,208,0.95);}
.nav-link::after{content:'';position:absolute;bottom:-4px;left:0;width:0;height:2px;background:linear-gradient(90deg,#10B981,#3B82F6);transition:width 0.3s;}
.nav-link:hover::after,.nav-link.router-link-exact-active::after{width:100%;}
.nav-actions{display:flex;gap:0.75rem;}
.btn{padding:0.6rem 1.25rem;border-radius:9999px;font-size:0.9rem;font-weight:600;cursor:pointer;transition:all 0.3s;border:none;}
.btn-outline{background:rgba(255,255,255,0.06);border:1.5px solid rgba(255,255,255,0.16);color:rgba(226,232,240,0.88);}
.btn-outline:hover{border-color:rgba(167,243,208,0.55);color:rgba(167,243,208,0.95);}
.theme-toggle{padding:0.6rem;min-width:auto;border-radius:50%;display:flex;align-items:center;justify-content:center;}
.theme-toggle svg{width:20px;height:20px;}
.btn-primary{background:linear-gradient(135deg,#10B981,#059669);color:white;box-shadow:0 4px 14px rgba(16,185,129,0.35);}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 6px 20px rgba(16,185,129,0.45);}
.page-hero{position:relative;padding:9rem 2rem 4rem;text-align:center;overflow:hidden;}
.hero-gradient{position:absolute;inset:0;background:radial-gradient(circle at 20% 18%, rgba(16,185,129,0.30), transparent 58%),radial-gradient(circle at 82% 22%, rgba(59,130,246,0.28), transparent 56%),linear-gradient(180deg,#030712 0%,#07162e 35%,#020617 100%);}
html.dark-mode .hero-gradient{background:radial-gradient(circle at 20% 18%, rgba(16,185,129,0.30), transparent 58%),radial-gradient(circle at 82% 22%, rgba(59,130,246,0.28), transparent 56%),linear-gradient(180deg,#030712 0%,#07162e 35%,#020617 100%);}
.hero-content{position:relative;z-index:10;}
.page-title{font-size:clamp(2.5rem,5vw,3.5rem);font-weight:760;color:rgba(255,255,255,0.92);margin-bottom:1rem;font-family:'Georgia',serif;text-shadow:0 10px 40px rgba(2,6,23,0.55),0 0 18px rgba(59,130,246,0.16),0 0 16px rgba(16,185,129,0.14);}
html.dark-mode .page-title{color:rgba(255,255,255,0.92);}
.gradient-text{background:linear-gradient(135deg,#10B981,#3B82F6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
html.dark-mode .gradient-text{background:linear-gradient(135deg,#6ee7b7,#60a5fa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.page-subtitle{font-size:1.15rem;color:rgba(226,232,240,0.82);max-width:600px;margin:0 auto;text-shadow:0 8px 26px rgba(2,6,23,0.55);}
html.dark-mode .page-subtitle{color:rgba(226,232,240,0.82);}
.content-section{padding:4rem 2rem;}
.section-alt{background:var(--bg-secondary);}
.section-inner{max-width:1000px;margin:0 auto;}
.section-title{font-size:1.6rem;font-weight:700;color:var(--text-primary);text-align:center;margin-bottom:2rem;}
.card-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.5rem;}
.dest-card{border-radius:1.2rem;overflow:hidden;cursor:pointer;transition:all 0.4s;background:var(--bg-card);border:1px solid var(--border-color);}
.dest-card:hover{transform:translateY(-6px);box-shadow:0 16px 32px -8px var(--shadow-color);}
.dest-img{height:120px;display:flex;align-items:center;justify-content:center;}
.dest-emoji{font-size:3rem;}
.dest-info{padding:1.2rem;}
.dest-info h3{color:var(--text-primary);font-size:1.1rem;margin-bottom:0.3rem;}
.dest-info p{color:var(--text-secondary);font-size:0.85rem;margin-bottom:0.8rem;}
.dest-tags{display:flex;gap:0.5rem;}
.tag{background:rgba(16,185,129,0.1);color:var(--primary-color);padding:0.2rem 0.6rem;border-radius:20px;font-size:0.75rem;}
html.dark-mode .tag{background:rgba(96,165,250,0.15);}
.theme-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1.2rem;}
.theme-card{background:var(--bg-card);border:1px solid var(--border-color);border-radius:1.2rem;padding:1.5rem;text-align:center;cursor:pointer;transition:all 0.4s;}
.theme-card:hover{transform:translateY(-4px);box-shadow:0 12px 24px -6px var(--shadow-color);}
.theme-icon{font-size:2rem;display:block;margin-bottom:0.8rem;}
.theme-card h3{color:var(--text-primary);font-size:1rem;margin-bottom:0.4rem;}
.theme-card p{color:var(--text-secondary);font-size:0.85rem;}
.timeline{max-width:700px;margin:0 auto;}
.timeline-item{display:flex;gap:1.5rem;padding:1rem 0;border-bottom:1px solid var(--border-color);}
.timeline-month{min-width:80px;color:var(--primary-color);font-weight:700;font-size:1rem;padding-top:2px;}
.timeline-content strong{color:var(--text-primary);}
.timeline-content p{color:var(--text-secondary);font-size:0.9rem;margin-top:0.2rem;}
.footer{background:var(--bg-secondary);padding:4rem 2rem 2rem;border-top:1px solid var(--border-color);}
.footer-content{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 3fr;gap:4rem;}
.footer-brand{display:flex;flex-direction:column;gap:1rem;}
.brand-header{display:flex;align-items:center;gap:1rem;}
.brand-desc{color:var(--text-secondary);font-size:0.95rem;line-height:1.6;max-width:300px;}
.footer-links{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:2rem;}
.link-group{display:flex;flex-direction:column;gap:1rem;}
.link-title{font-size:1.1rem;font-weight:700;color:var(--text-primary);margin-bottom:0.5rem;}
.footer-link{color:var(--text-secondary);text-decoration:none;font-size:0.95rem;transition:all 0.3s;display:block;}
.footer-link:hover{color:var(--primary-color);transform:translateX(4px);}
.footer-bottom{max-width:1200px;margin:3rem auto 0;padding-top:2rem;border-top:1px solid var(--border-color);text-align:center;}
.copyright{color:var(--text-secondary);font-size:0.9rem;}
@media(max-width:768px){.nav-links{display:none;}.card-grid{grid-template-columns:1fr;}.footer-content{grid-template-columns:1fr;gap:2rem;}.footer-links{grid-template-columns:repeat(2,1fr);}}

.hamburger{display:none;flex-direction:column;gap:5px;padding:0.5rem;cursor:pointer;background:none;border:none;}
.hamburger span{display:block;width:22px;height:2px;background:rgba(226,232,240,0.85);border-radius:2px;transition:all 0.3s;}
.hamburger.active span:nth-child(1){transform:rotate(45deg) translate(5px,5px);}
.hamburger.active span:nth-child(2){opacity:0;}
.hamburger.active span:nth-child(3){transform:rotate(-45deg) translate(5px,-5px);}
.mobile-menu{display:none;}
</style>
