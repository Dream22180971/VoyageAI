<template>
  <div class="result-container">
    <nav class="nav-bar">
      <div class="nav-brand">
        <div class="brand-icon"><svg class="icon-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 00-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z" fill="currentColor"/></svg></div>
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
        <button class="btn btn-outline" @click="goHome">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          返回首页
        </button>
        <button class="btn btn-primary" @click="exportResult">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>
          导出指南
        </button>
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

    <div class="result-content">
      <div class="overview-card glass-card">
        <div class="overview-image" :style="{ background: destGradient }">
          <span class="dest-emoji">{{ destEmoji }}</span>
          <div class="image-overlay">
            <span class="badge">AI 精选方案</span>
            <span class="date">{{ currentDate }} 生成</span>
          </div>
        </div>
        <div class="overview-info">
          <h1 class="overview-title serif">
            <span class="destination">{{ itinerary.overview?.destination || '目的地' }}</span>
            <span class="days">{{ itinerary.overview?.days || 0 }}</span>日深度发现之旅
          </h1>
          <div class="overview-stats">
            <div class="stat-item glass-card"><div class="stat-icon bg-emerald-light"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg></div><div class="stat-content"><span class="stat-label">行程天数</span><span class="stat-value">{{ itinerary.overview?.days || 0 }} 天</span></div></div>
            <div class="stat-item glass-card"><div class="stat-icon bg-amber-light"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="5" width="20" height="14" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/></svg></div><div class="stat-content"><span class="stat-label">预算范围</span><span class="stat-value">¥{{ itinerary.overview?.budget || 0 }}</span></div></div>
            <div class="stat-item glass-card"><div class="stat-icon bg-blue-light"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg></div><div class="stat-content"><span class="stat-label">最佳季节</span><span class="stat-value">{{ itinerary.overview?.best_season || '四季皆宜' }}</span></div></div>
            <div class="stat-item glass-card"><div class="stat-icon bg-purple-light"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg></div><div class="stat-content"><span class="stat-label">行程节奏</span><span class="stat-value">{{ itinerary.overview?.pace || '适中' }}</span></div></div>
          </div>
        </div>
      </div>

      <div class="main-grid">
        <div class="timeline-section glass-card">
          <div class="section-header"><h2 class="section-title"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>每日行程安排</h2></div>
          <div class="timeline">
            <div v-for="(day, index) in itinerary.daily_plan" :key="index" class="timeline-day" :style="{ animationDelay: index * 0.1 + 's' }">
              <div class="timeline-marker"><div class="marker-dot">{{ day.day }}</div><div class="marker-line" v-if="index < (itinerary.daily_plan?.length || 0) - 1"></div></div>
              <div class="timeline-content">
                <div class="day-header"><h3 class="day-title">第 {{ day.day }} 天</h3><span class="day-theme">{{ day.title }}</span></div>
                <div class="activities">
                  <div v-for="(activity, actIndex) in day.activities" :key="actIndex" class="activity-card glass-card card-hover">
                    <div class="activity-time"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>{{ activity.time }}</div>
                    <h4 class="activity-name">{{ activity.name || activity.title }}</h4>
                    <p class="activity-desc">{{ activity.description }}</p>
                    <div class="activity-tags" v-if="activity.tags"><span v-for="(tag, ti) in activity.tags" :key="ti" class="tag">{{ tag }}</span></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="sidebar">
          <div class="sidebar-card glass-card">
            <div class="card-header"><h3><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/></svg>实时天气</h3><span class="city">{{ itinerary.overview?.destination }}</span></div>
            <div class="weather-main"><div class="weather-temp">{{ weather.temperature }}°</div><div class="weather-info"><p class="weather-condition">{{ weather.condition }}</p><p class="weather-detail">{{ weather.detail }}</p></div><div class="weather-icon" :class="weather.iconClass"><svg viewBox="0 0 24 24" fill="currentColor"><path v-if="weather.icon === 'sun'" d="M12 7c-2.76 0-5 2.24-5 5s2.24 5 5 5 5-2.24 5-5-2.24-5-5-5zM2 13h2c.55 0 1-.45 1-1s-.45-1-1-1H2c-.55 0-1 .45-1 1s.45 1 1 1zm18 0h2c.55 0 1-.45 1-1s-.45-1-1-1h-2c-.55 0-1 .45-1 1s.45 1 1 1zM11 2v2c0 .55.45 1 1 1s1-.45 1-1V2c0-.55-.45-1-1-1s-1 .45-1 1zm0 18v2c0 .55.45 1 1 1s1-.45 1-1v-2c0-.55-.45-1-1-1s-1 .45-1 1z"/><path v-else d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96z"/></svg></div></div>
            <div class="weather-alert" v-if="weather.alert"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg><p>{{ weather.alert }}</p></div>
          </div>

          <div class="sidebar-card glass-card">
            <div class="card-header"><h3><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21.21 15.89A10 10 0 118 2.83M22 12A10 10 0 0012 2v10z"/></svg>智能预算分析</h3></div>
            <div class="budget-chart-container"><canvas ref="budgetChart" width="280" height="200"></canvas></div>
            <div class="budget-summary"><div class="budget-item"><span class="budget-label">预估总费用</span><span class="budget-value">¥{{ totalBudget }}</span></div></div>
          </div>

          <div class="sidebar-card glass-card">
            <div class="card-header"><h3><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/></svg>智能行前清单</h3></div>
            <div class="packing-list">
              <div v-for="(cat, ci) in packingList" :key="ci" class="packing-category"><h4 class="category-title">{{ cat.name }}</h4><div class="category-items"><label v-for="(item, ii) in cat.items" :key="ii" class="packing-item"><input type="checkbox" v-model="item.checked" class="custom-checkbox"><span class="item-name" :class="{ checked: item.checked }">{{ item.name }}</span></label></div></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <footer class="footer">
      <div class="footer-content">
        <div class="footer-brand">
          <div class="brand-header"><div class="brand-icon"><svg class="icon-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 00-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z" fill="currentColor"/></svg></div><router-link to="/" class="brand-text-link"><span class="brand-text">Voyage<span class="brand-highlight">AI</span></span></router-link></div>
          <p class="brand-desc">成立于 2026 年，致力于利用先进的 AI 技术为旅行者提供最纯粹的灵感发现体验。</p>
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
import axios from 'axios'
import html2canvas from 'html2canvas'
export default {
  name: 'Result',
  data() {
    return {
      isDark: false,
      menuOpen: false,
      itinerary: {},
      weather: { temperature: 22, condition: '多云转晴', detail: '加载中...', icon: 'sun', iconClass: 'sunny', alert: '' },
      packingList: [
        { name: '🪪 证件与财务', items: [{ name: '身份证/护照', checked: false }, { name: '驾驶证', checked: false }, { name: '现金与银行卡', checked: false }] },
        { name: '📱 电子设备', items: [{ name: '手机与充电器', checked: false }, { name: '相机与存储卡', checked: false }, { name: '充电宝', checked: false }] },
        { name: '🧳 个人用品', items: [{ name: '洗漱用品', checked: false }, { name: '防晒霜', checked: false }, { name: '常用药品', checked: false }] }
      ]
    }
  },
  computed: {
    currentDate() { const d = new Date(); return `${d.getFullYear()}.${String(d.getMonth()+1).padStart(2,'0')}.${String(d.getDate()).padStart(2,'0')}` },
    destinationImage() {
      return ''
    },
    destGradient() {
      const gradients = {
        '北京': 'linear-gradient(135deg, #ff6b35, #f7c59f, #efefd0)',
        '上海': 'linear-gradient(135deg, #667eea, #764ba2, #f093fb)',
        '杭州': 'linear-gradient(135deg, #43e97b, #38f9d7, #a8edea)',
        '成都': 'linear-gradient(135deg, #a18cd1, #fbc2eb, #f6d5f7)',
        '西安': 'linear-gradient(135deg, #f093fb, #f5576c, #fda085)',
        '南京': 'linear-gradient(135deg, #4facfe, #00f2fe, #43e97b)',
        '广州': 'linear-gradient(135deg, #fa709a, #fee140, #fda085)',
        '深圳': 'linear-gradient(135deg, #6ee7b7, #3b82f6, #a78bfa)',
        '重庆': 'linear-gradient(135deg, #f97316, #ef4444, #ec4899)',
        '厦门': 'linear-gradient(135deg, #4facfe, #00f2fe, #667eea)',
      }
      const dest = this.itinerary.overview?.destination || ''
      return gradients[dest] || 'linear-gradient(135deg, #10B981, #3B82F6, #8B5CF6)'
    },
    destEmoji() {
      const emojis = { '北京':'🏛️','上海':'🌆','杭州':'🌿','成都':'🐼','西安':'⚔️','南京':'🏯','广州':'🌺','深圳':'💎','重庆':'🌶️','厦门':'🌊','丽江':'🏘️','大理':'🏔️','张家界':'⛰️','三亚':'🏖️','青岛':'🍺','苏州':'🎐','厦门':'🌊','哈尔滨':'❄️' }
      return emojis[this.itinerary.overview?.destination] || '✈️'
    },
    totalBudget() {
      if (!this.itinerary.budget_breakdown) return 0
      return this.itinerary.budget_breakdown.reduce((s, i) => { const a = typeof i.amount==='string' ? parseInt(i.amount.replace(/[^0-9]/g,'')) : i.amount; return s+(a||0) }, 0)
    }
  },
  mounted() {
    const t = localStorage.getItem('theme'); this.isDark = t ? t==='dark' : false; this.applyTheme()
    // 支持 base64 编码参数和旧格式
    const raw = this.$route.query.d || this.$route.query.data
    if (raw) {
      try {
        let parsed
        if (this.$route.query.d) {
          parsed = JSON.parse(decodeURIComponent(escape(atob(raw))))
        } else {
          parsed = JSON.parse(raw)
        }
        this.itinerary = parsed
        this.$nextTick(() => { this.drawBudgetChart(); this.fetchWeatherData() })
      } catch(e) { console.error('解析行程数据失败:', e); this.$router.push('/') }
    } else { this.$router.push('/') }
  },
  methods: {
    toggleTheme() { this.isDark=!this.isDark; this.applyTheme(); localStorage.setItem('theme', this.isDark?'dark':'light') },
    applyTheme() { this.isDark ? document.documentElement.classList.add('dark-mode') : document.documentElement.classList.remove('dark-mode') },
    goHome() { this.$router.push('/') },
    async exportResult() {
      try {
        const el = document.querySelector('.result-content')
        if (!el) { console.error('element not found'); return }
        // 临时切换到浅色模式截图
        const wasDark = document.documentElement.classList.contains('dark-mode')
        if (wasDark) document.documentElement.classList.remove('dark-mode')
        await new Promise(r => setTimeout(r, 300))
        const canvas = await html2canvas(el, { scale: 2, useCORS: true, logging: false, backgroundColor: '#ffffff' })
        if (wasDark) document.documentElement.classList.add('dark-mode')
        const imgData = canvas.toDataURL('image/jpeg', 0.92)
        const pdf = new window.jspdf.jsPDF('p', 'mm', 'a4')
        const imgW = 190, pageH = 277
        const imgH = canvas.height * imgW / canvas.width
        let heightLeft = imgH, position = 10
        pdf.addImage(imgData, 'JPEG', 10, position, imgW, imgH)
        heightLeft -= pageH
        while (heightLeft > 0) {
          position = heightLeft - imgH
          pdf.addPage()
          pdf.addImage(imgData, 'JPEG', 10, position, imgW, imgH)
          heightLeft -= pageH
        }
        pdf.save(`旅行计划_${this.itinerary.overview?.destination || '行程'}.pdf`)
      } catch (e) {
        console.error('导出失败:', e)
        alert('导出PDF失败: ' + e.message)
      }
    },
    fetchWeatherData() {
      const dest = this.itinerary.overview?.destination; if (!dest) return
      axios.get(`/api/weather?city=${encodeURIComponent(dest)}`).then(r => {
        const w = r.data; this.weather = { temperature: parseInt(w.temp.replace('°C','')), condition: w.condition, detail: w.warning||'天气适宜出行。', icon: w.condition.includes('晴')?'sun':'cloud', iconClass: w.condition.includes('晴')?'sunny':'cloudy', alert: w.warning||'' }
      }).catch(() => { this.weather = { temperature:22, condition:'多云转晴', detail:'天气数据获取失败', icon:'sun', iconClass:'sunny', alert:'' } })
    },
    drawBudgetChart() {
      const canvas = this.$refs.budgetChart; if (!canvas) return
      const ctx = canvas.getContext('2d'); const dpr = window.devicePixelRatio||1; const rect = canvas.getBoundingClientRect()
      canvas.width = rect.width*dpr; canvas.height = rect.height*dpr; ctx.scale(dpr, dpr)
      const cats = this.itinerary.budget_breakdown||[]; if (!cats.length) return
      const colors = ['#10B981','#3B82F6','#8B5CF6','#F59E0B','#EF4444','#EC4899']
      const total = cats.reduce((s,c) => { const a = typeof c.amount==='string'?parseInt(c.amount.replace(/[^0-9]/g,'')):c.amount; return s+(a||0) }, 0)
      const cx = rect.width/2, cy = rect.height/2-10, r = Math.min(cx,cy)-20, ir = r*0.6
      let angle = -Math.PI/2
      cats.forEach((cat,i) => {
        const a = typeof cat.amount==='string'?parseInt(cat.amount.replace(/[^0-9]/g,'')):cat.amount
        const pct = (a||0)/total; const ang = pct*Math.PI*2
        ctx.beginPath(); ctx.arc(cx,cy,r,angle,angle+ang); ctx.arc(cx,cy,ir,angle+ang,angle,true); ctx.closePath(); ctx.fillStyle=colors[i%colors.length]; ctx.fill()
        angle += ang
      })
      ctx.fillStyle = getComputedStyle(document.documentElement).getPropertyValue('--text-primary').trim() || '#1e293b'
      ctx.font = 'bold 20px Inter, sans-serif'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle'
      ctx.fillText('¥'+total.toLocaleString(), cx, cy-5)
      ctx.fillStyle = getComputedStyle(document.documentElement).getPropertyValue('--text-secondary').trim() || '#64748b'
      ctx.font = '12px Inter, sans-serif'; ctx.fillText('总预算', cx, cy+15)
      let ly = rect.height-30; const lw = rect.width/Math.min(cats.length,3)
      cats.slice(0,3).forEach((cat,i) => {
        const x = lw*i+lw/2-30; ctx.fillStyle=colors[i%colors.length]; ctx.fillRect(x,ly,12,12)
        ctx.fillStyle = getComputedStyle(document.documentElement).getPropertyValue('--text-secondary').trim() || '#64748b'
        ctx.font = '11px Inter, sans-serif'; ctx.textAlign = 'left'; ctx.fillText(cat.category||'其他', x+18, ly+9)
      })
    }
  }
}
</script>

