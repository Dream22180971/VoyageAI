<template>
  <div class="page">
    <nav class="navbar">
      <div class="nav-container">
        <router-link to="/" class="nav-logo">
          <span class="logo-icon">🗺️</span>
          <span class="logo-text">VoyageAI</span>
        </router-link>
        <div class="nav-links">
          <router-link to="/" class="nav-link">首页</router-link>
          <router-link to="/inspiration" class="nav-link active">灵感发现</router-link>
          <router-link to="/guide" class="nav-link">目的地指南</router-link>
          <router-link to="/community" class="nav-link">社区足迹</router-link>
          <router-link to="/about" class="nav-link">关于我们</router-link>
        </div>
      </div>
    </nav>

    <section class="hero">
      <h1 class="hero-title">✨ <span class="highlight">灵感发现</span></h1>
      <p class="hero-subtitle">不知道去哪？让灵感为你指引方向</p>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section-title">🌍 热门目的地</h2>
        <div class="card-grid">
          <div class="dest-card" v-for="dest in destinations" :key="dest.name" @click="goHome(dest.name)">
            <div class="dest-img" :style="{ background: dest.bg }">
              <span class="dest-emoji">{{ dest.emoji }}</span>
            </div>
            <div class="dest-info">
              <h3>{{ dest.name }}</h3>
              <p>{{ dest.desc }}</p>
              <div class="dest-tags">
                <span class="tag" v-for="tag in dest.tags" :key="tag">{{ tag }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <h2 class="section-title">🎯 主题旅行</h2>
        <div class="theme-grid">
          <div class="theme-card" v-for="theme in themes" :key="theme.title" @click="goHome(theme.title)">
            <span class="theme-icon">{{ theme.icon }}</span>
            <h3>{{ theme.title }}</h3>
            <p>{{ theme.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section-title">📅 最佳出行时间</h2>
        <div class="timeline">
          <div class="timeline-item" v-for="item in seasons" :key="item.month">
            <div class="timeline-month">{{ item.month }}</div>
            <div class="timeline-content">
              <strong>{{ item.dest }}</strong>
              <p>{{ item.reason }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <footer class="footer">
      <div class="container"><p>© 2026 VoyageAI — 智能旅行规划系统</p></div>
    </footer>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
const goHome = (dest) => { router.push('/') }

const destinations = [
  { name: '成都', emoji: '🐼', bg: 'linear-gradient(135deg, #a18cd1, #fbc2eb)', desc: '天府之国，美食与文化的天堂', tags: ['美食', '文化', '休闲'] },
  { name: '大理', emoji: '🏔️', bg: 'linear-gradient(135deg, #667eea, #764ba2)', desc: '风花雪月，苍山洱海的诗意栖居', tags: ['自然', '摄影', '文艺'] },
  { name: '西安', emoji: '🏯', bg: 'linear-gradient(135deg, #f093fb, #f5576c)', desc: '千年古都，历史的厚重回响', tags: ['历史', '美食', '人文'] },
  { name: '厦门', emoji: '🌊', bg: 'linear-gradient(135deg, #4facfe, #00f2fe)', desc: '海上花园，文艺小资的海滨城市', tags: ['海滨', '文艺', '美食'] },
  { name: '张家界', emoji: '⛰️', bg: 'linear-gradient(135deg, #43e97b, #38f9d7)', desc: '奇峰林立，现实版的阿凡达世界', tags: ['自然', '探险', '摄影'] },
  { name: '丽江', emoji: '🏘️', bg: 'linear-gradient(135deg, #fa709a, #fee140)', desc: '古城悠悠，雪山下的浪漫邂逅', tags: ['古城', '雪山', '民族'] },
]

const themes = [
  { icon: '🍜', title: '美食之旅', desc: '专程为一座城市的味道出发' },
  { icon: '⛰️', title: '户外探险', desc: '挑战自我，征服山川湖海' },
  { icon: '📸', title: '摄影采风', desc: '用镜头记录世间最美的风景' },
  { icon: '🏛️', title: '文化寻踪', desc: '穿越时空，感受历史与人文' },
  { icon: '🏖️', title: '海岛度假', desc: '阳光沙滩，享受慢时光' },
  { icon: '👨‍👩‍👧‍👦', title: '亲子出行', desc: '陪伴成长，探索世界的奇妙' },
]

const seasons = [
  { month: '3-5月', dest: '推荐：婺源、大理、张家界', reason: '春暖花开，油菜花海与山花烂漫' },
  { month: '6-8月', dest: '推荐：青海湖、呼伦贝尔、九寨沟', reason: '避暑胜地，草原辽阔湖光山色' },
  { month: '9-11月', dest: '推荐：北京、额济纳、稻城亚丁', reason: '秋高气爽，金秋色彩最浓郁' },
  { month: '12-2月', dest: '推荐：哈尔滨、三亚、丽江', reason: '冰雪世界或温暖避寒，各有精彩' },
]
</script>

<style scoped>
.page { min-height: 100vh; background: linear-gradient(135deg, #0f0c29 0%, #1a1a3e 50%, #24243e 100%); color: #e0e0e0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
.navbar { position: fixed; top: 0; left: 0; right: 0; z-index: 100; background: rgba(15,12,41,0.85); backdrop-filter: blur(20px); border-bottom: 1px solid rgba(255,255,255,0.08); }
.nav-container { max-width: 1200px; margin: 0 auto; padding: 0.8rem 2rem; display: flex; justify-content: space-between; align-items: center; }
.nav-logo { display: flex; align-items: center; gap: 0.5rem; text-decoration: none; font-size: 1.3rem; font-weight: 700; }
.logo-icon { font-size: 1.5rem; }
.logo-text { background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.nav-links { display: flex; gap: 1.2rem; }
.nav-link { color: #b0b0b0; text-decoration: none; font-size: 0.9rem; transition: color 0.3s; }
.nav-link:hover, .nav-link.active { color: #667eea; }
.hero { padding: 8rem 2rem 3rem; text-align: center; }
.hero-title { font-size: 2.5rem; font-weight: 800; margin-bottom: 0.8rem; color: #fff; }
.highlight { background: linear-gradient(135deg, #667eea, #764ba2, #f093fb); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.hero-subtitle { color: #a0a0a0; font-size: 1.1rem; }
.section { padding: 3rem 2rem; }
.section-alt { background: rgba(255,255,255,0.02); }
.container { max-width: 1000px; margin: 0 auto; }
.section-title { font-size: 1.6rem; font-weight: 700; text-align: center; margin-bottom: 2rem; color: #fff; }

.card-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.5rem; }
.dest-card { border-radius: 16px; overflow: hidden; cursor: pointer; transition: transform 0.3s; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); }
.dest-card:hover { transform: translateY(-4px); }
.dest-img { height: 120px; display: flex; align-items: center; justify-content: center; }
.dest-emoji { font-size: 3rem; }
.dest-info { padding: 1.2rem; }
.dest-info h3 { color: #fff; font-size: 1.1rem; margin-bottom: 0.3rem; }
.dest-info p { color: #909090; font-size: 0.85rem; margin-bottom: 0.8rem; }
.dest-tags { display: flex; gap: 0.5rem; }
.tag { background: rgba(102,126,234,0.2); color: #667eea; padding: 0.2rem 0.6rem; border-radius: 20px; font-size: 0.75rem; }

.theme-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.2rem; }
.theme-card { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 1.5rem; text-align: center; cursor: pointer; transition: transform 0.3s, background 0.3s; }
.theme-card:hover { transform: translateY(-3px); background: rgba(255,255,255,0.07); }
.theme-icon { font-size: 2rem; display: block; margin-bottom: 0.8rem; }
.theme-card h3 { color: #fff; font-size: 1rem; margin-bottom: 0.4rem; }
.theme-card p { color: #909090; font-size: 0.85rem; }

.timeline { max-width: 700px; margin: 0 auto; }
.timeline-item { display: flex; gap: 1.5rem; padding: 1rem 0; border-bottom: 1px solid rgba(255,255,255,0.05); }
.timeline-month { min-width: 80px; color: #667eea; font-weight: 700; font-size: 1rem; padding-top: 2px; }
.timeline-content strong { color: #d0d0d0; }
.timeline-content p { color: #909090; font-size: 0.9rem; margin-top: 0.2rem; }

.footer { padding: 2rem; text-align: center; border-top: 1px solid rgba(255,255,255,0.05); color: #606060; font-size: 0.85rem; }
@media (max-width: 768px) { .hero-title { font-size: 1.8rem; } .nav-links { gap: 0.5rem; } .nav-link { font-size: 0.75rem; } .card-grid { grid-template-columns: 1fr; } }
</style>
