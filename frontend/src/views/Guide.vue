<template>
  <div class="page-container">
    <nav class="nav-bar">
      <div class="nav-brand"><div class="brand-icon"><svg class="icon-svg" viewBox="0 0 24 24" fill="none"><path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 00-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z" fill="currentColor"/></svg></div><router-link to="/" class="brand-text-link"><span class="brand-text">Voyage<span class="brand-highlight">AI</span></span></router-link></div>
      <div class="nav-links"><router-link to="/" class="nav-link">首页</router-link><router-link to="/inspiration" class="nav-link">发现灵感</router-link><router-link to="/guide" class="nav-link">目的地指南</router-link><router-link to="/community" class="nav-link">社区足迹</router-link><router-link to="/about" class="nav-link">关于我们</router-link></div>
      <div class="nav-actions"><button class="btn btn-outline theme-toggle" @click="toggleTheme"><svg v-if="!isDark" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg><svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/></svg></button><button class="btn btn-primary">开启探索</button><button class="hamburger" @click="menuOpen = !menuOpen" :class="{ active: menuOpen }"><span></span><span></span><span></span></button></div><transition name="menu"><div class="mobile-menu" v-if="menuOpen" @click="menuOpen = false"><router-link to="/" class="mobile-link">首页</router-link><router-link to="/inspiration" class="mobile-link">发现灵感</router-link><router-link to="/guide" class="mobile-link">目的地指南</router-link><router-link to="/community" class="mobile-link">社区足迹</router-link><router-link to="/about" class="mobile-link">关于我们</router-link></div></transition></nav>

    <section class="page-hero"><div class="hero-gradient"></div><div class="hero-content">
      <h1 class="page-title serif">📖 <span class="gradient-text">目的地指南</span></h1>
      <p class="page-subtitle">出发前必看，深度了解你的下一站</p>
      <div class="search-bar"><input v-model="search" placeholder="搜索目的地..." class="search-input"></div>
    </div></section>

    <section class="content-section">
      <div class="section-inner">
        <div class="guide-list">
          <div class="guide-card glass-card" v-for="g in filteredGuides" :key="g.city">
            <div class="guide-header" :style="{ background: g.bg }">
              <span class="guide-emoji">{{ g.emoji }}</span>
              <div class="guide-meta"><h2>{{ g.city }}</h2><span class="guide-badge">{{ g.province }}</span></div>
              <div class="guide-rating">⭐ {{ g.rating }}</div>
            </div>
            <div class="guide-body">
              <p class="guide-desc">{{ g.desc }}</p>
              <div class="guide-sections">
                <div class="guide-section"><h4>🍜 必吃美食</h4><p>{{ g.food }}</p></div>
                <div class="guide-section"><h4>📷 必去景点</h4><p>{{ g.attractions }}</p></div>
                <div class="guide-section"><h4>💰 人均预算</h4><p>{{ g.budget }}</p></div>
                <div class="guide-section"><h4>📅 最佳时间</h4><p>{{ g.bestTime }}</p></div>
              </div>
              <div class="guide-tips"><h4>💡 小贴士</h4><ul><li v-for="tip in g.tips" :key="tip">{{ tip }}</li></ul></div>
              <button class="plan-btn" @click="$router.push('/')">🤖 AI 规划此行程</button>
            </div>
          </div>
        </div>
        <p v-if="filteredGuides.length===0" class="empty-msg">没有找到匹配的目的地 😢</p>
      </div>
    </section>

    <footer class="footer">
      <div class="footer-content">
        <div class="footer-brand"><div class="brand-header"><div class="brand-icon"><svg class="icon-svg" viewBox="0 0 24 24" fill="none"><path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 00-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z" fill="currentColor"/></svg></div><router-link to="/" class="brand-text-link"><span class="brand-text">Voyage<span class="brand-highlight">AI</span></span></router-link></div><p class="brand-desc">成立于 2026 年，致力于利用先进的 AI 技术为旅行者提供最纯粹的灵感发现体验。</p></div>
        <div class="footer-links"><div class="link-group"><h4 class="link-title">产品</h4><router-link to="/" class="footer-link">行程规划</router-link><router-link to="/inspiration" class="footer-link">智能推荐</router-link><router-link to="/guide" class="footer-link">预算分析</router-link><router-link to="/community" class="footer-link">行前清单</router-link></div><div class="link-group"><h4 class="link-title">资源</h4><router-link to="/guide" class="footer-link">目的地指南</router-link><router-link to="/inspiration" class="footer-link">旅行灵感</router-link><router-link to="/community" class="footer-link">社区故事</router-link><router-link to="/about" class="footer-link">旅行攻略</router-link></div><div class="link-group"><h4 class="link-title">公司</h4><router-link to="/about" class="footer-link">关于我们</router-link><router-link to="/about" class="footer-link">联系我们</router-link><router-link to="/about" class="footer-link">隐私政策</router-link><router-link to="/about" class="footer-link">服务条款</router-link></div></div>
      </div>
      <div class="footer-bottom"><p class="copyright">© 2026 VoyageAI — 智能旅行规划系统</p></div>
    </footer>
  </div>
