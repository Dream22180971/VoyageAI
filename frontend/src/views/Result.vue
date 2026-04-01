<template>
  <div class="result-container">
    <!-- 导航栏 -->
    <nav class="nav-bar">
      <div class="nav-brand" @click="goHome">
        <div class="brand-icon">
          <svg class="icon-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 00-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z" fill="currentColor"/>
          </svg>
        </div>
        <span class="brand-text">Voyage<span class="brand-highlight">AI</span></span>
      </div>
      
      <div class="nav-links">
        <router-link to="/inspiration" class="nav-link">发现灵感</router-link>
        <router-link to="/guide" class="nav-link">目的地指南</router-link>
        <router-link to="/community" class="nav-link">社区足迹</router-link>
        <router-link to="/about" class="nav-link">关于我们</router-link>
      </div>
      
      <div class="nav-actions">
        <button class="btn btn-outline" @click="goHome">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M19 12H5M12 19l-7-7 7-7"/>
          </svg>
          返回首页
        </button>
        <button class="btn btn-primary" @click="exportResult">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M7 10l5 5 5-5M12 15V3"/>
          </svg>
          导出指南
        </button>
      </div>
    </nav>

    <div class="result-content">
      <!-- 头部概览卡片 -->
      <div class="overview-card glass-card">
        <div class="overview-image">
          <img :src="destinationImage" :alt="itinerary.overview?.destination">
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
            <div class="stat-item">
              <div class="stat-icon bg-emerald-light">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="3" y="4" width="18" height="18" rx="2"/>
                  <line x1="16" y1="2" x2="16" y2="6"/>
                  <line x1="8" y1="2" x2="8" y2="6"/>
                  <line x1="3" y1="10" x2="21" y2="10"/>
                </svg>
              </div>
              <div class="stat-content">
                <span class="stat-label">行程天数</span>
                <span class="stat-value">{{ itinerary.overview?.days || 0 }} 天</span>
              </div>
            </div>
            
            <div class="stat-item">
              <div class="stat-icon bg-amber-light">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="2" y="5" width="20" height="14" rx="2"/>
                  <line x1="2" y1="10" x2="22" y2="10"/>
                </svg>
              </div>
              <div class="stat-content">
                <span class="stat-label">预算范围</span>
                <span class="stat-value">¥{{ itinerary.overview?.budget || 0 }}</span>
              </div>
            </div>
            
            <div class="stat-item">
              <div class="stat-icon bg-blue-light">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="12" cy="12" r="10"/>
                  <path d="M12 6v6l4 2"/>
                </svg>
              </div>
              <div class="stat-content">
                <span class="stat-label">最佳季节</span>
                <span class="stat-value">{{ itinerary.overview?.best_season || '四季皆宜' }}</span>
              </div>
            </div>
            
            <div class="stat-item">
              <div class="stat-icon bg-purple-light">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
                </svg>
              </div>
              <div class="stat-content">
                <span class="stat-label">行程节奏</span>
                <span class="stat-value">{{ itinerary.overview?.pace || '适中' }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="main-grid">
        <!-- 左侧：时间轴行程 -->
        <div class="timeline-section">
          <div class="section-header">
            <h2 class="section-title">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"/>
                <polyline points="12 6 12 12 16 14"/>
              </svg>
              每日行程安排
            </h2>
          </div>
          
          <div class="timeline">
            <div 
              v-for="(day, index) in itinerary.daily_plan" 
              :key="index"
              class="timeline-day"
              :style="{ animationDelay: index * 0.1 + 's' }"
            >
              <div class="timeline-marker">
                <div class="marker-dot">{{ day.day }}</div>
                <div class="marker-line" v-if="index < (itinerary.daily_plan?.length || 0) - 1"></div>
              </div>
              
              <div class="timeline-content">
                <div class="day-header">
                  <h3 class="day-title">第 {{ day.day }} 天</h3>
                  <span class="day-theme">{{ day.title }}</span>
                </div>
                
                <div class="activities">
                  <div 
                    v-for="(activity, actIndex) in day.activities" 
                    :key="actIndex"
                    class="activity-card glass-card card-hover"
                  >
                    <div class="activity-time">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="12" cy="12" r="10"/>
                        <polyline points="12 6 12 12 16 14"/>
                      </svg>
                      {{ activity.time }}
                    </div>
                    <h4 class="activity-name">{{ activity.name }}</h4>
                    <p class="activity-desc">{{ activity.description }}</p>
                    <div class="activity-tags" v-if="activity.tags">
                      <span v-for="(tag, tagIndex) in activity.tags" :key="tagIndex" class="tag">
                        {{ tag }}
                      </span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 右侧：边栏工具 -->
        <div class="sidebar">
          <!-- 实时天气 -->
          <div class="sidebar-card glass-card">
            <div class="card-header">
              <h3>
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="12" cy="12" r="5"/>
                  <line x1="12" y1="1" x2="12" y2="3"/>
                  <line x1="12" y1="21" x2="12" y2="23"/>
                  <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/>
                  <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/>
                  <line x1="1" y1="12" x2="3" y2="12"/>
                  <line x1="21" y1="12" x2="23" y2="12"/>
                  <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/>
                  <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>
                </svg>
                实时天气
              </h3>
              <span class="city">{{ itinerary.overview?.destination }}</span>
            </div>
            
            <div class="weather-main">
              <div class="weather-temp">{{ weather.temperature }}°</div>
              <div class="weather-info">
                <p class="weather-condition">{{ weather.condition }}</p>
                <p class="weather-detail">{{ weather.detail }}</p>
              </div>
              <div class="weather-icon" :class="weather.iconClass">
                <svg viewBox="0 0 24 24" fill="currentColor">
                  <path v-if="weather.icon === 'sun'" d="M12 7c-2.76 0-5 2.24-5 5s2.24 5 5 5 5-2.24 5-5-2.24-5-5-5zM2 13h2c.55 0 1-.45 1-1s-.45-1-1-1H2c-.55 0-1 .45-1 1s.45 1 1 1zm18 0h2c.55 0 1-.45 1-1s-.45-1-1-1h-2c-.55 0-1 .45-1 1s.45 1 1 1zM11 2v2c0 .55.45 1 1 1s1-.45 1-1V2c0-.55-.45-1-1-1s-1 .45-1 1zm0 18v2c0 .55.45 1 1 1s1-.45 1-1v-2c0-.55-.45-1-1-1s-1 .45-1 1zM5.99 4.58a.996.996 0 00-1.41 0 .996.996 0 000 1.41l1.06 1.06c.39.39 1.03.39 1.41 0s.39-1.03 0-1.41L5.99 4.58zm12.37 12.37a.996.996 0 00-1.41 0 .996.996 0 000 1.41l1.06 1.06c.39.39 1.03.39 1.41 0 .39-.39.39-1.03 0-1.41l-1.06-1.06zm1.06-10.96a.996.996 0 000-1.41.996.996 0 00-1.41 0l-1.06 1.06c-.39.39-.39 1.03 0 1.41s1.03.39 1.41 0l1.06-1.06zM7.05 18.36a.996.996 0 000 1.41.996.996 0 001.41 0l1.06-1.06c.39-.39.39-1.03 0-1.41s-1.03-.39-1.41 0l-1.06 1.06z"/>
                  <path v-else-if="weather.icon === 'cloud'" d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96z"/>
                  <path v-else d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96z"/>
                </svg>
              </div>
            </div>
            
            <div class="weather-alert" v-if="weather.alert">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/>
                <line x1="12" y1="9" x2="12" y2="13"/>
                <line x1="12" y1="17" x2="12.01" y2="17"/>
              </svg>
              <p>{{ weather.alert }}</p>
            </div>
          </div>

          <!-- 智能预算分析 -->
          <div class="sidebar-card glass-card">
            <div class="card-header">
              <h3>
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M21.21 15.89A10 10 0 118 2.83M22 12A10 10 0 0012 2v10z"/>
                </svg>
                智能预算分析
              </h3>
            </div>
            
            <div class="budget-chart-container">
              <canvas ref="budgetChart" width="280" height="200"></canvas>
            </div>
            
            <div class="budget-summary">
              <div class="budget-item">
                <span class="budget-label">预估总费用</span>
                <span class="budget-value">¥{{ totalBudget }}</span>
              </div>
              <div class="budget-item highlight">
                <span class="budget-label">AI 优化建议</span>
                <span class="budget-savings">-¥420 (租车折扣)</span>
              </div>
            </div>
          </div>

          <!-- 智能行前清单 -->
          <div class="sidebar-card glass-card">
            <div class="card-header">
              <h3>
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M9 11l3 3L22 4"/>
                  <path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/>
                </svg>
                智能行前清单
              </h3>
            </div>
            
            <div class="packing-list">
              <div 
                v-for="(category, catIndex) in packingList" 
                :key="catIndex"
                class="packing-category"
              >
                <h4 class="category-title">{{ category.name }}</h4>
                <div class="category-items">
                  <label 
                    v-for="(item, itemIndex) in category.items" 
                    :key="itemIndex"
                    class="packing-item"
                  >
                    <input type="checkbox" v-model="item.checked" class="custom-checkbox">
                    <span class="item-name" :class="{ checked: item.checked }">{{ item.name }}</span>
                  </label>
                </div>
              </div>
            </div>
          </div>

          <!-- Pro 特权广告 -->
          <div class="pro-card">
            <div class="pro-bg">
              <svg viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2L14.09 8.26L21 9.27L16 14.14L17.18 21.02L12 17.77L6.82 21.02L8 14.14L3 9.27L9.91 8.26L12 2Z"/>
              </svg>
            </div>
            <span class="pro-badge">Pro 特权</span>
            <h4>开启 2026 全球漫游包</h4>
            <p>获取 AI 实时机票降价预警及管家式预订服务</p>
            <button class="pro-btn">立即升级</button>
          </div>
        </div>
      </div>
    </div>

    <!-- 底部导航栏 -->
    <footer class="footer">
      <div class="footer-content">
        <div class="footer-brand">
          <div class="brand-header">
            <div class="brand-icon">
              <svg class="icon-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 00-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z" fill="currentColor"/>
              </svg>
            </div>
            <span class="brand-text">Voyage<span class="brand-highlight">AI</span></span>
          </div>
          <p class="brand-desc">成立于 2026 年，我们致力于利用先进的 AI 技术为旅行者提供最纯粹的灵感发现体验。</p>
          <div class="social-links">
            <a href="#" class="social-link">
              <svg viewBox="0 0 24 24" fill="currentColor">
                <circle cx="8" cy="10" r="4"/>
                <circle cx="16" cy="10" r="4"/>
                <circle cx="7" cy="9" r="0.8"/>
                <circle cx="9" cy="9" r="0.8"/>
                <circle cx="8" cy="11" r="0.8"/>
              </svg>
            </a>
            <a href="#" class="social-link">
              <svg viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
                </svg>
            </a>
            <a href="#" class="social-link">
              <svg viewBox="0 0 24 24" fill="currentColor">
                <path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/>
                </svg>
            </a>
          </div>
        </div>

        <div class="footer-links">
          <div class="link-group">
            <h4 class="link-title">产品</h4>
            <a href="#" class="footer-link">行程规划</a>
            <a href="#" class="footer-link">智能推荐</a>
            <a href="#" class="footer-link">预算分析</a>
            <a href="#" class="footer-link">行前清单</a>
          </div>

          <div class="link-group">
            <h4 class="link-title">资源</h4>
            <a href="#" class="footer-link">目的地指南</a>
            <a href="#" class="footer-link">旅行灵感</a>
            <a href="#" class="footer-link">社区故事</a>
            <a href="#" class="footer-link">旅行攻略</a>
          </div>

          <div class="link-group">
            <h4 class="link-title">公司</h4>
            <a href="#" class="footer-link">关于我们</a>
            <a href="#" class="footer-link">联系我们</a>
            <a href="#" class="footer-link">隐私政策</a>
            <a href="#" class="footer-link">服务条款</a>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <p class="copyright">© 2024 VoyageAI. 保留所有权利。</p>
      </div>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Result',
  data() {
    return {
      itinerary: {},
      weather: {
        temperature: 22,
        condition: '多云转晴',
        detail: '加载中...',
        icon: 'sun',
        iconClass: 'sunny',
        alert: ''
      },
      packingList: [
        {
          name: '证件与财务',
          items: [
            { name: '身份证/护照', checked: false },
            { name: '驾驶证', checked: false },
            { name: '现金与银行卡', checked: false }
          ]
        },
        {
          name: '电子设备',
          items: [
            { name: '手机与充电器', checked: false },
            { name: '相机与存储卡', checked: false },
            { name: '充电宝', checked: false }
          ]
        },
        {
          name: '个人用品',
          items: [
            { name: '洗漱用品', checked: false },
            { name: '防晒霜', checked: false },
            { name: '常用药品', checked: false }
          ]
        }
      ]
    }
  },
  computed: {
    currentDate() {
      const date = new Date()
      return `${date.getFullYear()}.${String(date.getMonth() + 1).padStart(2, '0')}.${String(date.getDate()).padStart(2, '0')}`
    },
    destinationImage() {
      const images = {
        '北京': 'https://images.unsplash.com/photo-1508804185872-d7badad00f7d?w=800&q=80',
        '上海': 'https://images.unsplash.com/photo-1538428494232-9c0d8a3ab403?w=800&q=80',
        '杭州': 'https://images.unsplash.com/photo-1599571234909-29ed5d1321d6?w=800&q=80',
        '成都': 'https://images.unsplash.com/photo-1584464491033-06628f3a6b7b?w=800&q=80',
        '西安': 'https://images.unsplash.com/photo-1598316811207-d4b2d758fd5c?w=800&q=80'
      }
      return images[this.itinerary.overview?.destination] || 'https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=800&q=80'
    },
    totalBudget() {
      if (!this.itinerary.budget_breakdown) return 0
      return this.itinerary.budget_breakdown.reduce((sum, item) => {
        const amount = typeof item.amount === 'string' 
          ? parseInt(item.amount.replace(/[^0-9]/g, '')) 
          : item.amount
        return sum + (amount || 0)
      }, 0)
    }
  },
  mounted() {
    // 获取路由参数中的行程数据
    const data = this.$route.query.data
    if (data) {
      try {
        this.itinerary = JSON.parse(data)
        this.$nextTick(() => {
          this.drawBudgetChart()
          // 获取目的地实时天气数据
          this.fetchWeatherData()
        })
      } catch (e) {
        console.error('解析行程数据失败:', e)
        this.$router.push('/')
      }
    } else {
      // 如果没有数据，返回首页
      this.$router.push('/')
    }
  },
  methods: {
    goHome() {
      this.$router.push('/')
    },
    exportResult() {
      const dataStr = JSON.stringify(this.itinerary, null, 2)
      const blob = new Blob([dataStr], { type: 'application/json' })
      const url = URL.createObjectURL(blob)
      const link = document.createElement('a')
      link.href = url
      link.download = `旅行计划_${this.itinerary.overview?.destination || '行程'}.json`
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
      URL.revokeObjectURL(url)
    },
    fetchWeatherData() {
      const destination = this.itinerary.overview?.destination
      if (!destination) return
      
      axios.get(`/api/weather?city=${encodeURIComponent(destination)}`)
        .then(response => {
          const weatherData = response.data
          this.weather = {
            temperature: parseInt(weatherData.temp.replace('°C', '')),
            condition: weatherData.condition,
            detail: weatherData.warning || '天气适宜出行。',
            icon: weatherData.condition.includes('晴') ? 'sun' : 'cloud',
            iconClass: weatherData.condition.includes('晴') ? 'sunny' : 'cloudy',
            alert: weatherData.warning || ''
          }
        })
        .catch(error => {
          console.error('获取天气数据失败:', error)
          this.weather = {
            temperature: 22,
            condition: '多云转晴',
            detail: '天气数据获取失败',
            icon: 'sun',
            iconClass: 'sunny',
            alert: ''
          }
        })
    },
    drawBudgetChart() {
      const canvas = this.$refs.budgetChart
      if (!canvas) return
      
      const ctx = canvas.getContext('2d')
      const dpr = window.devicePixelRatio || 1
      const rect = canvas.getBoundingClientRect()
      
      canvas.width = rect.width * dpr
      canvas.height = rect.height * dpr
      ctx.scale(dpr, dpr)
      
      const categories = this.itinerary.budget_breakdown || []
      if (categories.length === 0) return
      
      const colors = ['#10B981', '#3B82F6', '#8B5CF6', '#F59E0B', '#EF4444', '#EC4899']
      const total = categories.reduce((sum, cat) => {
        const amount = typeof cat.amount === 'string' 
          ? parseInt(cat.amount.replace(/[^0-9]/g, '')) 
          : cat.amount
        return sum + (amount || 0)
      }, 0)
      
      // 绘制环形图
      const centerX = rect.width / 2
      const centerY = rect.height / 2 - 10
      const radius = Math.min(centerX, centerY) - 20
      const innerRadius = radius * 0.6
      
      let currentAngle = -Math.PI / 2
      
      categories.forEach((cat, index) => {
        const amount = typeof cat.amount === 'string' 
          ? parseInt(cat.amount.replace(/[^0-9]/g, '')) 
          : cat.amount
        const percentage = (amount || 0) / total
        const angle = percentage * Math.PI * 2
        
        // 绘制扇形
        ctx.beginPath()
        ctx.arc(centerX, centerY, radius, currentAngle, currentAngle + angle)
        ctx.arc(centerX, centerY, innerRadius, currentAngle + angle, currentAngle, true)
        ctx.closePath()
        ctx.fillStyle = colors[index % colors.length]
        ctx.fill()
        
        currentAngle += angle
      })
      
      // 绘制中心文字
      ctx.fillStyle = '#1e293b'
      ctx.font = 'bold 20px Inter, sans-serif'
      ctx.textAlign = 'center'
      ctx.textBaseline = 'middle'
      ctx.fillText('¥' + total.toLocaleString(), centerX, centerY - 5)
      
      ctx.fillStyle = '#64748b'
      ctx.font = '12px Inter, sans-serif'
      ctx.fillText('总预算', centerX, centerY + 15)
      
      // 绘制图例
      let legendY = rect.height - 30
      const legendItemWidth = rect.width / Math.min(categories.length, 3)
      
      categories.slice(0, 3).forEach((cat, index) => {
        const x = legendItemWidth * index + legendItemWidth / 2 - 30
        
        ctx.fillStyle = colors[index % colors.length]
        ctx.fillRect(x, legendY, 12, 12)
        
        ctx.fillStyle = '#64748b'
        ctx.font = '11px Inter, sans-serif'
        ctx.textAlign = 'left'
        ctx.fillText(cat.category || '其他', x + 18, legendY + 9)
      })
    }
  }
}
</script>