<style scoped>
:root{--bg-primary:#fff;--bg-secondary:#fff;--bg-nav:rgba(255,255,255,0.95);--bg-card:rgba(255,255,255,0.95);--text-primary:#1e293b;--text-secondary:#64748b;--border-color:rgba(226,232,240,0.8);--shadow-color:rgba(0,0,0,0.05);--primary-color:#10B981;--secondary-color:#3B82F6;}
html.dark-mode{--bg-primary:#020617;--bg-secondary:#0f172a;--bg-nav:rgba(15,23,42,0.95);--bg-card:rgba(30,41,59,0.98);--text-primary:#fff;--text-secondary:#e2e8f0;--border-color:rgba(255,255,255,0.15);--shadow-color:rgba(0,0,0,0.3);--primary-color:#60a5fa;--secondary-color:#a78bfa;}
.result-container{min-height:100vh;background:var(--bg-primary);padding-top:80px;}

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
.btn{display:flex;align-items:center;gap:0.5rem;padding:0.6rem 1.25rem;border-radius:9999px;font-size:0.9rem;font-weight:600;cursor:pointer;transition:all 0.3s;border:none;}
.btn svg{width:18px;height:18px;}
.btn-outline{background:transparent;border:1.5px solid var(--border-color);color:var(--text-primary);}
.btn-outline:hover{border-color:var(--primary-color);color:var(--primary-color);}
.theme-toggle{padding:0.6rem;min-width:auto;border-radius:50%;display:flex;align-items:center;justify-content:center;}
.theme-toggle svg{width:20px;height:20px;}
.btn-primary{background:linear-gradient(135deg,#10B981,#059669);color:white;box-shadow:0 4px 14px rgba(16,185,129,0.35);}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 6px 20px rgba(16,185,129,0.45);}

.result-content{max-width:1200px;margin:0 auto;padding:2rem;}
.glass-card{background:var(--bg-card);backdrop-filter:blur(16px);border:1px solid var(--border-color);box-shadow:0 8px 32px var(--shadow-color);}
.card-hover{transition:all 0.3s;}
.card-hover:hover{transform:translateY(-4px);box-shadow:0 12px 40px var(--shadow-color);}

.overview-card{display:flex;gap:2rem;padding:2rem;border-radius:2rem;margin-bottom:2rem;overflow:hidden;}
.overview-image{position:relative;width:300px;height:200px;border-radius:1.5rem;overflow:hidden;flex-shrink:0;display:flex;align-items:center;justify-content:center;}
.dest-emoji{font-size:4rem;filter:drop-shadow(0 4px 8px rgba(0,0,0,0.3));}
.image-overlay{position:absolute;bottom:0;left:0;right:0;padding:1rem;background:linear-gradient(to top,rgba(0,0,0,0.6),transparent);display:flex;justify-content:space-between;align-items:flex-end;}
.badge{background:linear-gradient(135deg,#10B981,#059669);color:white;padding:0.35rem 0.75rem;border-radius:9999px;font-size:0.7rem;font-weight:700;}
.date{color:rgba(255,255,255,0.9);font-size:0.8rem;}
.overview-info{flex:1;}
.overview-title{font-size:2rem;font-weight:700;color:var(--text-primary);margin-bottom:1.5rem;font-family:'Georgia',serif;}
.destination{background:linear-gradient(135deg,#10B981,#3B82F6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
html.dark-mode .destination{background:linear-gradient(135deg,#6ee7b7,#60a5fa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.overview-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;}
.stat-item{display:flex;align-items:center;gap:0.75rem;padding:1rem;border-radius:1rem;transition:all 0.3s;background:var(--bg-card);border:1px solid var(--border-color);}
.stat-item:hover{transform:translateY(-2px);box-shadow:0 8px 16px var(--shadow-color);}
.stat-icon{width:44px;height:44px;border-radius:12px;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.stat-icon svg{width:22px;height:22px;color:white;}
.bg-emerald-light{background:linear-gradient(135deg,#10B981,#34D399);}
.bg-amber-light{background:linear-gradient(135deg,#F59E0B,#FBBF24);}
.bg-blue-light{background:linear-gradient(135deg,#3B82F6,#60A5FA);}
.bg-purple-light{background:linear-gradient(135deg,#8B5CF6,#A78BFA);}
.stat-content{display:flex;flex-direction:column;}
.stat-label{font-size:0.75rem;color:var(--text-secondary);margin-bottom:0.25rem;}
.stat-value{font-size:1rem;font-weight:700;color:var(--text-primary);}

.main-grid{display:grid;grid-template-columns:1fr 380px;gap:2rem;}
.timeline-section{border-radius:2rem;padding:2rem;background:var(--bg-card);border:1px solid var(--border-color);}
.section-header{margin-bottom:1.5rem;}
.section-title{display:flex;align-items:center;gap:0.75rem;font-size:1.25rem;font-weight:700;color:var(--text-primary);}
.section-title svg{width:24px;height:24px;color:var(--primary-color);}
.timeline-day{display:flex;gap:1.5rem;margin-bottom:2rem;opacity:0;animation:fadeInUp 0.6s ease forwards;}
@keyframes fadeInUp{from{opacity:0;transform:translateY(20px);}to{opacity:1;transform:translateY(0);}}
.timeline-marker{display:flex;flex-direction:column;align-items:center;flex-shrink:0;}
.marker-dot{width:40px;height:40px;background:linear-gradient(135deg,#10B981,#059669);color:white;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.9rem;box-shadow:0 4px 12px rgba(16,185,129,0.3);}
.marker-line{width:2px;flex:1;background:linear-gradient(to bottom,#10B981,transparent);margin-top:0.5rem;min-height:40px;}
.day-header{display:flex;align-items:center;gap:1rem;margin-bottom:1rem;}
.day-title{font-size:1.1rem;font-weight:700;color:var(--text-primary);}
.day-theme{background:rgba(16,185,129,0.1);color:var(--primary-color);padding:0.35rem 0.75rem;border-radius:9999px;font-size:0.8rem;font-weight:600;}
html.dark-mode .day-theme{background:rgba(96,165,250,0.15);}
.activities{display:flex;flex-direction:column;gap:1rem;}
.activity-card{padding:1.25rem;border-radius:1rem;background:var(--bg-card);border:1px solid var(--border-color);transition:all 0.3s;}
.activity-card:hover{transform:translateX(4px);box-shadow:0 8px 24px var(--shadow-color);}
.activity-time{display:flex;align-items:center;gap:0.5rem;font-size:0.8rem;color:var(--primary-color);font-weight:600;margin-bottom:0.5rem;}
.activity-time svg{width:14px;height:14px;}
.activity-name{font-size:1rem;font-weight:700;color:var(--text-primary);margin-bottom:0.5rem;}
.activity-desc{font-size:0.9rem;color:var(--text-secondary);line-height:1.6;}
.activity-tags{display:flex;flex-wrap:wrap;gap:0.5rem;margin-top:0.75rem;}
.tag{background:rgba(16,185,129,0.1);color:var(--primary-color);padding:0.25rem 0.6rem;border-radius:9999px;font-size:0.75rem;}
html.dark-mode .tag{background:rgba(96,165,250,0.15);}

.sidebar{display:flex;flex-direction:column;gap:1.5rem;}
.sidebar-card{padding:1.5rem;border-radius:1.5rem;background:var(--bg-card);border:1px solid var(--border-color);}
.card-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:1.25rem;}
.card-header h3{display:flex;align-items:center;gap:0.5rem;font-size:1rem;font-weight:700;color:var(--text-primary);}
.card-header h3 svg{width:20px;height:20px;color:var(--primary-color);}
.city{font-size:0.75rem;color:var(--text-secondary);font-weight:600;text-transform:uppercase;letter-spacing:0.5px;}

.weather-main{display:flex;align-items:center;gap:1rem;margin-bottom:1rem;}
.weather-temp{font-size:3rem;font-weight:700;color:var(--text-primary);line-height:1;}
.weather-info{flex:1;}
.weather-condition{font-size:1rem;font-weight:600;color:var(--text-primary);margin-bottom:0.25rem;}
.weather-detail{font-size:0.8rem;color:var(--text-secondary);}
.weather-icon{width:60px;height:60px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#FCD34D,#F59E0B);}
.weather-icon svg{width:36px;height:36px;color:white;}
.weather-alert{display:flex;align-items:flex-start;gap:0.75rem;padding:1rem;background:rgba(245,158,11,0.1);border-radius:1rem;border:1px solid rgba(245,158,11,0.2);}
.weather-alert svg{width:20px;height:20px;color:#F59E0B;flex-shrink:0;}
.weather-alert p{font-size:0.85rem;color:#92400e;line-height:1.5;}

.budget-chart-container{display:flex;justify-content:center;margin-bottom:1rem;}
.budget-chart-container canvas{max-width:100%;}
.budget-summary{border-top:1px solid var(--border-color);padding-top:1rem;}
.budget-item{display:flex;justify-content:space-between;align-items:center;}
.budget-label{font-size:0.85rem;color:var(--text-secondary);}
.budget-value{font-size:1rem;font-weight:700;color:var(--text-primary);}

.packing-category{margin-bottom:1.25rem;}
.packing-category:last-child{margin-bottom:0;}
.category-title{font-size:0.85rem;font-weight:600;color:var(--text-secondary);margin-bottom:0.75rem;text-transform:uppercase;letter-spacing:0.5px;}
.category-items{display:flex;flex-direction:column;gap:0.5rem;}
.packing-item{display:flex;align-items:center;gap:0.75rem;padding:0.5rem;border-radius:0.5rem;cursor:pointer;transition:all 0.2s;}
.packing-item:hover{background:rgba(16,185,129,0.05);}
.custom-checkbox{width:20px;height:20px;border:2px solid var(--border-color);border-radius:6px;cursor:pointer;transition:all 0.2s;appearance:none;position:relative;}
.custom-checkbox:checked{background:var(--primary-color);border-color:var(--primary-color);}
.custom-checkbox:checked::after{content:'✓';position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);color:white;font-size:12px;font-weight:bold;}
.item-name{font-size:0.9rem;color:var(--text-primary);transition:all 0.2s;}
.item-name.checked{text-decoration:line-through;color:var(--text-secondary);}

.footer{background:var(--bg-secondary);padding:4rem 2rem 2rem;border-top:1px solid var(--border-color);margin-top:4rem;}
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

@media(max-width:1024px){.main-grid{grid-template-columns:1fr;}.overview-card{flex-direction:column;}.overview-image{width:100%;height:200px;}.overview-stats{grid-template-columns:repeat(2,1fr);}}
@media(max-width:768px){.nav-links{display:none;}.desktop-only{display:none;}.hamburger{display:flex;}.mobile-menu{display:flex;flex-direction:column;padding:1rem 1.5rem;background:var(--bg-nav);backdrop-filter:blur(20px);border-top:1px solid var(--border-color);}.mobile-link{padding:0.8rem 0;font-size:1rem;font-weight:500;color:var(--text-primary);text-decoration:none;border-bottom:1px solid var(--border-color);}.mobile-link:hover{color:var(--primary-color);}.menu-enter-active,.menu-leave-active{transition:all 0.3s ease;max-height:400px;overflow:hidden;}.menu-enter-from,.menu-leave-to{max-height:0;opacity:0;}.result-content{padding:1rem;}.overview-stats{grid-template-columns:1fr;}.footer-content{grid-template-columns:1fr;gap:2rem;}.footer-links{grid-template-columns:repeat(2,1fr);}}

.hamburger{display:none;flex-direction:column;gap:5px;padding:0.5rem;cursor:pointer;background:none;border:none;}
.hamburger span{display:block;width:22px;height:2px;background:var(--text-primary);border-radius:2px;transition:all 0.3s;}
.hamburger.active span:nth-child(1){transform:rotate(45deg) translate(5px,5px);}
.hamburger.active span:nth-child(2){opacity:0;}
.hamburger.active span:nth-child(3){transform:rotate(-45deg) translate(5px,-5px);}
.mobile-menu{display:none;}
</style>
