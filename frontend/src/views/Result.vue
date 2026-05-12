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
        <button class="btn btn-outline" @click="exportMarkdown">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M8 13h8"/><path d="M8 17h8"/><path d="M8 9h2"/></svg>
          导出 MD
        </button>
        <button class="btn btn-outline" @click="exportJson">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7a3 3 0 0 1 3-3h3"/><path d="M20 7a3 3 0 0 0-3-3h-3"/><path d="M4 17a3 3 0 0 0 3 3h3"/><path d="M20 17a3 3 0 0 1-3 3h-3"/><path d="M8 12h.01"/><path d="M12 12h.01"/><path d="M16 12h.01"/></svg>
          导出 JSON
        </button>
        <button class="btn btn-outline" @click="copyToClipboard(toWechatFormat())">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
          微信版
        </button>
        <button class="btn btn-outline" @click="copyToClipboard(toRednoteFormat())">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1"/></svg>
          小红书版
        </button>
        <span v-if="copySuccess" class="copy-toast">已复制 ✓</span>
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
            <span class="destination">{{ cleanDestination || '目的地' }}</span>
            <span class="days">{{ itinerary.overview?.days || 0 }}</span>日深度发现之旅
          </h1>
          <div class="overview-stats">
            <div class="stat-item glass-card"><div class="stat-icon bg-emerald-light"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg></div><div class="stat-content"><span class="stat-label">行程天数</span><span class="stat-value">{{ itinerary.overview?.days || 0 }} 天</span></div></div>
            <div class="stat-item glass-card"><div class="stat-icon bg-amber-light"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="5" width="20" height="14" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/></svg></div><div class="stat-content"><span class="stat-label">预算范围</span><span class="stat-value">¥{{ itinerary.overview?.budget || 0 }}</span></div></div>
            <div class="stat-item glass-card"><div class="stat-icon bg-blue-light"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg></div><div class="stat-content"><span class="stat-label">出发日期</span><span class="stat-value">{{ itinerary.overview?.travel_date || '待定' }}</span></div></div>
            <div class="stat-item glass-card"><div class="stat-icon bg-purple-light"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg></div><div class="stat-content"><span class="stat-label">出行人数</span><span class="stat-value">{{ itinerary.overview?.travelers || 1 }} 人</span></div></div>
            <div class="stat-item glass-card"><div class="stat-icon bg-blue-light"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg></div><div class="stat-content"><span class="stat-label">最佳季节</span><span class="stat-value">{{ itinerary.overview?.best_season || '四季皆宜' }}</span></div></div>
            <div class="stat-item glass-card"><div class="stat-icon bg-purple-light"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg></div><div class="stat-content"><span class="stat-label">行程节奏</span><span class="stat-value">{{ itinerary.overview?.pace || '适中' }}</span></div></div>
          </div>
        </div>
      </div>

      <!-- 路线地图 -->
      <div class="map-section glass-card">
        <div class="section-header">
          <h2 class="section-title"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"/><line x1="8" y1="2" x2="8" y2="18"/><line x1="16" y1="6" x2="16" y2="22"/></svg>路线地图</h2>
          <button class="btn btn-outline btn-sm" type="button" @click="toggleMap">{{ mapExpanded ? '收起地图' : '展开地图' }}</button>
        </div>
        <div v-show="mapExpanded" ref="mapContainer" class="map-container"></div>
      </div>

      <div class="main-grid">
        <div class="timeline-section glass-card">
          <div class="section-header"><h2 class="section-title"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>每日行程安排</h2><div class="timeline-toggle"><button :class="{ active: timelineView === 'gantt' }" class="toggle-btn" @click="timelineView = 'gantt'; $nextTick(() => drawGanttChart())">时间轴</button><button :class="{ active: timelineView === 'cards' }" class="toggle-btn" @click="timelineView = 'cards'">卡片</button></div></div>
          <div v-show="timelineView === 'gantt'" ref="ganttChart" class="gantt-container"></div>
          <div v-show="timelineView === 'cards'" class="timeline">
            <div v-for="(day, index) in itinerary.daily_plan" :key="index" class="timeline-day" :style="{ animationDelay: index * 0.1 + 's' }">
              <div class="timeline-marker"><div class="marker-dot">{{ day.day }}</div><div class="marker-line" v-if="index < (itinerary.daily_plan?.length || 0) - 1"></div></div>
              <div class="timeline-content">
                <div class="day-header"><h3 class="day-title">第 {{ day.day }} 天</h3><span class="day-theme">{{ day.title }}</span></div>
                <div class="activities">
                  <div v-for="(activity, actIndex) in day.activities" :key="actIndex" class="activity-card glass-card card-hover">
                    <div class="activity-time"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>{{ activity.time }}</div>
                    <h4 class="activity-name">{{ activity.name || activity.title }}</h4>
                    <p class="activity-desc">{{ activity.description }}</p>
                    <div class="activity-meta" v-if="activity.transport || activity.duration || (activity.food && activity.food.length) || (activity.alternatives && activity.alternatives.length) || activity.booking_tip">
                      <div class="meta-row" v-if="activity.transport || activity.duration">
                        <span class="meta-pill" v-if="activity.transport">交通：{{ activity.transport }}</span>
                        <span class="meta-pill" v-if="activity.duration">耗时：{{ activity.duration }}</span>
                      </div>
                      <div class="meta-row" v-if="activity.food && activity.food.length">
                        <span class="meta-label">用餐推荐</span>
                        <span class="meta-text">{{ activity.food.slice(0, 3).join(' / ') }}</span>
                      </div>
                      <div class="meta-row" v-if="activity.booking_tip">
                        <span class="meta-label">预约提示</span>
                        <span class="meta-text">{{ activity.booking_tip }}</span>
                      </div>
                      <div class="meta-row" v-if="activity.alternatives && activity.alternatives.length">
                        <span class="meta-label">备选方案</span>
                        <span class="meta-text">{{ activity.alternatives.slice(0, 2).join('；') }}</span>
                      </div>
                    </div>
                    <div class="activity-tags" v-if="activity.tags"><span v-for="(tag, ti) in activity.tags" :key="ti" class="tag">{{ tag }}</span></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="sidebar">
            <div class="sidebar-card glass-card">
            <div class="card-header"><h3><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/></svg>实时天气</h3><span class="city">{{ cleanDestination }}</span></div>
            <div class="weather-main"><div class="weather-temp">{{ weather.temperature }}°</div><div class="weather-info"><p class="weather-condition">{{ weather.condition }}</p><p class="weather-detail">{{ weather.detail }}</p></div><div class="weather-icon" :class="weather.iconClass"><svg viewBox="0 0 24 24" fill="currentColor"><path v-if="weather.icon === 'sun'" d="M12 7c-2.76 0-5 2.24-5 5s2.24 5 5 5 5-2.24 5-5-2.24-5-5-5zM2 13h2c.55 0 1-.45 1-1s-.45-1-1-1H2c-.55 0-1 .45-1 1s.45 1 1 1zm18 0h2c.55 0 1-.45 1-1s-.45-1-1-1h-2c-.55 0-1 .45-1 1s.45 1 1 1zM11 2v2c0 .55.45 1 1 1s1-.45 1-1V2c0-.55-.45-1-1-1s-1 .45-1 1zm0 18v2c0 .55.45 1 1 1s1-.45 1-1v-2c0-.55-.45-1-1-1s-1 .45-1 1z"/><path v-else d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96z"/></svg></div></div>
            <div class="weather-alert" v-if="weather.alert"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg><p>{{ weather.alert }}</p></div>
            <div class="weather-advice" v-if="weather.advice && weather.advice.length">
              <div class="advice-title">出行建议</div>
              <div v-for="(a, ai) in weather.advice" :key="ai" class="advice-item">
                <span class="advice-icon">{{ a.icon }}</span>
                <span class="advice-text">{{ a.text }}</span>
              </div>
            </div>
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

          <!-- 调整行程 Chat -->
          <div class="sidebar-card glass-card chat-panel">
            <div class="card-header"><h3><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>调整行程</h3></div>
            <div class="chat-messages" ref="chatMsgs">
              <div v-if="!chatHistory.length" class="chat-hint">直接描述你想调整的内容，AI 会重新生成行程。例如：</div>
              <div v-for="(msg, mi) in chatHistory" :key="mi" class="chat-msg" :class="msg.role">
                <span class="chat-role">{{ msg.role === 'user' ? '你' : 'AI' }}</span>
                <p class="chat-text">{{ msg.content }}</p>
              </div>
            </div>
            <div class="chat-input-row">
              <input v-model="chatInput" placeholder="把第二天换成海边..." @keydown.enter="sendChat" :disabled="chatLoading" class="chat-input" />
              <button @click="sendChat" :disabled="chatLoading || !chatInput.trim()" class="btn btn-primary btn-sm">{{ chatLoading ? '...' : '发送' }}</button>
            </div>
            <p class="chat-example">试试：「把第二天换成美食之旅」「增加一天自由活动」</p>
          </div>
        </div>
      </div>
    </div>

    <footer class="footer">
      <div class="footer-content">
        <div class="footer-brand">
          <div class="brand-header"><div class="brand-icon"><svg class="icon-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 00-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z" fill="currentColor"/></svg></div><router-link to="/" class="brand-text-link"><span class="brand-text">Voyage<span class="brand-highlight">AI</span></span></router-link></div>
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
import axios from 'axios'
import * as echarts from 'echarts'

