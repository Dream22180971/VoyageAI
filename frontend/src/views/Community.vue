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
          <router-link to="/guide" class="nav-link">目的地指南</router-link>
          <router-link to="/community" class="nav-link active">社区足迹</router-link>
          <router-link to="/about" class="nav-link">关于我们</router-link>
        </div>
      </div>
    </nav>

    <section class="hero">
      <h1 class="hero-title">🌏 <span class="highlight">社区足迹</span></h1>
      <p class="hero-subtitle">看看旅行者们都在哪里留下故事</p>
    </section>

    <section class="section">
      <div class="container">
        <!-- 数据统计 -->
        <div class="stats-bar">
          <div class="stat" v-for="s in stats" :key="s.label">
            <div class="stat-num">{{ s.num }}</div>
            <div class="stat-label">{{ s.label }}</div>
          </div>
        </div>

        <!-- 旅行故事 -->
        <h2 class="section-title" style="margin-top:3rem">📝 旅行故事</h2>
        <div class="stories">
          <div class="story-card" v-for="story in stories" :key="story.id">
            <div class="story-header">
              <div class="avatar" :style="{ background: story.avatarBg }">{{ story.avatar }}</div>
              <div class="story-meta">
                <strong>{{ story.author }}</strong>
                <span>{{ story.time }}</span>
              </div>
            </div>
            <div class="story-body">
              <h3>{{ story.title }}</h3>
              <p>{{ story.content }}</p>
            </div>
            <div class="story-footer">
              <div class="story-tags">
                <span class="tag" v-for="tag in story.tags" :key="tag">#{{ tag }}</span>
              </div>
              <div class="story-actions">
                <span class="action">❤️ {{ story.likes }}</span>
                <span class="action">💬 {{ story.comments }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 旅行者排行 -->
        <h2 class="section-title" style="margin-top:3rem">🏆 活跃旅行者</h2>
        <div class="ranking">
          <div class="rank-item" v-for="(user, i) in topUsers" :key="user.name">
            <span class="rank-num" :class="{ top3: i < 3 }">{{ i + 1 }}</span>
            <div class="rank-avatar" :style="{ background: user.bg }">{{ user.avatar }}</div>
            <div class="rank-info">
              <strong>{{ user.name }}</strong>
              <span>{{ user.cities }} 个城市 · {{ user.trips }} 次行程</span>
            </div>
            <span class="rank-badge">{{ user.badge }}</span>
          </div>
        </div>

        <!-- 热门话题 -->
        <h2 class="section-title" style="margin-top:3rem">🔥 热门话题</h2>
        <div class="topics">
          <div class="topic-tag" v-for="t in topics" :key="t.name">
            <span class="topic-name">#{{ t.name }}</span>
            <span class="topic-count">{{ t.count }} 篇</span>
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
const stats = [
  { num: '12,847', label: '旅行者' },
  { num: '38,291', label: '行程方案' },
  { num: '5,632', label: '旅行故事' },
  { num: '218', label: '覆盖城市' },
]

const stories = [
  { id: 1, author: '行者无疆', avatar: '🧑', avatarBg: 'linear-gradient(135deg,#667eea,#764ba2)', time: '2天前', title: '大理7天深度游——我找到了理想的慢生活',
    content: '离开大理的那天，我在洱海边坐了很久。苍山的云在头顶飘过，白族老阿妈在旁边卖着鲜花饼。这次AI帮我规划了7天行程，完美避开了人潮，体验了最地道的大理生活。',
    tags: ['大理', '慢旅行', '7天行程'], likes: 234, comments: 45 },
  { id: 2, author: '吃货小分队', avatar: '👩', avatarBg: 'linear-gradient(135deg,#f093fb,#f5576c)', time: '5天前', title: '成都美食地图——跟着AI吃遍锦官城',
    content: '用 VoyageAI 规划了成都4天美食之旅，从玉林路的小酒馆到建设路的夜市，每一家都没踩雷。最惊喜的是 AI 推荐的一家隐藏在巷子里的苍蝇馆子，老板嬢嬢做的脑花绝了！',
    tags: ['成都', '美食', '4天行程'], likes: 189, comments: 32 },
  { id: 3, author: '背包客老张', avatar: '👨', avatarBg: 'linear-gradient(135deg,#43e97b,#38f9d7)', time: '1周前', title: '带着爸妈游西安——科技与温情的碰撞',
    content: '第一次用 AI 做攻略就带爸妈出行，本来很忐忑。结果 VoyageAI 把行程安排得张弛有度，充分考虑了老年人的体力和节奏。爸说：「这个AI比你靠谱」。',
    tags: ['西安', '亲子', '孝心旅行'], likes: 567, comments: 89 },
]

const topUsers = [
  { name: '行者无疆', avatar: '🧑', bg: 'linear-gradient(135deg,#667eea,#764ba2)', cities: 86, trips: 127, badge: '🌍 环球旅行家' },
  { name: '吃货小分队', avatar: '👩', bg: 'linear-gradient(135deg,#f093fb,#f5576c)', cities: 52, trips: 98, badge: '🍜 美食猎人' },
  { name: '背包客老张', avatar: '👨', bg: 'linear-gradient(135deg,#43e97b,#38f9d7)', cities: 45, trips: 76, badge: '🎒 资深背包客' },
  { name: '摄影阿杰', avatar: '🧔', bg: 'linear-gradient(135deg,#4facfe,#00f2fe)', cities: 38, trips: 65, badge: '📸 摄影达人' },
  { name: '慢旅小鹿', avatar: '👧', bg: 'linear-gradient(135deg,#fa709a,#fee140)', cities: 29, trips: 43, badge: '🌸 文艺旅人' },
]

const topics = [
  { name: '一个人旅行', count: 1234 },
  { name: '穷游攻略', count: 987 },
  { name: '亲子出行', count: 856 },
  { name: '美食地图', count: 743 },
  { name: '古镇慢生活', count: 621 },
  { name: '自驾游', count: 589 },
  { name: '旅行摄影', count: 478 },
  { name: 'AI旅行攻略', count: 367 },
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
.section { padding: 2rem 2rem 3rem; }
.container { max-width: 900px; margin: 0 auto; }
.section-title { font-size: 1.6rem; font-weight: 700; text-align: center; margin-bottom: 1.5rem; color: #fff; }

.stats-bar { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); border-radius: 16px; padding: 2rem; }
.stat { text-align: center; }
.stat-num { font-size: 1.6rem; font-weight: 800; background: linear-gradient(135deg, #667eea, #f093fb); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.stat-label { font-size: 0.8rem; color: #888; margin-top: 0.3rem; }

.stories { display: flex; flex-direction: column; gap: 1.2rem; }
.story-card { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 1.5rem; }
.story-header { display: flex; align-items: center; gap: 0.8rem; margin-bottom: 1rem; }
.avatar { width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; }
.story-meta strong { color: #fff; display: block; font-size: 0.9rem; }
.story-meta span { color: #666; font-size: 0.75rem; }
.story-body h3 { color: #fff; font-size: 1.05rem; margin-bottom: 0.5rem; }
.story-body p { color: #a0a0a0; font-size: 0.9rem; line-height: 1.7; }
.story-footer { display: flex; justify-content: space-between; align-items: center; margin-top: 1rem; padding-top: 0.8rem; border-top: 1px solid rgba(255,255,255,0.05); }
.story-tags { display: flex; gap: 0.5rem; }
.tag { background: rgba(102,126,234,0.15); color: #667eea; padding: 0.15rem 0.5rem; border-radius: 20px; font-size: 0.75rem; }
.story-actions { display: flex; gap: 1rem; }
.action { color: #888; font-size: 0.85rem; }

.ranking { display: flex; flex-direction: column; gap: 0.6rem; }
.rank-item { display: flex; align-items: center; gap: 1rem; background: rgba(255,255,255,0.03); border-radius: 12px; padding: 1rem 1.2rem; }
.rank-num { width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.85rem; font-weight: 700; color: #666; background: rgba(255,255,255,0.05); }
.rank-num.top3 { background: linear-gradient(135deg, #667eea, #764ba2); color: #fff; }
.rank-avatar { width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1rem; }
.rank-info strong { color: #fff; display: block; font-size: 0.9rem; }
.rank-info span { color: #888; font-size: 0.75rem; }
.rank-badge { margin-left: auto; font-size: 0.8rem; color: #f093fb; }

.topics { display: flex; flex-wrap: wrap; gap: 0.8rem; }
.topic-tag { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.08); border-radius: 50px; padding: 0.6rem 1.2rem; display: flex; align-items: center; gap: 0.6rem; cursor: pointer; transition: background 0.3s; }
.topic-tag:hover { background: rgba(255,255,255,0.08); }
.topic-name { color: #d0d0d0; font-size: 0.9rem; }
.topic-count { color: #666; font-size: 0.75rem; }

.footer { padding: 2rem; text-align: center; border-top: 1px solid rgba(255,255,255,0.05); color: #606060; font-size: 0.85rem; }
@media (max-width: 768px) { .hero-title { font-size: 1.8rem; } .stats-bar { grid-template-columns: 1fr 1fr; } .nav-links { gap: 0.5rem; } .nav-link { font-size: 0.75rem; } }
</style>