</template>

<script>
import { computed } from 'vue'
export default {
  name: 'Guide',
  data() { return { isDark: false, menuOpen: false, search: '', guides: [
    { city:'成都',emoji:'🐼',province:'四川省',rating:'4.8',bg:'linear-gradient(135deg,#a18cd1,#fbc2eb)',desc:'成都，一座来了就不想走的城市。这里有憨态可掬的大熊猫，有麻辣鲜香的火锅，有悠闲的茶馆文化，还有璀璨的三千年历史。',food:'火锅、串串香、担担面、龙抄手、钟水饺、兔头、钵钵鸡',attractions:'大熊猫繁育基地、宽窄巷子、武侯祠、锦里、都江堰、青城山',budget:'每日约 300-500 元（含住宿餐饮交通）',bestTime:'3-6月 / 9-11月，春秋最佳',tips:['建议预留至少3天','火锅推荐晚上去本地人多的店','大熊猫基地早上8点前去','地铁覆盖广，出行方便'] },
    { city:'大理',emoji:'🏔️',province:'云南省',rating:'4.7',bg:'linear-gradient(135deg,#667eea,#764ba2)',desc:'大理，风花雪月的代名词。苍山十九峰与洱海交相辉映，白族古城中保留着最纯粹的慢生活气息。',food:'乳扇、饵丝、鲜花饼、凉鸡米线、酸辣鱼、白族三道茶',attractions:'洱海环湖、大理古城、苍山索道、双廊古镇、崇圣寺三塔、喜洲古镇',budget:'每日约 200-400 元',bestTime:'3-5月 / 9-11月',tips:['环洱海建议租电动车或自驾','古城内住宿淡季性价比高','注意防晒，高原紫外线强','可以住一晚海景客栈'] },
    { city:'西安',emoji:'🏯',province:'陕西省',rating:'4.9',bg:'linear-gradient(135deg,#f093fb,#f5576c)',desc:'十三朝古都西安，承载着中华文明最辉煌的篇章。兵马俑、城墙、大雁塔……每一处都是活着的历史。',food:'肉夹馍、羊肉泡馍、凉皮、biangbiang面、灌汤包、甑糕',attractions:'兵马俑、华清宫、大雁塔、古城墙、回民街、陕西历史博物馆、大唐不夜城',budget:'每日约 300-500 元',bestTime:'3-5月 / 9-11月',tips:['兵马俑建议请讲解员','城墙可以租自行车骑行','回民街周边小巷子才是本地人去的','陕西历史博物馆需提前预约'] },
    { city:'厦门',emoji:'🌊',province:'福建省',rating:'4.6',bg:'linear-gradient(135deg,#4facfe,#00f2fe)',desc:'厦门，一座充满文艺气息的海滨城市。鼓浪屿的琴声、曾厝垵的烟火、环岛路的海风，处处是浪漫。',food:'沙茶面、海蛎煎、土笋冻、姜母鸭、花生汤、烧仙草',attractions:'鼓浪屿、南普陀寺、曾厝垵、环岛路、厦门大学、中山路步行街',budget:'每日约 250-450 元',bestTime:'3-5月 / 10-12月',tips:['鼓浪屿船票需提前网上购买','厦门大学需预约参观','环岛路适合骑行','建议安排2-3天'] }
  ] }},
  computed: { filteredGuides() { if(!this.search) return this.guides; const s=this.search.toLowerCase(); return this.guides.filter(g=>g.city.includes(s)||g.province.includes(s)||g.desc.includes(s)) } },
  mounted() { const t=localStorage.getItem('theme');this.isDark=t?t==='dark':false;this.applyTheme() },
  methods: { toggleTheme(){this.isDark=!this.isDark;this.applyTheme();localStorage.setItem('theme',this.isDark?'dark':'light')}, applyTheme(){this.isDark?document.documentElement.classList.add('dark-mode'):document.documentElement.classList.remove('dark-mode')} }
}
</script>

