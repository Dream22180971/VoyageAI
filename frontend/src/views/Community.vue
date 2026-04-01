<template>
  <div class="page-container">
    <nav class="nav-bar">
      <div class="nav-brand"><div class="brand-icon"><svg class="icon-svg" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/><ellipse cx="12" cy="12" rx="4" ry="10" stroke="currentColor" stroke-width="2"/><path d="M2 12H22" stroke="currentColor" stroke-width="2"/></svg></div><router-link to="/" class="brand-text-link"><span class="brand-text">Voyage<span class="brand-highlight">AI</span></span></router-link></div>
      <div class="nav-links"><router-link to="/" class="nav-link">首页</router-link><router-link to="/inspiration" class="nav-link">发现灵感</router-link><router-link to="/guide" class="nav-link">目的地指南</router-link><router-link to="/community" class="nav-link">社区足迹</router-link><router-link to="/about" class="nav-link">关于我们</router-link></div>
      <div class="nav-actions"><button class="btn btn-outline theme-toggle" @click="toggleTheme"><svg v-if="!isDark" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg><svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/></svg></button><button class="btn btn-primary">开启探索</button></div>
    </nav>

    <section class="page-hero"><div class="hero-gradient"></div><div class="hero-content">
      <h1 class="page-title serif">🌏 <span class="gradient-text">社区足迹</span></h1>
      <p class="page-subtitle">看看旅行者们都在哪里留下故事</p>
    </div></section>

    <section class="content-section">
      <div class="section-inner">
        <div class="stats-bar">
          <div class="stat" v-for="s in stats" :key="s.label"><div class="stat-num">{{ s.num }}</div><div class="stat-label">{{ s.label }}</div></div>
        </div>
        <h2 class="section-title">📝 旅行故事</h2>
        <div class="stories">
          <div class="story-card glass-card" v-for="story in stories" :key="story.id">
            <div class="story-header"><div class="avatar" :style="{background:story.avatarBg}">{{ story.avatar }}</div><div class="story-meta"><strong>{{ story.author }}</strong><span>{{ story.time }}</span></div></div>
            <div class="story-body"><h3>{{ story.title }}</h3><p>{{ story.content }}</p></div>
            <div class="story-footer"><div class="story-tags"><span class="tag" v-for="tag in story.tags" :key="tag">#{{ tag }}</span></div><div class="story-actions"><span class="action">❤️ {{ story.likes }}</span><span class="action">💬 {{ story.comments }}</span></div></div>
          </div>
        </div>
        <h2 class="section-title">🏆 活跃旅行者</h2>
        <div class="ranking">
          <div class="rank-item glass-card" v-for="(user,i) in topUsers" :key="user.name">
            <span class="rank-num" :class="{top3:i<3}">{{ i+1 }}</span>
            <div class="rank-avatar" :style="{background:user.bg}">{{ user.avatar }}</div>
            <div class="rank-info"><strong>{{ user.name }}</strong><span>{{ user.cities }} 个城市 · {{ user.trips }} 次行程</span></div>
            <span class="rank-badge">{{ user.badge }}</span>
          </div>
        </div>
        <h2 class="section-title">🔥 热门话题</h2>
        <div class="topics">
          <div class="topic-tag glass-card" v-for="t in topics" :key="t.name"><span class="topic-name">#{{ t.name }}</span><span class="topic-count">{{ t.count }} 篇</span></div>
        </div>
      </div>
    </section>

    <footer class="footer">
      <div class="footer-content">
        <div class="footer-brand"><div class="brand-header"><div class="brand-icon"><svg class="icon-svg" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/><ellipse cx="12" cy="12" rx="4" ry="10" stroke="currentColor" stroke-width="2"/><path d="M2 12H22" stroke="currentColor" stroke-width="2"/></svg></div><router-link to="/" class="brand-text-link"><span class="brand-text">Voyage<span class="brand-highlight">AI</span></span></router-link></div><p class="brand-desc">成立于 2026 年，致力于利用先进的 AI 技术为旅行者提供最纯粹的灵感发现体验。</p></div>
        <div class="footer-links"><div class="link-group"><h4 class="link-title">产品</h4><router-link to="/" class="footer-link">行程规划</router-link><router-link to="/inspiration" class="footer-link">智能推荐</router-link><router-link to="/guide" class="footer-link">预算分析</router-link><router-link to="/community" class="footer-link">行前清单</router-link></div><div class="link-group"><h4 class="link-title">资源</h4><router-link to="/guide" class="footer-link">目的地指南</router-link><router-link to="/inspiration" class="footer-link">旅行灵感</router-link><router-link to="/community" class="footer-link">社区故事</router-link><router-link to="/about" class="footer-link">旅行攻略</router-link></div><div class="link-group"><h4 class="link-title">公司</h4><router-link to="/about" class="footer-link">关于我们</router-link><router-link to="/about" class="footer-link">联系我们</router-link><router-link to="/about" class="footer-link">隐私政策</router-link><router-link to="/about" class="footer-link">服务条款</router-link></div></div>
      </div>
      <div class="footer-bottom"><p class="copyright">© 2026 VoyageAI — 智能旅行规划系统</p></div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'Community',
  data() { return { isDark: false, stats: [
    {num:'12,847',label:'旅行者'},{num:'38,291',label:'行程方案'},{num:'5,632',label:'旅行故事'},{num:'218',label:'覆盖城市'}
  ], stories: [
    {id:1,author:'行者无疆',avatar:'🧑',avatarBg:'linear-gradient(135deg,#667eea,#764ba2)',time:'2天前',title:'大理7天深度游——我找到了理想的慢生活',content:'离开大理的那天，我在洱海边坐了很久。苍山的云在头顶飘过，白族老阿妈在旁边卖着鲜花饼。这次AI帮我规划了7天行程，完美避开了人潮，体验了最地道的大理生活。',tags:['大理','慢旅行','7天行程'],likes:234,comments:45},
    {id:2,author:'吃货小分队',avatar:'👩',avatarBg:'linear-gradient(135deg,#f093fb,#f5576c)',time:'5天前',title:'成都美食地图——跟着AI吃遍锦官城',content:'用 VoyageAI 规划了成都4天美食之旅，从玉林路的小酒馆到建设路的夜市，每一家都没踩雷。最惊喜的是 AI 推荐的一家隐藏在巷子里的苍蝇馆子，老板嬢嬢做的脑花绝了！',tags:['成都','美食','4天行程'],likes:189,comments:32},
    {id:3,author:'背包客老张',avatar:'👨',avatarBg:'linear-gradient(135deg,#43e97b,#38f9d7)',time:'1周前',title:'带着爸妈游西安——科技与温情的碰撞',content:'第一次用 AI 做攻略就带爸妈出行，本来很忐忑。结果 VoyageAI 把行程安排得张弛有度，充分考虑了老年人的体力和节奏。爸说：「这个AI比你靠谱」。',tags:['西安','亲子','孝心旅行'],likes:567,comments:89}
  ], topUsers: [
    {name:'行者无疆',avatar:'🧑',bg:'linear-gradient(135deg,#667eea,#764ba2)',cities:86,trips:127,badge:'🌍 环球旅行家'},
    {name:'吃货小分队',avatar:'👩',bg:'linear-gradient(135deg,#f093fb,#f5576c)',cities:52,trips:98,badge:'🍜 美食猎人'},
    {name:'背包客老张',avatar:'👨',bg:'linear-gradient(135deg,#43e97b,#38f9d7)',cities:45,trips:76,badge:'🎒 资深背包客'},
    {name:'摄影阿杰',avatar:'🧔',bg:'linear-gradient(135deg,#4facfe,#00f2fe)',cities:38,trips:65,badge:'📸 摄影达人'},
    {name:'慢旅小鹿',avatar:'👧',bg:'linear-gradient(135deg,#fa709a,#fee140)',cities:29,trips:43,badge:'🌸 文艺旅人'}
  ], topics: [
    {name:'一个人旅行',count:1234},{name:'穷游攻略',count:987},{name:'亲子出行',count:856},{name:'美食地图',count:743},
    {name:'古镇慢生活',count:621},{name:'自驾游',count:589},{name:'旅行摄影',count:478},{name:'AI旅行攻略',count:367}
  ] }},
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
.page-subtitle{font-size:1.15rem;color:#64748b;max-width:600px;margin:0 auto;}
html.dark-mode .page-subtitle{color:#94a3b8;}
.content-section{padding:3rem 2rem 4rem;}
.section-inner{max-width:900px;margin:0 auto;}
.section-title{font-size:1.6rem;font-weight:700;color:var(--text-primary);text-align:center;margin-bottom:1.5rem;}
.stats-bar{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;background:var(--bg-card);border:1px solid var(--border-color);border-radius:1.2rem;padding:2rem;margin-bottom:3rem;}
.stat{text-align:center;}
.stat-num{font-size:1.6rem;font-weight:800;background:linear-gradient(135deg,#10B981,#3B82F6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.stat-label{font-size:0.8rem;color:var(--text-secondary);margin-top:0.3rem;}
.stories{display:flex;flex-direction:column;gap:1.2rem;}
.story-card{background:var(--bg-card);border:1px solid var(--border-color);border-radius:1.2rem;padding:1.5rem;transition:all 0.4s;}
.story-card:hover{box-shadow:0 12px 24px -6px var(--shadow-color);}
.story-header{display:flex;align-items:center;gap:0.8rem;margin-bottom:1rem;}
.avatar{width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.2rem;color:#fff;}
.story-meta strong{color:var(--text-primary);display:block;font-size:0.9rem;}
.story-meta span{color:var(--text-secondary);font-size:0.75rem;}
.story-body h3{color:var(--text-primary);font-size:1.05rem;margin-bottom:0.5rem;}
.story-body p{color:var(--text-secondary);font-size:0.9rem;line-height:1.7;}
.story-footer{display:flex;justify-content:space-between;align-items:center;margin-top:1rem;padding-top:0.8rem;border-top:1px solid var(--border-color);}
.story-tags{display:flex;gap:0.5rem;}
.tag{background:rgba(16,185,129,0.1);color:var(--primary-color);padding:0.15rem 0.5rem;border-radius:20px;font-size:0.75rem;}
.story-actions{display:flex;gap:1rem;}
.action{color:var(--text-secondary);font-size:0.85rem;}
.ranking{display:flex;flex-direction:column;gap:0.6rem;}
.rank-item{display:flex;align-items:center;gap:1rem;background:var(--bg-card);border:1px solid var(--border-color);border-radius:12px;padding:1rem 1.2rem;transition:all 0.3s;}
.rank-item:hover{box-shadow:0 8px 16px -4px var(--shadow-color);}
.rank-num{width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.85rem;font-weight:700;color:var(--text-secondary);background:var(--bg-primary);}
.rank-num.top3{background:linear-gradient(135deg,#10B981,#3B82F6);color:#fff;}
.rank-avatar{width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1rem;color:#fff;}
.rank-info strong{color:var(--text-primary);display:block;font-size:0.9rem;}
.rank-info span{color:var(--text-secondary);font-size:0.75rem;}
.rank-badge{margin-left:auto;font-size:0.8rem;color:#F59E0B;}
.topics{display:flex;flex-wrap:wrap;gap:0.8rem;}
.topic-tag{background:var(--bg-card);border:1px solid var(--border-color);border-radius:50px;padding:0.6rem 1.2rem;display:flex;align-items:center;gap:0.6rem;cursor:pointer;transition:all 0.3s;}
.topic-tag:hover{box-shadow:0 8px 16px -4px var(--shadow-color);transform:translateY(-2px);}
.topic-name{color:var(--text-primary);font-size:0.9rem;}
.topic-count{color:var(--text-secondary);font-size:0.75rem;}
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
@media(max-width:768px){.nav-links{display:none;}.stats-bar{grid-template-columns:1fr 1fr;}.footer-content{grid-template-columns:1fr;gap:2rem;}.footer-links{grid-template-columns:repeat(2,1fr);}}
</style>
