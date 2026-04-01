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
          <router-link to="/inspiration" class="nav-link">灵感发现</router-link>
          <router-link to="/guide" class="nav-link active">目的地指南</router-link>
          <router-link to="/community" class="nav-link">社区足迹</router-link>
          <router-link to="/about" class="nav-link">关于我们</router-link>
        </div>
      </div>
    </nav>

    <section class="hero">
      <h1 class="hero-title">📖 <span class="highlight">目的地指南</span></h1>
      <p class="hero-subtitle">出发前必看，深度了解你的下一站</p>
      <div class="search-bar">
        <input v-model="search" placeholder="搜索目的地..." class="search-input" />
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="guide-list">
          <div class="guide-card" v-for="g in filteredGuides" :key="g.city">
            <div class="guide-header" :style="{ background: g.bg }">
              <span class="guide-emoji">{{ g.emoji }}</span>
              <div class="guide-meta">
                <h2>{{ g.city }}</h2>
                <span class="guide-badge">{{ g.province }}</span>
              </div>
              <div class="guide-rating">⭐ {{ g.rating }}</div>
            </div>
            <div class="guide-body">
              <p class="guide-desc">{{ g.desc }}</p>
              <div class="guide-sections">
                <div class="guide-section">
                  <h4>🍜 必吃美食</h4>
                  <p>{{ g.food }}</p>
                </div>
                <div class="guide-section">
                  <h4>📷 必去景点</h4>
                  <p>{{ g.attractions }}</p>
                </div>
                <div class="guide-section">
                  <h4>💰 人均预算</h4>
                  <p>{{ g.budget }}</p>
                </div>
                <div class="guide-section">
                  <h4>📅 最佳时间</h4>
                  <p>{{ g.bestTime }}</p>
                </div>
              </div>
              <div class="guide-tips">
                <h4>💡 小贴士</h4>
                <ul>
                  <li v-for="tip in g.tips" :key="tip">{{ tip }}</li>
                </ul>
              </div>
              <button class="plan-btn" @click="planTrip(g.city)">🤖 AI 规划此行程</button>
            </div>
          </div>
        </div>
        <p v-if="filteredGuides.length === 0" class="empty">没有找到匹配的目的地 😢</p>
      </div>
    </section>

    <footer class="footer">
      <div class="container"><p>© 2026 VoyageAI — 智能旅行规划系统</p></div>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const search = ref('')
const planTrip = (city) => { router.push('/') }

const guides = [
  {
    city: '成都', emoji: '🐼', province: '四川省', rating: '4.8',
    bg: 'linear-gradient(135deg, #a18cd1, #fbc2eb)',
    desc: '成都，一座来了就不想走的城市。这里有憨态可掬的大熊猫，有麻辣鲜香的火锅，有悠闲的茶馆文化，还有璀璨的三千年历史。',
    food: '火锅、串串香、担担面、龙抄手、钟水饺、兔头、钵钵鸡',
    attractions: '大熊猫繁育基地、宽窄巷子、武侯祠、锦里、都江堰、青城山',
    budget: '每日约 300-500 元（含住宿餐饮交通）',
    bestTime: '3-6月 / 9-11月，春秋最佳',
    tips: ['建议预留至少3天', '火锅推荐晚上去本地人多的店', '大熊猫基地早上8点前去，熊猫最活跃', '地铁覆盖广，出行方便']
  },
  {
    city: '大理', emoji: '🏔️', province: '云南省', rating: '4.7',
    bg: 'linear-gradient(135deg, #667eea, #764ba2)',
    desc: '大理，风花雪月的代名词。苍山十九峰与洱海交相辉映，白族古城中保留着最纯粹的慢生活气息。',
    food: '乳扇、饵丝、鲜花饼、凉鸡米线、酸辣鱼、白族三道茶',
    attractions: '洱海环湖、大理古城、苍山索道、双廊古镇、崇圣寺三塔、喜洲古镇',
    budget: '每日约 200-400 元',
    bestTime: '3-5月 / 9-11月',
    tips: ['环洱海建议租电动车或自驾', '古城内住宿选择很多，淡季性价比高', '注意防晒，高原紫外线强', '可以住一晚海景客栈']
  },
  {
    city: '西安', emoji: '🏯', province: '陕西省', rating: '4.9',
    bg: 'linear-gradient(135deg, #f093fb, #f5576c)',
    desc: '十三朝古都西安，承载着中华文明最辉煌的篇章。兵马俑、城墙、大雁塔……每一处都是活着的历史。',
    food: '肉夹馍、羊肉泡馍、凉皮、biangbiang面、灌汤包、甑糕',
    attractions: '兵马俑、华清宫、大雁塔、古城墙、回民街、陕西历史博物馆、大唐不夜城',
    budget: '每日约 300-500 元',
    bestTime: '3-5月 / 9-11月',
    tips: ['兵马俑建议请讲解员或租语音导览', '城墙可以租自行车骑行一圈', '回民街周边小巷子才是本地人去的', '陕西历史博物馆需提前预约']
  },
  {
    city: '厦门', emoji: '🌊', province: '福建省', rating: '4.6',
    bg: 'linear-gradient(135deg, #4facfe, #00f2fe)',
    desc: '厦门，一座充满文艺气息的海滨城市。鼓浪屿的琴声、曾厝垵的烟火、环岛路的海风，处处是浪漫。',
    food: '沙茶面、海蛎煎、土笋冻、姜母鸭、花生汤、烧仙草',
    attractions: '鼓浪屿、南普陀寺、曾厝垵、环岛路、厦门大学、中山路步行街',
    budget: '每日约 250-450 元',
    bestTime: '3-5月 / 10-12月',
    tips: ['鼓浪屿船票需提前网上购买', '厦门大学需预约参观', '环岛路适合骑行，沿途风景绝美', '建议安排2-3天']
  },
]