<style scoped>
.result-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
  padding-top: 80px;
}

/* 导航栏 */
.nav-bar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 2rem;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.5);
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.05);
}

.nav-brand {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  cursor: pointer;
}

.nav-links {
  display: flex;
  gap: 2rem;
}

.nav-link {
  position: relative;
  color: #64748b;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
  padding: 0.5rem 0;
}

.nav-link:hover {
  color: #1e293b;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: linear-gradient(135deg, #10B981, #3B82F6);
  transition: width 0.3s ease;
}

.nav-link:hover::after {
  width: 100%;
}

.brand-icon {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #10B981, #059669);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.icon-svg {
  width: 24px;
  height: 24px;
  color: white;
}

.brand-text {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1e293b;
}

.brand-highlight {
  background: linear-gradient(135deg, #10B981, #3B82F6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.nav-actions {
  display: flex;
  gap: 0.75rem;
}

.btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.6rem 1.25rem;
  border-radius: 9999px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
}

.btn svg {
  width: 18px;
  height: 18px;
}

.btn-outline {
  background: transparent;
  border: 1.5px solid #e2e8f0;
  color: #64748b;
}

.btn-outline:hover {
  border-color: #10B981;
  color: #10B981;
  background: rgba(16, 185, 129, 0.05);
}