<style scoped>
:root{--bg-primary:#fff;--bg-secondary:#fff;--bg-nav:rgba(255,255,255,0.95);--bg-card:rgba(255,255,255,0.95);--text-primary:#1e293b;--text-secondary:#64748b;--border-color:rgba(226,232,240,0.8);--shadow-color:rgba(0,0,0,0.05);--primary-color:#10B981;--secondary-color:#3B82F6;}
html.dark-mode{--bg-primary:#020617;--bg-secondary:#0f172a;--bg-nav:rgba(15,23,42,0.95);--bg-card:rgba(30,41,59,0.98);--text-primary:#fff;--text-secondary:#e2e8f0;--border-color:rgba(255,255,255,0.15);--shadow-color:rgba(0,0,0,0.3);--primary-color:#60a5fa;--secondary-color:#a78bfa;}
.page-container{min-height:100vh;background:var(--bg-primary);}
.nav-bar{position:fixed;top:0;left:0;right:0;z-index:1000;display:flex;align-items:center;justify-content:space-between;padding:1rem 2rem;background:var(--bg-nav);backdrop-filter:blur(20px);border-bottom:1px solid var(--border-color);box-shadow:0 4px 20px var(--shadow-color);}
.nav-brand{display:flex;align-items:center;gap:0.75rem;}
.brand-icon{width:40px;height:40px;background:linear-gradient(135deg,#10B981,#059669);border-radius:12px;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 12px rgba(16,185,129,0.3);}
.icon-svg{width:24px;height:24px;color:white;}
.brand-text-link{text-decoration:none;}
.brand-text{font-size:1.5rem;font-weight:700;color:var(--text-primary);letter-spacing:-0.5px;}
.brand-highlight{background:linear-gradient(135deg,#10B981,#3B82F6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.nav-links{display:flex;gap:2rem;}
.nav-link{font-size:0.95rem;font-weight:500;color:var(--text-secondary);text-decoration:none;transition:color 0.3s;position:relative;}
.nav-link:hover,.nav-link.router-link-exact-active{color:var(--primary-color);}
.nav-link::after{content:'';position:absolute;bottom:-4px;left:0;width:0;height:2px;background:linear-gradient(90deg,#10B981,#3B82F6);transition:width 0.3s;}
.nav-link:hover::after,.nav-link.router-link-exact-active::after{width:100%;}
.nav-actions{display:flex;gap:0.75rem;}
.btn{padding:0.6rem 1.25rem;border-radius:9999px;font-size:0.9rem;font-weight:600;cursor:pointer;transition:all 0.3s;border:none;}
.btn-outline{background:transparent;border:1.5px solid var(--border-color);color:var(--text-primary);}
.btn-outline:hover{border-color:var(--primary-color);color:var(--primary-color);}
.theme-toggle{padding:0.6rem;min-width:auto;border-radius:50%;display:flex;align-items:center;justify-content:center;}
.theme-toggle svg{width:20px;height:20px;}
.btn-primary{background:linear-gradient(135deg,#10B981,#059669);color:white;box-shadow:0 4px 14px rgba(16,185,129,0.35);}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 6px 20px rgba(16,185,129,0.45);}
.page-hero{position:relative;padding:9rem 2rem 4rem;text-align:center;overflow:hidden;}
.hero-gradient{position:absolute;inset:0;background:linear-gradient(135deg,#ecfdf5 0%,#dbeafe 30%,#ede9fe 60%,#fce7f3 100%);}
html.dark-mode .hero-gradient{background:linear-gradient(135deg,#0f172a 0%,#1e293b 50%,#334155 100%);}
.hero-content{position:relative;z-index:10;}
.page-title{font-size:clamp(2.5rem,5vw,3.5rem);font-weight:700;color:#1e293b;margin-bottom:1rem;font-family:'Georgia',serif;}
html.dark-mode .page-title{color:#fff;}
.gradient-text{background:linear-gradient(135deg,#10B981,#3B82F6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
html.dark-mode .gradient-text{background:linear-gradient(135deg,#6ee7b7,#60a5fa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.page-subtitle{font-size:1.15rem;color:#64748b;max-width:600px;margin:0 auto 1.5rem;}
html.dark-mode .page-subtitle{color:#94a3b8;}
.search-bar{max-width:500px;margin:0 auto;}
.search-input{width:100%;padding:0.8rem 1.2rem;border-radius:50px;border:1px solid var(--border-color);background:var(--bg-card);color:var(--text-primary);font-size:1rem;outline:none;box-shadow:0 4px 16px var(--shadow-color);box-sizing:border-box;transition:all 0.3s;}
.search-input:focus{border-color:var(--primary-color);box-shadow:0 4px 16px var(--shadow-color),0 0 0 3px rgba(16,185,129,0.15);}
.content-section{padding:3rem 2rem 4rem;}
.section-inner{max-width:900px;margin:0 auto;}
.guide-list{display:flex;flex-direction:column;gap:1.5rem;}
.guide-card{border-radius:1.5rem;overflow:hidden;background:var(--bg-card);border:1px solid var(--border-color);transition:all 0.4s;}
.guide-card:hover{box-shadow:0 16px 32px -8px var(--shadow-color);}
.guide-header{padding:1.5rem 2rem;display:flex;align-items:center;gap:1rem;}
.guide-emoji{font-size:2.5rem;}
.guide-meta h2{font-size:1.4rem;color:#fff;margin:0;}
.guide-badge{background:rgba(255,255,255,0.2);color:#fff;padding:0.15rem 0.6rem;border-radius:20px;font-size:0.75rem;}
.guide-rating{margin-left:auto;font-size:1.1rem;}
.guide-body{padding:1.5rem 2rem 2rem;}
.guide-desc{color:var(--text-secondary);line-height:1.7;margin-bottom:1.5rem;}
.guide-sections{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-bottom:1.5rem;}
.guide-section{background:var(--bg-primary);border-radius:12px;padding:1rem;border:1px solid var(--border-color);}
.guide-section h4{color:var(--primary-color);font-size:0.85rem;margin-bottom:0.4rem;}
.guide-section p{color:var(--text-secondary);font-size:0.85rem;line-height:1.5;}
.guide-tips{margin-bottom:1.5rem;}
.guide-tips h4{color:#F59E0B;font-size:0.9rem;margin-bottom:0.5rem;}
.guide-tips ul{list-style:none;padding:0;}
.guide-tips li{color:var(--text-secondary);font-size:0.85rem;padding:0.25rem 0;}
.guide-tips li::before{content:'• ';color:var(--primary-color);}
.plan-btn{width:100%;padding:0.9rem;border:none;border-radius:12px;background:linear-gradient(135deg,#10B981,#059669);color:#fff;font-size:1rem;font-weight:600;cursor:pointer;transition:all 0.3s;}
.plan-btn:hover{transform:translateY(-2px);box-shadow:0 8px 20px rgba(16,185,129,0.35);}
.empty-msg{text-align:center;color:var(--text-secondary);padding:3rem;font-size:1.1rem;}
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
@media(max-width:768px){.nav-links{display:none;}.guide-sections{grid-template-columns:1fr;}.footer-content{grid-template-columns:1fr;gap:2rem;}.footer-links{grid-template-columns:repeat(2,1fr);}}

.hamburger{display:none;flex-direction:column;gap:5px;padding:0.5rem;cursor:pointer;background:none;border:none;}
.hamburger span{display:block;width:22px;height:2px;background:var(--text-primary);border-radius:2px;transition:all 0.3s;}
.hamburger.active span:nth-child(1){transform:rotate(45deg) translate(5px,5px);}
.hamburger.active span:nth-child(2){opacity:0;}
.hamburger.active span:nth-child(3){transform:rotate(-45deg) translate(5px,-5px);}
.mobile-menu{display:none;}
</style>