const filteredGuides = computed(() => {
  if (!search.value) return guides
  const s = search.value.toLowerCase()
  return guides.filter(g =>
    g.city.includes(s) || g.province.includes(s) || g.food.includes(s) || g.desc.includes(s)
  )
})
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
.hero-subtitle { color: #a0a0a0; font-size: 1.1rem; margin-bottom: 1.5rem; }
.search-bar { max-width: 500px; margin: 0 auto; }
.search-input { width: 100%; padding: 0.8rem 1.2rem; border-radius: 50px; border: 1px solid rgba(255,255,255,0.1); background: rgba(255,255,255,0.06); color: #fff; font-size: 1rem; outline: none; box-sizing: border-box; }
.search-input::placeholder { color: #666; }
.search-input:focus { border-color: #667eea; }
.section { padding: 2rem 2rem 3rem; }
.container { max-width: 900px; margin: 0 auto; }
.guide-list { display: flex; flex-direction: column; gap: 1.5rem; }
.guide-card { border-radius: 16px; overflow: hidden; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); }
.guide-header { padding: 1.5rem 2rem; display: flex; align-items: center; gap: 1rem; }
.guide-emoji { font-size: 2.5rem; }
.guide-meta h2 { font-size: 1.4rem; color: #fff; margin: 0; }
.guide-badge { background: rgba(255,255,255,0.2); color: #fff; padding: 0.15rem 0.6rem; border-radius: 20px; font-size: 0.75rem; }
.guide-rating { margin-left: auto; font-size: 1.1rem; }
.guide-body { padding: 1.5rem 2rem 2rem; }
.guide-desc { color: #b0b0b0; line-height: 1.7; margin-bottom: 1.5rem; }
.guide-sections { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1.5rem; }
.guide-section { background: rgba(255,255,255,0.03); border-radius: 10px; padding: 1rem; }
.guide-section h4 { color: #667eea; font-size: 0.85rem; margin-bottom: 0.4rem; }
.guide-section p { color: #a0a0a0; font-size: 0.85rem; line-height: 1.5; }
.guide-tips { margin-bottom: 1.5rem; }
.guide-tips h4 { color: #f093fb; font-size: 0.9rem; margin-bottom: 0.5rem; }
.guide-tips ul { list-style: none; padding: 0; }
.guide-tips li { color: #a0a0a0; font-size: 0.85rem; padding: 0.25rem 0; }
.guide-tips li::before { content: '• '; color: #667eea; }
.plan-btn { width: 100%; padding: 0.9rem; border: none; border-radius: 12px; background: linear-gradient(135deg, #667eea, #764ba2); color: #fff; font-size: 1rem; font-weight: 600; cursor: pointer; transition: opacity 0.3s; }
.plan-btn:hover { opacity: 0.9; }
.empty { text-align: center; color: #666; padding: 3rem; }
.footer { padding: 2rem; text-align: center; border-top: 1px solid rgba(255,255,255,0.05); color: #606060; font-size: 0.85rem; }
@media (max-width: 768px) { .hero-title { font-size: 1.8rem; } .nav-links { gap: 0.5rem; } .nav-link { font-size: 0.75rem; } .guide-sections { grid-template-columns: 1fr; } }
</style>