.btn-primary {
  background: linear-gradient(135deg, #10B981, #059669);
  color: white;
  box-shadow: 0 4px 14px rgba(16, 185, 129, 0.35);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(16, 185, 129, 0.45);
}

/* 主内容区 */
.result-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

/* 概览卡片 */
.overview-card {
  display: flex;
  gap: 2rem;
  padding: 2rem;
  border-radius: 2rem;
  margin-bottom: 2rem;
  overflow: hidden;
}

.overview-image {
  position: relative;
  width: 300px;
  height: 200px;
  border-radius: 1.5rem;
  overflow: hidden;
  flex-shrink: 0;
}

.overview-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.overview-image:hover img {
  transform: scale(1.05);
}

.image-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 1rem;
  background: linear-gradient(to top, rgba(0,0,0,0.6), transparent);
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
}

.badge {
  background: linear-gradient(135deg, #10B981, #059669);
  color: white;
  padding: 0.35rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.date {
  color: rgba(255, 255, 255, 0.9);
  font-size: 0.8rem;
}

.overview-info {
  flex: 1;
}

.overview-title {
  font-size: 2rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 1.5rem;
}

.destination {
  background: linear-gradient(135deg, #10B981, #3B82F6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.overview-stats {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
}

.stat-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.6);
  border-radius: 1rem;
  transition: all 0.3s ease;
}

.stat-item:hover {
  background: rgba(255, 255, 255, 0.9);
  transform: translateY(-2px);
}

.stat-icon {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.stat-icon svg {
  width: 22px;
  height: 22px;
  color: white;
}

.bg-emerald-light { background: linear-gradient(135deg, #10B981, #34D399); }
.bg-amber-light { background: linear-gradient(135deg, #F59E0B, #FBBF24); }
.bg-blue-light { background: linear-gradient(135deg, #3B82F6, #60A5FA); }
.bg-purple-light { background: linear-gradient(135deg, #8B5CF6, #A78BFA); }

.stat-content {
  display: flex;
  flex-direction: column;
}

.stat-label {
  font-size: 0.75rem;
  color: #94a3b8;
  margin-bottom: 0.25rem;
}

.stat-value {
  font-size: 1rem;
  font-weight: 700;
  color: #1e293b;
}

/* 主网格布局 */
.main-grid {
  display: grid;
  grid-template-columns: 1fr 380px;
  gap: 2rem;
}

/* 时间轴区域 */
.timeline-section {
  background: rgba(255, 255, 255, 0.5);
  border-radius: 2rem;
  padding: 2rem;
}

.section-header {
  margin-bottom: 1.5rem;
}

.section-title {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 1.25rem;
  font-weight: 700;
  color: #1e293b;
}

.section-title svg {
  width: 24px;
  height: 24px;
  color: #10B981;
}

.timeline {
  position: relative;
}

.timeline-day {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 2rem;
  opacity: 0;
  animation: fadeInUp 0.6s ease forwards;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.timeline-marker {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex-shrink: 0;
}

.marker-dot {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #10B981, #059669);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.9rem;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
  transition: all 0.3s ease;
}

.marker-dot:hover {
  transform: scale(1.1);
  box-shadow: 0 6px 20px rgba(16, 185, 129, 0.4);
}

.marker-line {
  width: 2px;
  flex: 1;
  background: linear-gradient(to bottom, #10B981, transparent);
  margin-top: 0.5rem;
  min-height: 40px;
}

.timeline-content {
  flex: 1;
}

.day-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.day-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: #1e293b;
}

.day-theme {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(59, 130, 246, 0.1));
  color: #10B981;
  padding: 0.35rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.8rem;
  font-weight: 600;
}

.activities {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.activity-card {
  padding: 1.25rem;
  border-radius: 1rem;
  transition: all 0.3s ease;
}

.activity-card:hover {
  transform: translateX(4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
}

.activity-time {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.8rem;
  color: #10B981;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.activity-time svg {
  width: 14px;
  height: 14px;
}

.activity-name {
  font-size: 1rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.activity-desc {
  font-size: 0.9rem;
  color: #64748b;
  line-height: 1.6;
  margin-bottom: 0.75rem;
}

.activity-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tag {
  background: rgba(16, 185, 129, 0.1);
  color: #10B981;
  padding: 0.25rem 0.6rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 500;
}

/* 侧边栏 */
.sidebar {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.sidebar-card {
  padding: 1.5rem;
  border-radius: 1.5rem;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.25rem;
}

.card-header h3 {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1rem;
  font-weight: 700;
  color: #1e293b;
}

.card-header h3 svg {
  width: 20px;
  height: 20px;
  color: #10B981;
}

.city {
  font-size: 0.75rem;
  color: #94a3b8;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* 天气组件 */
.weather-main {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.weather-temp {
  font-size: 3rem;
  font-weight: 700;
  color: #1e293b;
  line-height: 1;
}

.weather-info {
  flex: 1;
}

.weather-condition {
  font-size: 1rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.25rem;
}

.weather-detail {
  font-size: 0.8rem;
  color: #94a3b8;
}

.weather-icon {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.weather-icon.sunny {
  background: linear-gradient(135deg, #FCD34D, #F59E0B);
}

.weather-icon svg {
  width: 36px;
  height: 36px;
  color: white;
}

.weather-alert {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  padding: 1rem;
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.1), rgba(245, 158, 11, 0.05));
  border-radius: 1rem;
  border: 1px solid rgba(245, 158, 11, 0.2);
}

.weather-alert svg {
  width: 20px;
  height: 20px;
  color: #F59E0B;
  flex-shrink: 0;
}

.weather-alert p {
  font-size: 0.85rem;
  color: #92400e;
  line-height: 1.5;
}

/* 预算图表 */
.budget-chart-container {
  display: flex;
  justify-content: center;
  margin-bottom: 1rem;
}

.budget-chart-container canvas {
  max-width: 100%;
}

.budget-summary {
  border-top: 1px solid #e2e8f0;
  padding-top: 1rem;
}

.budget-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.budget-label {
  font-size: 0.85rem;
  color: #64748b;
}

.budget-value {
  font-size: 1rem;
  font-weight: 700;
  color: #1e293b;
}

.budget-savings {
  font-size: 0.9rem;
  font-weight: 600;
  color: #10B981;
}

.budget-item.highlight {
  padding: 0.5rem;
  background: rgba(16, 185, 129, 0.05);
  border-radius: 0.5rem;
}

/* 行前清单 */
.packing-category {
  margin-bottom: 1.25rem;
}

.packing-category:last-child {
  margin-bottom: 0;
}

.category-title {
  font-size: 0.85rem;
  font-weight: 600;
  color: #64748b;
  margin-bottom: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.category-items {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.packing-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.5rem;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.packing-item:hover {
  background: rgba(16, 185, 129, 0.05);
}

.custom-checkbox {
  width: 20px;
  height: 20px;
  border: 2px solid #d1d5db;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  appearance: none;
  position: relative;
}

.custom-checkbox:checked {
  background: #10B981;
  border-color: #10B981;
}

.custom-checkbox:checked::after {
  content: '✓';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-size: 12px;
  font-weight: bold;
}

.item-name {
  font-size: 0.9rem;
  color: #1e293b;
  transition: all 0.2s ease;
}

.item-name.checked {
  text-decoration: line-through;
  color: #94a3b8;
}

/* Pro 卡片 */
.pro-card {
  position: relative;
  padding: 1.5rem;
  background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
  border-radius: 1.5rem;
  color: white;
  overflow: hidden;
}

.pro-bg {
  position: absolute;
  top: -20px;
  right: -20px;
  width: 100px;
  height: 100px;
  opacity: 0.1;
}

.pro-bg svg {
  width: 100%;
  height: 100%;
}

.pro-badge {
  display: inline-block;
  background: linear-gradient(135deg, #10B981, #059669);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 0.75rem;
}

.pro-card h4 {
  font-size: 1.1rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.pro-card p {
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: 1rem;
  line-height: 1.5;
}

.pro-btn {
  width: 100%;
  padding: 0.75rem;
  background: linear-gradient(135deg, #10B981, #059669);
  color: white;
  border: none;
  border-radius: 0.75rem;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.pro-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.4);
}

/* 玻璃卡片效果 */
.glass-card {
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.5);
  box-shadow: 0 8px 32px rgba(31, 38, 135, 0.07);
}

.card-hover {
  transition: all 0.3s ease;
}

.card-hover:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(31, 38, 135, 0.12);
}

/* 底部导航栏 */
.footer {
  background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
  padding: 4rem 2rem 2rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  margin-top: 4rem;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 3fr;
  gap: 4rem;
  align-items: start;
}

.footer-brand {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.brand-header {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.brand-desc {
  color: #64748b;
  font-size: 0.95rem;
  line-height: 1.6;
  max-width: 300px;
}

.footer-links {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
  align-items: start;
}

.link-group {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.link-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.footer-link {
  color: #64748b;
  text-decoration: none;
  font-size: 0.95rem;
  transition: all 0.3s ease;
}

.footer-link:hover {
  color: #10B981;
  transform: translateX(4px);
}

.social-links {
  display: flex;
  gap: 1rem;
  margin-top: 0.5rem;
  align-items: center;
}

.social-link {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #64748b;
  text-decoration: none;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.social-link:hover {
  transform: translateY(-4px);
  color: #10B981;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.social-link svg {
  width: 20px;
  height: 20px;
}

.footer-bottom {
  max-width: 1200px;
  margin: 3rem auto 0;
  padding-top: 2rem;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
  text-align: center;
}

.copyright {
  color: #64748b;
  font-size: 0.9rem;
}

/* 响应式设计 */
@media (max-width: 1024px) {
  .main-grid {
    grid-template-columns: 1fr;
  }
  
  .overview-card {
    flex-direction: column;
  }
  
  .overview-image {
    width: 100%;
    height: 200px;
  }
  
  .overview-stats {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .result-content {
    padding: 1rem;
  }
  
  .nav-bar {
    padding: 1rem;
  }
  
  .nav-actions .btn span {
    display: none;
  }
  
  .overview-stats {
    grid-template-columns: 1fr;
  }
  
  .timeline-day {
    flex-direction: column;
    gap: 1rem;
  }
  
  .timeline-marker {
    flex-direction: row;
    align-items: center;
  }
  
  .marker-line {
    width: 40px;
    height: 2px;
    margin: 0 0.5rem;
    min-height: auto;
  }
  
  /* 移动端底部导航栏 */
  .footer {
    padding: 3rem 1rem 1.5rem;
  }
  
  .footer-content {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .footer-links {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
  }
  
  .footer-bottom {
    margin-top: 2rem;
    padding-top: 1.5rem;
  }
}
</style>