export default {
  name: 'Result',
  data() {
    return {
      isDark: false,
      menuOpen: false,
      timelineView: 'cards',
      copySuccess: false,
      mapExpanded: false,
      amapLoaded: false,
      chatHistory: [],
      chatInput: '',
      chatLoading: false,
      itinerary: {},
      weather: { temperature: 22, condition: '多云转晴', detail: '加载中...', icon: 'sun', iconClass: 'sunny', alert: '', advice: [] },
      packingList: [
        { name: '🪪 证件与财务', items: [{ name: '身份证/护照', checked: false }, { name: '驾驶证', checked: false }, { name: '现金与银行卡', checked: false }] },
        { name: '📱 电子设备', items: [{ name: '手机与充电器', checked: false }, { name: '相机与存储卡', checked: false }, { name: '充电宝', checked: false }] },
        { name: '🧳 个人用品', items: [{ name: '洗漱用品', checked: false }, { name: '防晒霜', checked: false }, { name: '常用药品', checked: false }] }
      ]
    }
  },
  computed: {
    currentDate() { const d = new Date(); return `${d.getFullYear()}.${String(d.getMonth()+1).padStart(2,'0')}.${String(d.getDate()).padStart(2,'0')}` },
    cleanDestination() {
      const raw = (this.itinerary?.overview?.destination || '').trim()
      if (!raw) return ''
      // Remove common prompt tails accidentally ending up in destination
      // e.g. "北京玩5天" / "东京自由行" / "北京5日"
      return raw
        .replace(/(?:玩|游玩|游|旅行|自由行|之旅)\s*\d+\s*(?:天|日).*/u, '')
        .replace(/\d+\s*(?:天|日).*/u, '')
        .replace(/(?:玩|游玩|游|旅行|自由行|之旅).*/u, '')
        .trim()
    },
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
      const dest = this.cleanDestination || ''
      return gradients[dest] || 'linear-gradient(135deg, #10B981, #3B82F6, #8B5CF6)'
    },
    destEmoji() {
      const emojis = { '北京':'🏛️','上海':'🌆','杭州':'🌿','成都':'🐼','西安':'⚔️','南京':'🏯','广州':'🌺','深圳':'💎','重庆':'🌶️','厦门':'🌊','丽江':'🏘️','大理':'🏔️','张家界':'⛰️','三亚':'🏖️','青岛':'🍺','苏州':'🎐','厦门':'🌊','哈尔滨':'❄️' }
      return emojis[this.cleanDestination] || '✈️'
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
    downloadBlob(blob, filename) {
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = filename
      document.body.appendChild(a)
      a.click()
      a.remove()
      URL.revokeObjectURL(url)
    },
    itineraryToMarkdown() {
      const o = this.itinerary?.overview || {}
      const dest = this.cleanDestination || o.destination || '目的地'
      const days = o.days ?? ''
      const budget = o.budget ?? ''
      const best = o.best_season || ''
      const pace = o.pace || ''
      const lines = []
      lines.push(`# ${dest}${days ? ` ${days} 日` : ''}行程`)
      lines.push('')
      lines.push(`- 生成日期：${this.currentDate}`)
      if (days !== '') lines.push(`- 天数：${days}`)
      if (o.travel_date) lines.push(`- 出发日期：${o.travel_date}`)
      if (o.travelers) lines.push(`- 出行人数：${o.travelers} 人`)
      if (budget !== '') lines.push(`- 预算：¥${budget}`)
      if (best) lines.push(`- 最佳季节：${best}`)
      if (pace) lines.push(`- 行程节奏：${pace}`)
      lines.push('')

      const daily = Array.isArray(this.itinerary?.daily_plan) ? this.itinerary.daily_plan : []
      if (daily.length) {
        lines.push('## 每日行程')
        lines.push('')
        daily.forEach((d) => {
          lines.push(`### 第 ${d.day ?? ''} 天：${d.title || ''}`.trim())
          const acts = Array.isArray(d.activities) ? d.activities : []
          acts.forEach((a) => {
            const time = a.time ? `**${a.time}** ` : ''
            const name = a.name || a.title || ''
            const desc = a.description ? ` — ${a.description}` : ''
            lines.push(`- ${time}${name}${desc}`.trim())
          })
          lines.push('')
        })
      }

      const budgetList = Array.isArray(this.itinerary?.budget_breakdown) ? this.itinerary.budget_breakdown : []
      if (budgetList.length) {
        lines.push('## 预算拆分')
        lines.push('')
        budgetList.forEach((b) => {
          const cat = b.category || '其他'
          const amt = b.amount ?? ''
          lines.push(`- ${cat}：${typeof amt === 'number' ? `¥${amt}` : String(amt)}`)
        })
        lines.push('')
      }

      const tips = this.itinerary?.tips
      if (tips && typeof tips === 'string') {
        lines.push('## 小贴士')
        lines.push('')
        lines.push(tips)
        lines.push('')
      }

      return lines.join('\n').trim() + '\n'
    },
    exportMarkdown() {
      const md = this.itineraryToMarkdown()
      const name = `旅行计划_${this.cleanDestination || '行程'}_${this.currentDate}.md`
      this.downloadBlob(new Blob([md], { type: 'text/markdown;charset=utf-8' }), name)
    },
    exportJson() {
      const name = `旅行计划_${this.cleanDestination || '行程'}_${this.currentDate}.json`
      const content = JSON.stringify(this.itinerary || {}, null, 2) + '\n'
      this.downloadBlob(new Blob([content], { type: 'application/json;charset=utf-8' }), name)
    },
    fetchWeatherData() {
      const dest = this.cleanDestination; if (!dest) return
      axios.get(`/api/weather?city=${encodeURIComponent(dest)}`).then(r => {
        const w = r.data; this.weather = { temperature: parseInt(w.temp.replace('°C','')), condition: w.condition, detail: w.warning||'天气适宜出行。', icon: w.condition.includes('晴')?'sun':'cloud', iconClass: w.condition.includes('晴')?'sunny':'cloudy', alert: w.warning||'', advice: w.advice||[] }
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
    },
    drawGanttChart() {
      const dom = this.$refs.ganttChart; if (!dom) return
      if (this._ganttChart) this._ganttChart.dispose()
      const chart = echarts.init(dom)
      const dp = this.itinerary.daily_plan || []
      if (!dp.length) return
      const colors = ['#10B981','#3B82F6','#8B5CF6','#F59E0B','#EC4899','#14B8A6']
      const yData = dp.map(d => 'Day ' + d.day).reverse()
      const dayCount = dp.length
      const series = []

      dp.forEach((day, dayIdx) => {
        const activities = (day.activities || []).slice().sort((a, b) => {
          return this.parseTimeSegment(a.time, 0)[0] - this.parseTimeSegment(b.time, 0)[0]
        })
        let cursor = 6
        activities.forEach((act, actIdx) => {
          const seg = this.parseTimeSegment(act.time, actIdx)
          const startH = seg[0]; const endH = Math.min(seg[1], 22)
          // transparent spacer before activity
          if (startH > cursor) {
            series.push({
              type: 'bar', stack: 'day' + dayIdx, name: '',
              data: yData.map((_, yi) => yi === dayCount - 1 - dayIdx ? startH - cursor : null),
              itemStyle: { color: 'transparent' }, barWidth: 18,
              tooltip: { show: false }, silent: true
            })
          }
          const dur = Math.max(endH - startH, 0.5)
          series.push({
            type: 'bar', stack: 'day' + dayIdx,
            name: (act.title || act.name || '').substring(0, 10),
            data: yData.map((_, yi) => yi === dayCount - 1 - dayIdx ? dur : null),
            itemStyle: { color: colors[actIdx % colors.length], borderRadius: 4 },
            barWidth: 18, emphasis: { itemStyle: { shadowBlur: 8 } }
          })
          cursor = endH
        })
      })

      chart.setOption({
        tooltip: {
          trigger: 'item',
          formatter: p => {
            if (p.seriesName) return p.seriesName
            return ''
          }
        },
        legend: { show: false },
        grid: { left: 65, right: 20, top: 15, bottom: 20 },
        xAxis: {
          type: 'value', min: 6, max: 22, interval: 2,
          axisLabel: { formatter: '{value}:00', fontSize: 11 },
          splitLine: { lineStyle: { color: 'rgba(148,163,184,0.1)' } }
        },
        yAxis: { type: 'category', data: yData, axisLabel: { fontSize: 12, fontWeight: 600 } },
        series
      })

      window.addEventListener('resize', () => chart.resize())
      this._ganttChart = chart
    },
    parseTimeSegment(timeStr, actIdx) {
      const t = (timeStr || '').trim()
      const m = t.match(/(\d{1,2}):?(\d{2})?\s*[-~至到]\s*(\d{1,2}):?(\d{2})?/)
      if (m) {
        const sh = parseInt(m[1]) + (parseInt(m[2] || '0') / 60)
        const eh = parseInt(m[3]) + (parseInt(m[4] || '0') / 60)
        return [Math.max(6, sh), Math.min(22, eh)]
      }
      // Fallback: assign by index
      const slots = [[8, 10.5], [10.5, 12], [13, 15], [15, 17], [17, 19], [19, 21]]
      return slots[actIdx % slots.length] || [8, 10]
    },
    toWechatFormat() {
      const o = this.itinerary.overview || {}
      const dest = this.cleanDestination
      const dp = this.itinerary.daily_plan || []
      const lines = []
      lines.push('✈️ ' + dest + (o.days || '') + '日游攻略来啦！')
      lines.push('')
      lines.push('📅 行程天数：' + (o.days || '') + '天')
      if (o.travel_date) lines.push('🗓️ 出发日期：' + o.travel_date)
      if (o.travelers) lines.push('👥 出行人数：' + o.travelers + '人')
      lines.push('💰 预算参考：¥' + (o.budget || ''))
      lines.push('🌸 最佳季节：' + (o.best_season || ''))
      lines.push('🏃 游玩节奏：' + (o.pace || ''))
      lines.push('')
      lines.push('📍 每日安排：')
      const emojis = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣']
      dp.forEach(day => {
        const emoji = emojis[(day.day || 1) - 1] || '📍'
        lines.push(emoji + ' Day' + day.day + '：' + day.title)
        ;(day.activities || []).slice(0, 2).forEach(a => {
          lines.push('  ' + (a.time || '') + ' ' + (a.title || a.name || ''))
        })
      })
      lines.push('')
      lines.push('💡 出行清单：')
      ;(this.itinerary.packing_list || []).slice(0, 5).forEach(item => { lines.push('✅ ' + item) })
      lines.push('')
      lines.push('#旅行攻略 #自由行 #' + dest + '旅行')
      return lines.join('\n')
    },
    toRednoteFormat() {
      const o = this.itinerary.overview || {}
      const dest = this.cleanDestination
      const dp = this.itinerary.daily_plan || []
      const lines = []
      lines.push('✨ ' + dest + '｜' + (o.days || '') + '天深度游保姆级攻略')
      lines.push('')
      lines.push('——  基本信息 ——')
      lines.push('📆 天数：' + (o.days || '') + '天')
      if (o.travel_date) lines.push('🗓️ 出发日期：' + o.travel_date)
      if (o.travelers) lines.push('👥 出行人数：' + o.travelers + '人')
      lines.push('💰 预算：¥' + (o.budget || ''))
      lines.push('🌸 最佳季节：' + (o.best_season || ''))
      lines.push('🏃 节奏：' + (o.pace || ''))
      lines.push('')
      lines.push('——  每日行程 ——')
      dp.forEach(day => {
        lines.push('Day' + day.day + ' ✦ ' + day.title)
        ;(day.activities || []).forEach(a => {
          lines.push('  ▸ ' + (a.time || '') + ' ' + (a.title || a.name || ''))
        })
        lines.push('')
      })
      lines.push('——  出行清单 ——')
      ;(this.itinerary.packing_list || []).forEach(item => { lines.push('☐ ' + item) })
      lines.push('')
      lines.push('#旅行 #攻略 #' + dest + ' #自由行')
      return lines.join('\n')
    },
    async copyToClipboard(text) {
      try {
        await navigator.clipboard.writeText(text)
        this.copySuccess = true
        setTimeout(() => { this.copySuccess = false }, 2000)
      } catch {
        const ta = document.createElement('textarea')
        ta.value = text; document.body.appendChild(ta); ta.select()
        document.execCommand('copy'); document.body.removeChild(ta)
        this.copySuccess = true
        setTimeout(() => { this.copySuccess = false }, 2000)
      }
    },
    async toggleMap() {
      this.mapExpanded = !this.mapExpanded
      if (this.mapExpanded && !this.amapLoaded) {
        await this.$nextTick()
        await this.initMap()
      }
    },
    async loadAMap() {
      if (window.AMap) return window.AMap
      const { data } = await axios.get('/api/amap-config')
      return new Promise((resolve, reject) => {
        const script = document.createElement('script')
        script.src = 'https://webapi.amap.com/maps?v=' + data.version + '&key=' + data.key
        script.onload = () => resolve(window.AMap)
        script.onerror = reject
        document.head.appendChild(script)
      })
    },
    async initMap() {
      try {
        await this.loadAMap()
        this.amapLoaded = true
        const AMap = window.AMap
        const map = new AMap.Map(this.$refs.mapContainer, {
          zoom: 12,
          center: [116.397428, 39.90923],
          mapStyle: this.isDark ? 'amap://styles/dark' : 'amap://styles/light'
        })
        // Geocode destination to center the map
        const geocoder = new AMap.Geocoder()
        const dest = this.cleanDestination
        const dp = this.itinerary.daily_plan || []
        const colors = ['#10B981','#3B82F6','#8B5CF6','#F59E0B','#EC4899','#14B8A6','#EF4444']
        let markerIdx = 0

        geocoder.getLocation(dest, (status, result) => {
          if (status === 'complete' && result.geocodes.length) {
            map.setCenter(result.geocodes[0].location)
          }
        })

        // Place markers for each activity
        dp.forEach((day, dayIdx) => {
          ;(day.activities || []).forEach(act => {
            const title = act.title || act.name
            if (!title) return
            geocoder.getLocation(dest + title, (status, result) => {
              if (status === 'complete' && result.geocodes.length) {
                const pos = result.geocodes[0].location
                const marker = new AMap.Marker({
                  position: [pos.lng, pos.lat],
                  title: 'D' + day.day + ': ' + title,
                  label: {
                    content: '<span style="background:' + colors[dayIdx % colors.length] + ';color:#fff;padding:2px 6px;border-radius:4px;font-size:11px">D' + day.day + '</span>',
                    offset: new AMap.Pixel(0, -24)
                  }
                })
                marker.setMap(map)
                markerIdx++
              }
            })
          })
        })

        this._mapInstance = map
      } catch (e) {
        console.error('地图加载失败:', e)
      }
    },
    async sendChat() {
      const msg = this.chatInput.trim()
      if (!msg || this.chatLoading) return
      this.chatHistory.push({ role: 'user', content: msg })
      this.chatInput = ''
      this.chatLoading = true
      try {
        const res = await axios.post('/api/chat', {
          previous_itinerary: this.itinerary,
          message: msg
        })
        this.itinerary = res.data
        this.chatHistory.push({ role: 'assistant', content: '已根据你的要求更新行程！' })
        this.$nextTick(() => {
          this.drawBudgetChart()
          this.drawGanttChart()
        })
      } catch (e) {
        this.chatHistory.push({ role: 'assistant', content: '修改失败，请稍后重试' })
      } finally {
        this.chatLoading = false
        this.$nextTick(() => {
          const el = this.$refs.chatMsgs
          if (el) el.scrollTop = el.scrollHeight
        })
      }
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

/* Map */
.map-section{margin-top:1.5rem;border-radius:2rem;padding:2rem;background:var(--bg-card);border:1px solid var(--border-color);}
.map-container{width:100%;height:380px;border-radius:1rem;overflow:hidden;margin-top:1rem;}
.btn-sm{padding:0.35rem 0.85rem;font-size:0.8rem;}

/* Chat */
.chat-panel{margin-top:0;}
.chat-messages{max-height:240px;overflow-y:auto;margin-bottom:0.75rem;display:flex;flex-direction:column;gap:0.6rem;}
.chat-hint{font-size:0.78rem;color:var(--text-secondary);text-align:center;padding:0.5rem;}
.chat-msg{padding:0.5rem 0.75rem;border-radius:0.75rem;font-size:0.82rem;line-height:1.5;}
.chat-msg.user{background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.2);align-self:flex-end;}
.chat-msg.assistant{background:rgba(59,130,246,0.08);border:1px solid rgba(59,130,246,0.15);}
.chat-role{font-size:0.7rem;font-weight:600;color:var(--text-secondary);display:block;margin-bottom:0.15rem;}
.chat-text{margin:0;color:var(--text-primary);}
.chat-input-row{display:flex;gap:0.5rem;}
.chat-input{flex:1;padding:0.5rem 0.75rem;border-radius:0.75rem;border:1px solid var(--border-color);background:var(--bg-primary);color:var(--text-primary);font-size:0.82rem;outline:none;}
.chat-input:focus{border-color:var(--primary-color);}
.chat-example{font-size:0.7rem;color:var(--text-secondary);margin-top:0.5rem;text-align:center;}

.main-grid{display:grid;grid-template-columns:1fr 380px;gap:2rem;}
.timeline-section{border-radius:2rem;padding:2rem;background:var(--bg-card);border:1px solid var(--border-color);}
.section-header{margin-bottom:1.5rem;}
.section-title{display:flex;align-items:center;gap:0.75rem;font-size:1.25rem;font-weight:700;color:var(--text-primary);}
.section-title svg{width:24px;height:24px;color:var(--primary-color);}
.section-header{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:0.75rem;}
.timeline-toggle{display:flex;gap:0.25rem;background:var(--border-color);border-radius:9999px;padding:3px;}
.toggle-btn{padding:0.35rem 0.9rem;border-radius:9999px;border:none;background:transparent;color:var(--text-secondary);font-size:0.8rem;cursor:pointer;transition:all 0.2s;font-weight:500;}
.toggle-btn.active{background:var(--primary-color);color:#fff;box-shadow:0 2px 8px rgba(16,185,129,0.25);}
.gantt-container{width:100%;height:280px;margin-top:0.5rem;}
.copy-toast{font-size:0.8rem;color:#10B981;font-weight:600;animation:fadeInUp 0.3s ease;}
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
.activity-meta{margin-top:0.75rem;display:flex;flex-direction:column;gap:0.45rem;}
.meta-row{display:flex;flex-wrap:wrap;gap:0.5rem;align-items:baseline;}
.meta-pill{background:rgba(16,185,129,0.10);color:var(--primary-color);border:1px solid rgba(16,185,129,0.22);padding:0.18rem 0.55rem;border-radius:9999px;font-size:0.75rem;font-weight:700;}
html.dark-mode .meta-pill{background:rgba(96,165,250,0.15);border-color:rgba(96,165,250,0.22);}
.meta-label{font-size:0.75rem;font-weight:800;color:var(--text-primary);opacity:0.92;}
.meta-text{font-size:0.82rem;color:var(--text-secondary);line-height:1.5;}
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

.weather-advice{margin-top:1rem;padding-top:1rem;border-top:1px solid var(--border-color);}
.advice-title{font-size:0.75rem;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-secondary);margin-bottom:0.6rem;}
.advice-item{display:flex;align-items:flex-start;gap:0.5rem;padding:0.35rem 0;font-size:0.82rem;color:var(--text-primary);}
.advice-icon{flex-shrink:0;font-size:1rem;}

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
