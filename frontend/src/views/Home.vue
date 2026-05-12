<template>
  <div class="home-container">
    <!-- 导航栏 -->
    <nav class="nav-bar">
      <div class="nav-brand">
        <div class="brand-icon">
          <svg class="icon-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 00-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z" fill="currentColor"/>
          </svg>
        </div>
        <router-link to="/" class="brand-text-link">
          <span class="brand-text">Voyage<span class="brand-highlight">AI</span></span>
        </router-link>
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
        <button class="btn btn-outline theme-toggle" @click="toggleTheme" :title="isDark ? '切换浅色' : '切换深色'">
          <svg v-if="!isDark" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
          <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
        </button>
        <button class="btn btn-primary desktop-only">开启探索</button>
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
          <button class="btn btn-primary mobile-cta" @click="$router.push('/'); menuOpen = false">开启探索</button>
        </div>
      </transition>
    </nav>

    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-bg">
        <!-- Travel scene background (image). Swap to video if needed. -->
        <div class="hero-media" aria-hidden="true"></div>
        <div class="hero-gradient"></div>
      </div>
      <div class="hero-content">
        <h1 class="hero-title serif">
          远航<span class="gradient-text">AI</span>
        </h1>
        <p class="hero-subtitle gradient-text">让每一次思考都更有方向 · 3秒生成个性化旅行行程 · AI智能规划</p>

        <div class="search-card glass-card">
          <div class="search-fields">
            <div class="field-group">
              <label class="field-label">出发地</label>
              <div class="field-input-wrapper">
                <svg class="field-icon text-emerald" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
                <input v-model="form.start" type="text" :class="['field-input', { error: errors.start }]" placeholder="哪个城市出发？">
              </div>
              <div v-if="errors.start" class="error-message">{{ errors.start }}</div>
            </div>
            <div class="field-divider"></div>
            <div class="field-group">
              <label class="field-label">目的地</label>
              <div class="field-input-wrapper">
                <svg class="field-icon text-blue" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>
                <input v-model="form.dest" type="text" :class="['field-input', { error: errors.dest }]" placeholder="想去哪里？">
              </div>
              <div v-if="errors.dest" class="error-message">{{ errors.dest }}</div>
            </div>
            <div class="field-divider"></div>
            <div class="field-group">
              <label class="field-label">游玩天数</label>
              <div class="field-input-wrapper">
                <svg class="field-icon text-purple" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                <input v-model="form.days" type="number" :class="['field-input', { error: errors.days }]" placeholder="几天时间？" min="1" max="30">
              </div>
              <div v-if="errors.days" class="error-message">{{ errors.days }}</div>
            </div>
            <div class="field-divider"></div>
            <div class="field-group">
              <label class="field-label">预算范围</label>
              <div class="field-input-wrapper">
                <svg class="field-icon text-amber" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="5" width="20" height="14" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/></svg>
                <input v-model="form.budget" type="text" :class="['field-input', { error: errors.budget }]" placeholder="预算范围？">
              </div>
              <div v-if="errors.budget" class="error-message">{{ errors.budget }}</div>
            </div>
            <div class="field-divider"></div>
            <div class="field-group">
              <label class="field-label">出发日期</label>
              <div class="field-input-wrapper">
                <svg class="field-icon text-blue" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                <input v-model="form.date" type="date" class="field-input" placeholder="哪天出发？">
              </div>
            </div>
            <div class="field-divider"></div>
            <div class="field-group">
              <label class="field-label">人数</label>
              <div class="field-input-wrapper">
                <svg class="field-icon text-purple" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg>
                <input v-model.number="form.travelers" type="number" min="1" max="50" class="field-input" placeholder="几人同行？">
              </div>
            </div>
          </div>

          <!-- Preference tags -->
          <div class="pref-section">
            <span class="pref-label">旅行偏好（可多选）</span>
            <div class="pref-chips">
              <button
                v-for="p in prefOptions"
                :key="p.key"
                class="pref-chip"
                :class="{ active: selectedPrefs.includes(p.key) }"
                type="button"
                @click="togglePref(p.key)"
              >
                <span class="pref-chip-icon">{{ p.icon }}</span>
                {{ p.label }}
              </button>
            </div>
          </div>

          <button class="search-btn" @click="startPlanning" :disabled="loading">
            <span v-if="!loading">帮我规划</span>
            <span v-else>规划中...</span>
            <svg class="btn-icon" :class="{ rotating: loading }" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
          </button>

          <!-- Quick examples -->
          <div class="quick-examples" aria-label="快速示例">
            <button
              v-for="ex in quickExamples"
              :key="ex.id"
              class="example-chip"
              type="button"
              @click="applyExample(ex)"
            >
              <span class="chip-ai" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none">
                  <path d="M12 2l1.2 4.3L17.5 8l-4.3 1.2L12 13.5l-1.2-4.3L6.5 8l4.3-1.7L12 2z" fill="currentColor" opacity="0.95"/>
                  <path d="M19 12l.8 2.8L22.5 16l-2.7.8L19 19.5l-.8-2.7L15.5 16l2.7-1.2L19 12z" fill="currentColor" opacity="0.65"/>
                </svg>
              </span>
              <span class="chip-text">{{ ex.text }}</span>
            </button>
          </div>
        </div>

        <!-- AI prompt box: chat-like entry point -->
        <div class="ai-entry" aria-label="AI 输入区">
          <div class="ai-entry-head">
            <div class="ai-entry-title">
              <span class="ai-pill" aria-hidden="true">
                <span class="ai-pill-dot"></span>AI
              </span>
              <span>直接描述你的需求</span>
            </div>
            <button class="ai-entry-cta" type="button" @click="openPlannerWithDemo">
              查看演示样例 →
            </button>
          </div>
          <div class="ai-entry-box">
            <textarea
              v-model="aiPrompt"
              class="ai-textarea"
              rows="3"
              placeholder="例如：帮我规划 5 天东京自由行，预算适中，喜欢美食和二次元"
              @keydown.ctrl.enter.prevent="sendPrompt"
            ></textarea>
            <button class="ai-send" type="button" :disabled="loading || !aiPrompt.trim()" @click="sendPrompt">
              <span>发送</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M22 2L11 13" />
                <path d="M22 2L15 22l-4-9-9-4 20-7z" />
              </svg>
            </button>
          </div>
          <div class="ai-entry-hint">提示：按 <strong>Ctrl + Enter</strong> 发送</div>
        </div>
      </div>
    </section>

    <!-- 功能卡片区域 -->
    <section class="features-section">
      <div class="section-head">
        <h2 class="section-title serif">一站式服务</h2>
      </div>
      <div class="features-grid">
        <router-link to="/inspiration" class="feature-card feature-card--image card-hover">
          <div class="feature-media" aria-hidden="true">
            <div class="media-img media-img--inspiration"></div>
            <div class="media-overlay"></div>
            <div class="ai-badge">
              <span class="ai-dot" aria-hidden="true"></span>
              <span class="ai-text">AI</span>
            </div>
          </div>
          <div class="feature-body">
            <div class="feature-top">
              <h3 class="feature-title">灵感发现</h3>
            </div>
            <p class="feature-desc">探索未知与小众路线，AI 为你生成灵感清单与最佳出行时机。</p>
            <span class="feature-btn-text">立即探索 →</span>
          </div>
        </router-link>

        <router-link to="/guide" class="feature-card feature-card--image card-hover">
          <div class="feature-media" aria-hidden="true">
            <div class="media-img media-img--guide"></div>
            <div class="media-overlay"></div>
            <div class="ai-badge ai-badge--blue">
              <span class="ai-dot" aria-hidden="true"></span>
              <span class="ai-text">AI</span>
            </div>
          </div>
          <div class="feature-body">
            <div class="feature-top">
              <h3 class="feature-title">目的地指南</h3>
            </div>
            <p class="feature-desc">美食、文化与玩法路线一站式整理，快速了解“怎么玩才地道”。</p>
            <span class="feature-btn-text">查看指南 →</span>
          </div>
        </router-link>

        <router-link to="/community" class="feature-card feature-card--image card-hover">
          <div class="feature-media" aria-hidden="true">
            <div class="media-img media-img--community"></div>
            <div class="media-overlay"></div>
            <div class="ai-badge ai-badge--purple">
              <span class="ai-dot" aria-hidden="true"></span>
              <span class="ai-text">AI</span>
            </div>
          </div>
          <div class="feature-body">
            <div class="feature-top">
              <h3 class="feature-title">社区足迹</h3>
            </div>
            <p class="feature-desc">真实旅行者的照片与故事，找到最适合你的玩法与避坑建议。</p>
            <span class="feature-btn-text">查看足迹 →</span>
          </div>
        </router-link>
      </div>
    </section>

    <!-- 评价 / 信任徽章 -->
    <section class="social-proof">
      <div class="social-proof-inner">
        <div class="proof-header">
          <h2 class="proof-title serif">用户声音</h2>
        </div>

        <div class="testimonials-marquee" aria-label="用户评价滚动">
          <div class="marquee-viewport">
            <div class="marquee-track">
              <article v-for="t in testimonials" :key="`a-${t.id}`" class="testimonial-card">
                <div class="t-top">
                  <div class="avatar" :style="{ background: t.avatarBg }" aria-hidden="true">
                    <span class="avatar-text">{{ t.initials }}</span>
                  </div>
                  <div class="t-meta">
                    <div class="t-name">{{ t.name }}</div>
                    <div class="t-sub">{{ t.meta }}</div>
                  </div>
                  <div class="t-rating" :aria-label="`评分 ${t.rating} / 5`">
                    <span v-for="n in 5" :key="n" class="star" :class="{ on: n <= t.rating }">★</span>
                  </div>
                </div>
                <p class="t-quote">“{{ t.quote }}”</p>
                <div class="t-tags">
                  <span v-for="tag in t.tags" :key="tag" class="tag">{{ tag }}</span>
                </div>
              </article>

              <!-- duplicate for seamless loop -->
              <article v-for="t in testimonials" :key="`b-${t.id}`" class="testimonial-card" aria-hidden="true">
                <div class="t-top">
                  <div class="avatar" :style="{ background: t.avatarBg }" aria-hidden="true">
                    <span class="avatar-text">{{ t.initials }}</span>
                  </div>
                  <div class="t-meta">
                    <div class="t-name">{{ t.name }}</div>
                    <div class="t-sub">{{ t.meta }}</div>
                  </div>
                  <div class="t-rating" aria-hidden="true">
                    <span v-for="n in 5" :key="n" class="star" :class="{ on: n <= t.rating }">★</span>
                  </div>
                </div>
                <p class="t-quote">“{{ t.quote }}”</p>
                <div class="t-tags">
                  <span v-for="tag in t.tags" :key="tag" class="tag">{{ tag }}</span>
                </div>
              </article>
            </div>
          </div>
        </div>

        <div class="testimonials-marquee testimonials-marquee--second" aria-label="用户评价滚动（第二行）">
          <div class="marquee-viewport">
            <div class="marquee-track marquee-track--reverse">
              <article v-for="t in testimonials" :key="`c-${t.id}`" class="testimonial-card">
                <div class="t-top">
                  <div class="avatar" :style="{ background: t.avatarBg }" aria-hidden="true">
                    <span class="avatar-text">{{ t.initials }}</span>
                  </div>
                  <div class="t-meta">
                    <div class="t-name">{{ t.name }}</div>
                    <div class="t-sub">{{ t.meta }}</div>
                  </div>
                  <div class="t-rating" :aria-label="`评分 ${t.rating} / 5`">
                    <span v-for="n in 5" :key="n" class="star" :class="{ on: n <= t.rating }">★</span>
                  </div>
                </div>
                <p class="t-quote">“{{ t.quote }}”</p>
                <div class="t-tags">
                  <span v-for="tag in t.tags" :key="tag" class="tag">{{ tag }}</span>
                </div>
              </article>

              <!-- duplicate for seamless loop -->
              <article v-for="t in testimonials" :key="`d-${t.id}`" class="testimonial-card" aria-hidden="true">
                <div class="t-top">
                  <div class="avatar" :style="{ background: t.avatarBg }" aria-hidden="true">
                    <span class="avatar-text">{{ t.initials }}</span>
                  </div>
                  <div class="t-meta">
                    <div class="t-name">{{ t.name }}</div>
                    <div class="t-sub">{{ t.meta }}</div>
                  </div>
                  <div class="t-rating" aria-hidden="true">
                    <span v-for="n in 5" :key="n" class="star" :class="{ on: n <= t.rating }">★</span>
                  </div>
                </div>
                <p class="t-quote">“{{ t.quote }}”</p>
                <div class="t-tags">
                  <span v-for="tag in t.tags" :key="tag" class="tag">{{ tag }}</span>
                </div>
              </article>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Demo itinerary (always visible value preview) -->
    <section class="demo-section">
      <div class="demo-inner">
        <div class="demo-head">
          <h2 class="demo-title serif">5 天行程演示（示例）</h2>
          <p class="demo-subtitle">让你不点任何按钮，也能一眼看到 VoyageAI 能输出什么。</p>
          <button class="demo-open" type="button" @click="openPlannerWithDemo">在规划器里查看 →</button>
        </div>

        <div v-if="demoLoading" class="demo-loading">正在加载示例行程...</div>
        <div v-else-if="demoItinerary" class="demo-grid">
          <div class="demo-card">
            <div class="demo-kpi">
              <div class="kpi-label">目的地</div>
              <div class="kpi-value">{{ demoItinerary.overview?.destination || '—' }}</div>
            </div>
            <div class="demo-kpi">
              <div class="kpi-label">天数</div>
              <div class="kpi-value">{{ demoItinerary.overview?.days || 5 }} 天</div>
            </div>
            <div class="demo-kpi">
              <div class="kpi-label">预算</div>
              <div class="kpi-value">{{ demoItinerary.overview?.budget || '—' }}</div>
            </div>
          </div>
          <div class="demo-card demo-card--wide">
            <div class="demo-list-title">每日安排（节选）</div>
            <div class="demo-days">
              <div v-for="d in (demoItinerary.daily_plan || []).slice(0, 3)" :key="d.day" class="demo-day">
                <div class="day-badge">Day {{ d.day }}</div>
                <div class="day-title">{{ d.title }}</div>
              </div>
            </div>
          </div>
          <div class="demo-card demo-card--wide">
            <div class="demo-list-title">预算拆分</div>
            <div class="demo-budget">
              <div v-for="b in (demoItinerary.budget_breakdown || [])" :key="b.category" class="budget-row">
                <span class="budget-cat">{{ b.category }}</span>
                <span class="budget-amt">¥ {{ b.amount }}</span>
              </div>
            </div>
          </div>

          <div class="demo-card">
            <div class="demo-list-title">行前清单（节选）</div>
            <div class="demo-pack">
              <span v-for="item in (demoItinerary.packing_list || []).slice(0, 10)" :key="item" class="demo-pack-item">
                {{ item }}
              </span>
            </div>
            <div class="demo-pack-hint">更多内容在规划器与结果页中查看。</div>
          </div>
        </div>
        <div v-else class="demo-loading">示例行程暂不可用（稍后重试）。</div>
      </div>
    </section>

    <!-- 历史行程 -->
    <section class="history-section">
      <div class="history-inner">
        <div class="section-head">
          <h2 class="section-title serif">我的历史行程</h2>
          <span class="history-count" v-if="historyTotal">{{ historyTotal }} 条记录</span>
        </div>

        <div v-if="historyLoading" class="history-loading">加载中...</div>

        <div v-else-if="historyItems.length" class="history-scroll">
          <div
            v-for="item in historyItems"
            :key="item.id"
            class="history-card card-hover"
            @click="openHistoryDetail(item.id)"
          >
            <div class="h-card-top">
              <div class="h-dest">{{ item.destination }}</div>
              <div class="h-date">{{ formatDate(item.created_at) }}</div>
            </div>
            <div class="h-card-body">
              <div class="h-stat">
                <span class="h-label">出发</span>
                <span class="h-val">{{ item.start_location }}</span>
              </div>
              <div class="h-stat">
                <span class="h-label">天数</span>
                <span class="h-val">{{ item.days }}天</span>
              </div>
              <div class="h-stat">
                <span class="h-label">预算</span>
                <span class="h-val">{{ item.budget }}</span>
              </div>
            </div>
          </div>
        </div>

        <div v-else class="history-empty">还没有行程记录，去首页生成一个吧。</div>
      </div>

      <!-- 历史详情弹窗 -->
      <transition name="fade">
        <div
          v-if="historyDetailOpen"
          class="history-detail-backdrop"
          @click.self="historyDetailOpen = false"
        >
          <div class="history-detail">
            <div class="hd-head">
              <h3 class="hd-title">行程详情</h3>
              <button class="hd-close" @click="historyDetailOpen = false">✕</button>
            </div>
            <div v-if="historyDetailLoading" class="hd-loading">加载中...</div>
            <div v-else-if="historyDetail" class="hd-body">
              <div class="hd-kpis">
                <div class="hd-kpi">
                  <span class="hd-kpi-label">目的地</span>
                  <span class="hd-kpi-val">{{ historyDetail.destination }}</span>
                </div>
                <div class="hd-kpi">
                  <span class="hd-kpi-label">出发地</span>
                  <span class="hd-kpi-val">{{ historyDetail.start_location }}</span>
                </div>
                <div class="hd-kpi">
                  <span class="hd-kpi-label">天数</span>
                  <span class="hd-kpi-val">{{ historyDetail.days }} 天</span>
                </div>
                <div class="hd-kpi">
                  <span class="hd-kpi-label">预算</span>
                  <span class="hd-kpi-val">{{ historyDetail.budget }}</span>
                </div>
              </div>

              <div class="hd-block" v-if="historyDetail.overview && Object.keys(historyDetail.overview).length">
                <div class="hd-block-title">概览</div>
                <div class="hd-overview-grid">
                  <div class="hd-ov-item" v-if="historyDetail.overview.best_season">
                    <span class="hd-ov-label">最佳季节</span>
                    <span class="hd-ov-val">{{ historyDetail.overview.best_season }}</span>
                  </div>
                  <div class="hd-ov-item" v-if="historyDetail.overview.pace">
                    <span class="hd-ov-label">游玩节奏</span>
                    <span class="hd-ov-val">{{ historyDetail.overview.pace }}</span>
                  </div>
                </div>
              </div>

              <div class="hd-block" v-if="historyDetail.daily_plan && historyDetail.daily_plan.length">
                <div class="hd-block-title">每日安排</div>
                <div class="hd-days">
                  <div v-for="d in historyDetail.daily_plan" :key="d.day" class="hd-day">
                    <div class="hd-day-head">
                      <span class="hd-day-badge">Day {{ d.day }}</span>
                      <span class="hd-day-name">{{ d.title }}</span>
                    </div>
                    <div class="hd-acts" v-if="d.activities && d.activities.length">
                      <div v-for="(a, ai) in d.activities" :key="ai" class="hd-act">
                        <span class="hd-act-time">{{ a.time }}</span>
                        <span class="hd-act-title">{{ a.title }}</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div class="hd-block" v-if="historyDetail.budget_breakdown && historyDetail.budget_breakdown.length">
                <div class="hd-block-title">预算拆分</div>
                <div class="hd-budget">
                  <div v-for="b in historyDetail.budget_breakdown" :key="b.category" class="hd-budget-row">
                    <span>{{ b.category }}</span>
                    <span class="hd-budget-amt">¥{{ b.amount }}</span>
                  </div>
                </div>
              </div>

              <div class="hd-block" v-if="historyDetail.packing_list && historyDetail.packing_list.length">
                <div class="hd-block-title">行前清单</div>
                <div class="hd-pack">
                  <span v-for="p in historyDetail.packing_list" :key="p" class="hd-pack-item">{{ p }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </section>

    <!-- 底部 -->
    <footer class="footer">
      <div class="footer-content">
        <div class="footer-brand">
          <div class="brand-header">
            <div class="brand-icon">
              <svg class="icon-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 00-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z" fill="currentColor"/>
              </svg>
            </div>
            <router-link to="/" class="brand-text-link"><span class="brand-text">Voyage<span class="brand-highlight">AI</span></span></router-link>
          </div>
          <p class="brand-desc">成立于 2026 年，我们致力于利用先进的 AI 技术为旅行者提供最纯粹的灵感发现体验。</p>
        </div>
        <div class="footer-links">
          <div class="link-group">
            <h4 class="link-title">产品</h4>
            <router-link to="/" class="footer-link">行程规划</router-link>
            <router-link to="/inspiration" class="footer-link">智能推荐</router-link>
            <router-link to="/guide" class="footer-link">预算分析</router-link>
            <router-link to="/community" class="footer-link">行前清单</router-link>
          </div>
          <div class="link-group">
            <h4 class="link-title">资源</h4>
            <router-link to="/guide" class="footer-link">目的地指南</router-link>
            <router-link to="/inspiration" class="footer-link">旅行灵感</router-link>
            <router-link to="/community" class="footer-link">社区故事</router-link>
            <router-link to="/about" class="footer-link">旅行攻略</router-link>
          </div>
          <div class="link-group">
            <h4 class="link-title">公司</h4>
            <router-link to="/about" class="footer-link">关于我们</router-link>
            <router-link to="/about" class="footer-link">联系我们</router-link>
            <router-link to="/about" class="footer-link">隐私政策</router-link>
            <router-link to="/about" class="footer-link">服务条款</router-link>
          </div>
        </div>
      </div>
      <div class="footer-trust">
        <div class="trust-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0" stroke-linecap="round"/></svg>
          <span>基于先进大模型</span>
        </div>
        <div class="trust-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4" stroke-linecap="round"/></svg>
          <span>数据安全保障</span>
        </div>
        <div class="trust-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2" stroke-linecap="round"/></svg>
          <span>秒级智能响应</span>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="copyright">© 2026 VoyageAI. 保留所有权利。</p>
      </div>
    </footer>

    <!-- 加载遮罩层 -->
    <transition name="fade">
      <div v-if="loading" class="loading-overlay">
        <div class="loading-content">
          <div class="loading-spinner">
            <div class="spinner-ring"></div>
            <div class="spinner-icon">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 00-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z"/></svg>
            </div>
          </div>
          <h2 class="loading-title serif">VoyageAI 正在思考...</h2>
          <p class="loading-text loader-dots">正在分析目的地实时交通与天气数据<span>.</span><span>.</span><span>.</span></p>
          <div class="loading-progress">
            <div class="progress-bar" :style="{ width: loadingProgress + '%' }"></div>
          </div>
        </div>
      </div>
    </transition>

    <!-- Planner drawer / fullscreen -->
    <transition name="drawer">
      <div v-if="plannerOpen" class="drawer-backdrop" @click.self="closePlanner" aria-label="AI 规划器">
        <div class="drawer">
          <div class="drawer-head">
            <div class="drawer-title">
              <span class="drawer-ai">AI</span>
              <span>旅行规划器</span>
            </div>
            <button class="drawer-close" type="button" @click="closePlanner" aria-label="关闭">✕</button>
          </div>

          <div class="drawer-body">
            <div class="drawer-input">
              <textarea
                v-model="aiPrompt"
                class="drawer-textarea"
                rows="3"
                placeholder="描述你的旅行需求（可包含：出发地、目的地、天数、预算、偏好）"
                @keydown.ctrl.enter.prevent="sendPrompt"
              ></textarea>
              <div class="drawer-actions">
                <button class="drawer-btn drawer-btn--secondary" type="button" @click="useDemoPrompt">
                  使用演示示例
                </button>
                <button class="drawer-btn drawer-btn--primary" type="button" :disabled="loading || !aiPrompt.trim()" @click="sendPrompt">
                  生成预览
                </button>
              </div>
            </div>

            <div v-if="plannerError" class="drawer-error">{{ plannerError }}</div>

            <div v-if="plannerItinerary" class="drawer-preview">
              <div class="preview-grid">
                <div class="preview-card">
                  <div class="preview-title">行程概览</div>
                  <div class="preview-kpis">
                    <div class="kpi">
                      <div class="kpi-k">目的地</div>
                      <div class="kpi-v">{{ plannerItinerary.overview?.destination || '—' }}</div>
                    </div>
                    <div class="kpi">
                      <div class="kpi-k">天数</div>
                      <div class="kpi-v">{{ plannerItinerary.overview?.days || '—' }}</div>
                    </div>
                    <div class="kpi">
                      <div class="kpi-k">预算</div>
                      <div class="kpi-v">{{ plannerItinerary.overview?.budget || '—' }}</div>
                    </div>
                  </div>
                </div>

                <div class="preview-card preview-card--map">
                  <div class="preview-title">地图 / 热点（占位）</div>
                  <div class="map-skeleton">
                    <div class="map-pin"></div>
                    <div class="map-line"></div>
                    <div class="map-line map-line--2"></div>
                  </div>
                  <div class="map-hint">接入地图服务后可展示路线、景点与餐馆分布。</div>
                </div>

                <div class="preview-card preview-card--wide">
                  <div class="preview-title">每日安排</div>
                  <div class="days">
                    <div v-for="d in (plannerItinerary.daily_plan || [])" :key="d.day" class="day">
                      <div class="day-left">
                        <div class="day-chip">Day {{ d.day }}</div>
                        <div class="day-name">{{ d.title }}</div>
                      </div>
                      <div class="day-right">{{ (d.activities || []).length }} 项活动</div>
                    </div>
                  </div>
                </div>

                <div class="preview-card">
                  <div class="preview-title">预算拆分</div>
                  <div class="budget">
                    <div v-for="b in (plannerItinerary.budget_breakdown || [])" :key="b.category" class="budget-row">
                      <span class="budget-cat">{{ b.category }}</span>
                      <span class="budget-amt">¥ {{ b.amount }}</span>
                    </div>
                  </div>
                </div>

                <div class="preview-card">
                  <div class="preview-title">行前清单</div>
                  <div class="packing">
                    <span v-for="item in (plannerItinerary.packing_list || []).slice(0, 10)" :key="item" class="pack-item">{{ item }}</span>
                  </div>
                </div>
              </div>

              <div class="drawer-footer">
                <button class="drawer-btn drawer-btn--secondary" type="button" @click="applyItineraryToResult(plannerItinerary)">
                  打开完整结果页
                </button>
              </div>
            </div>

            <div v-else class="drawer-empty">
              <div class="empty-title">输入需求，马上看到 AI 的“即时回复”</div>
              <div class="empty-desc">我们会先解析你输入的关键信息，再生成行程预览（无 AI Key 也有模板兜底）。</div>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      form: { start: '南京', dest: '北京', days: 5, budget: '5000', date: '', travelers: 1 },
      loading: false,
      loadingProgress: 0,
      isDark: false,
      menuOpen: false,
      errors: { start: '', dest: '', days: '', budget: '' },
      aiPrompt: '',
      selectedPrefs: [],
      prefOptions: [
        { key: '美食', icon: '🍜', label: '美食' },
        { key: '拍照', icon: '📸', label: '拍照' },
        { key: '亲子', icon: '👨‍👩‍👧', label: '亲子' },
        { key: '户外', icon: '🏔️', label: '户外' },
        { key: '文化', icon: '🏛️', label: '文化' },
        { key: '购物', icon: '🛍️', label: '购物' },
        { key: '放松', icon: '🧘', label: '放松' },
        { key: '冒险', icon: '🧗', label: '冒险' },
      ],
      quickExamples: [
        {
          id: 'tokyo-5d',
          text: '帮我规划 5 天东京自由行，预算适中，喜欢美食和二次元',
          payload: { start: '上海', dest: '东京', days: 5, budget: '8000-12000' }
        },
        {
          id: 'sea-7d',
          text: '从上海出发，推荐 7 天东南亚海岛度假',
          payload: { start: '上海', dest: '巴厘岛', days: 7, budget: '12000-18000' }
        }
      ],
      testimonials: [
        {
          id: 't1',
          name: '小棠',
          initials: 'XT',
          meta: '上海 · 美食党',
          rating: 5,
          quote: '输入偏好后行程结构很清晰，预算拆分也合理，省了我做表格的时间。',
          tags: ['东京', '美食', '自由行'],
          avatarBg: 'linear-gradient(135deg, rgba(16,185,129,.55), rgba(59,130,246,.55))'
        },
        {
          id: 't2',
          name: '阿杰',
          initials: 'AJ',
          meta: '成都 · 周末短途',
          rating: 5,
          quote: '一键生成清单很实用，像充电宝/防晒/交通卡这种细节都会提醒到。',
          tags: ['周末游', '清单', '省心'],
          avatarBg: 'linear-gradient(135deg, rgba(59,130,246,.55), rgba(139,92,246,.55))'
        },
        {
          id: 't3',
          name: 'Lina',
          initials: 'LN',
          meta: '杭州 · 亲子出行',
          rating: 4,
          quote: '路线节奏安排得比较舒服，孩子不太累；没有 AI Key 也能用模板先跑通流程。',
          tags: ['亲子', '节奏', '模板兜底'],
          avatarBg: 'linear-gradient(135deg, rgba(245,158,11,.55), rgba(16,185,129,.55))'
        }
      ],

      // demo + planner
      demoLoading: true,
      demoItinerary: null,
      plannerOpen: false,
      plannerItinerary: null,
      plannerError: '',

      // history
      historyItems: [],
      historyTotal: 0,
      historyLoading: false,
      historyDetail: null,
      historyDetailOpen: false,
      historyDetailLoading: false
    }
  },
  mounted() {
    const savedTheme = localStorage.getItem('theme')
    this.isDark = savedTheme ? savedTheme === 'dark' : false
    this.applyTheme()
    this.loadDemo()
    this.loadHistory()
  },
  methods: {
    toggleTheme() {
      this.isDark = !this.isDark
      this.applyTheme()
      localStorage.setItem('theme', this.isDark ? 'dark' : 'light')
    },
    applyTheme() {
      if (this.isDark) { document.documentElement.classList.add('dark-mode') }
      else { document.documentElement.classList.remove('dark-mode') }
    },
    validateForm() {
      let isValid = true
      this.errors = { start: '', dest: '', days: '', budget: '' }
      if (!this.form.start || !this.form.start.trim()) { this.errors.start = '请输入出发地'; isValid = false }
      if (!this.form.dest || !this.form.dest.trim()) { this.errors.dest = '请输入目的地'; isValid = false }
      if (!this.form.days) { this.errors.days = '请输入天数'; isValid = false }
      else if (this.form.days < 1) { this.errors.days = '至少1天'; isValid = false }
      else if (this.form.days > 30) { this.errors.days = '最多30天'; isValid = false }
      if (!this.form.budget || !this.form.budget.trim()) { this.errors.budget = '请输入预算'; isValid = false }
      else if (!/^\d+(-\d+)?(\+)?$/.test(this.form.budget.replace(/,/g, ''))) { this.errors.budget = '格式如: 5000-8000'; isValid = false }
      return isValid
    },
    togglePref(key) {
      const idx = this.selectedPrefs.indexOf(key)
      if (idx >= 0) this.selectedPrefs.splice(idx, 1)
      else this.selectedPrefs.push(key)
    },
    applyExample(ex) {
      if (!ex) return
      if (this.loading) return
      if (ex.payload) this.form = { ...this.form, ...ex.payload }
      if (ex.text) this.aiPrompt = ex.text
      // bring the form into view for mobile users
      try { window.scrollTo({ top: 0, behavior: 'smooth' }) } catch (_) {}
      // trigger planning immediately for better "it works" feedback
      this.$nextTick(() => this.sendPrompt())
    },
    openPlanner() {
      this.plannerOpen = true
      this.plannerError = ''
    },
    closePlanner() {
      this.plannerOpen = false
      this.plannerError = ''
    },
    openPlannerWithDemo() {
      this.openPlanner()
      if (!this.aiPrompt.trim()) this.useDemoPrompt()
      if (!this.plannerItinerary && this.demoItinerary) this.plannerItinerary = this.demoItinerary
    },
    useDemoPrompt() {
      this.aiPrompt = '帮我规划 5 天东京自由行，预算适中，喜欢美食和二次元'
    },
    parsePromptToPayload(prompt) {
      const text = (prompt || '').trim()
      const payload = { ...this.form }

      // days: "5天"
      const daysMatch = text.match(/(\d+)\s*天/)
      if (daysMatch) payload.days = Math.min(30, Math.max(1, parseInt(daysMatch[1], 10)))

      // start: "从上海出发"
      const startMatch = text.match(/从([^，,。\s]{1,10})出发/)
      if (startMatch) payload.start = startMatch[1]

      // destination (prefer explicit patterns to avoid误抓“天东京”):
      // 1) "5天东京..." / "5 天 东京..."
      const dayCityMatch = text.match(/(\d+)\s*天\s*([^\s，,。]{2,12})/)
      // 2) "去东京" / "到东京" / "前往东京" / "去东京玩"
      const verbCityMatch =
        text.match(/(?:前往|去|到|到达|飞往|玩|游玩)([^，,。\s]{2,12})/)

      const destCandidate = (dayCityMatch && dayCityMatch[2]) || (verbCityMatch && verbCityMatch[1])
      if (destCandidate) payload.dest = destCandidate.replace(/^天/, '').trim()

      // budget hints
      if (/预算适中/.test(text)) payload.budget = payload.budget || '8000-12000'
      const budgetMatch = text.match(/预算[^0-9]*(\d+(?:-\d+)?\+?)/)
      if (budgetMatch) payload.budget = budgetMatch[1]

      return payload
    },
    async sendPrompt() {
      if (!this.aiPrompt.trim()) return
      this.openPlanner()
      const payload = this.parsePromptToPayload(this.aiPrompt)
      this.plannerError = ''
      this.plannerItinerary = null
      try {
        this.loading = true
        const res = await axios.post('/api/plan', {
          start: payload.start,
          dest: payload.dest,
          days: parseInt(payload.days),
          budget: String(payload.budget),
          date: payload.date || '',
          travelers: parseInt(payload.travelers) || 1,
          preferences: this.selectedPrefs
        })
        this.plannerItinerary = res.data
      } catch (e) {
        console.error('生成行程失败:', e)
        this.plannerError = '生成失败：请检查后端是否启动，或稍后重试（无 AI Key 也应有模板兜底）。'
      } finally {
        this.loading = false
      }
    },
    applyItineraryToResult(data) {
      if (!data) return
      const encoded = btoa(unescape(encodeURIComponent(JSON.stringify(data))))
      this.$router.push({ name: 'Result', query: { d: encoded } })
      this.closePlanner()
    },
    async loadDemo() {
      try {
        this.demoLoading = true
        // fixed demo: 5 days Tokyo, mid budget
        const res = await axios.post('/api/plan', { start: '上海', dest: '东京', days: 5, budget: '8000-12000' })
        this.demoItinerary = res.data
      } catch (e) {
        console.error('加载示例行程失败:', e)
        this.demoItinerary = null
      } finally {
        this.demoLoading = false
      }
    },
    async loadHistory() {
      try {
        this.historyLoading = true
        const res = await axios.get('/api/history', { params: { limit: 12 } })
        this.historyItems = res.data.items || []
        this.historyTotal = res.data.total || 0
      } catch (e) {
        console.error('加载历史行程失败:', e)
      } finally {
        this.historyLoading = false
      }
    },
    async openHistoryDetail(id) {
      try {
        this.historyDetailOpen = true
        this.historyDetailLoading = true
        this.historyDetail = null
        const res = await axios.get(`/api/itinerary/${id}`)
        this.historyDetail = res.data
      } catch (e) {
        console.error('加载行程详情失败:', e)
      } finally {
        this.historyDetailLoading = false
      }
    },
    formatDate(iso) {
      if (!iso) return ''
      const d = new Date(iso)
      const pad = (n) => String(n).padStart(2, '0')
      return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`
    },
    startPlanning() {
      if (!this.validateForm()) return
      // Instead of navigating immediately, open planner and show preview first
      // Use a parse-friendly template: “去{dest}玩{days}天”
      this.aiPrompt = this.aiPrompt.trim() || `从${this.form.start}出发，去${this.form.dest}玩${this.form.days}天，预算${this.form.budget}`
      this.sendPrompt()
    }
  }
}
</script>

<style scoped>
:root {
  --bg-primary: #ffffff;
  --bg-secondary: #ffffff;
  --bg-nav: rgba(255, 255, 255, 0.95);
  --bg-card: rgba(255, 255, 255, 0.95);
  --text-primary: #1e293b;
  --text-secondary: #64748b;
  --border-color: rgba(226, 232, 240, 0.8);
  --shadow-color: rgba(0, 0, 0, 0.05);
  --primary-color: #10B981;
  --secondary-color: #3B82F6;
}
html.dark-mode {
  --bg-primary: #020617;
  --bg-secondary: #0f172a;
  --bg-nav: rgba(15, 23, 42, 0.95);
  --bg-card: rgba(30, 41, 59, 0.98);
  --text-primary: #ffffff;
  --text-secondary: #e2e8f0;
  --border-color: rgba(255, 255, 255, 0.15);
  --shadow-color: rgba(0, 0, 0, 0.3);
  --primary-color: #60a5fa;
  --secondary-color: #a78bfa;
}
.home-container { min-height: 100vh; background: var(--bg-primary); }

/* 导航栏 */
.nav-bar {
  position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
  display: flex; align-items: center; justify-content: space-between;
  padding: 1rem 2rem;
  /* Home hero is dark → use dark glass nav for cohesion */
  background: rgba(2, 6, 23, 0.40);
  backdrop-filter: blur(22px) saturate(1.15);
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
  box-shadow: 0 10px 40px rgba(2, 6, 23, 0.25);
}
.nav-brand { display: flex; align-items: center; gap: 0.75rem; }
.brand-icon {
  width: 40px; height: 40px;
  background: linear-gradient(135deg, #10B981, #059669);
  border-radius: 12px; display: flex; align-items: center; justify-content: center;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}
.icon-svg { width: 24px; height: 24px; color: white; }
.brand-text-link { text-decoration: none; }
.brand-text { font-size: 1.5rem; font-weight: 700; color: var(--text-primary); letter-spacing: -0.5px; }
.nav-bar .brand-text { color: rgba(255, 255, 255, 0.92); }
.brand-highlight { background: linear-gradient(135deg, #10B981, #3B82F6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.brand-slogan {
  margin-left: 0.75rem;
  padding-left: 0.75rem;
  border-left: 1px solid rgba(255, 255, 255, 0.14);
  color: rgba(226, 232, 240, 0.78);
  font-size: 0.85rem;
  font-weight: 650;
  letter-spacing: 0.02em;
  white-space: nowrap;
}

.nav-links { display: flex; gap: 2rem; }
.nav-link {
  font-size: 0.95rem; font-weight: 600; color: rgba(226, 232, 240, 0.80);
  text-decoration: none; transition: color 0.3s; position: relative;
}
.nav-link:hover, .nav-link.router-link-exact-active { color: rgba(167, 243, 208, 0.95); }
.nav-link::after {
  content: ''; position: absolute; bottom: -4px; left: 0; width: 0; height: 2px;
  background: linear-gradient(90deg, #10B981, #3B82F6); transition: width 0.3s;
}
.nav-link:hover::after, .nav-link.router-link-exact-active::after { width: 100%; }

.nav-actions { display: flex; gap: 0.75rem; }
.btn { padding: 0.6rem 1.25rem; border-radius: 9999px; font-size: 0.9rem; font-weight: 600; cursor: pointer; transition: all 0.3s; border: none; }
.btn-outline { background: rgba(255,255,255,0.06); border: 1.5px solid rgba(255,255,255,0.16); color: rgba(226, 232, 240, 0.88); }
.btn-outline:hover { border-color: rgba(167, 243, 208, 0.55); color: rgba(167, 243, 208, 0.95); background: rgba(16, 185, 129, 0.10); }
.theme-toggle { padding: 0.6rem; min-width: auto; border-radius: 50%; display: flex; align-items: center; justify-content: center; }
.theme-toggle svg { width: 20px; height: 20px; }
.btn-primary { background: linear-gradient(135deg, #10B981, #059669); color: white; box-shadow: 0 4px 14px rgba(16, 185, 129, 0.35); }
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(16, 185, 129, 0.45); }

/* Hero */
.hero-section {
  position: relative; min-height: 100vh; display: flex; align-items: center;
  justify-content: center; padding-top: 80px; overflow: hidden;
}
.hero-bg { position: absolute; inset: 0; z-index: 0; }
.hero-media {
  position: absolute;
  inset: -4%;
  z-index: 0;
  /* High-tech sailboat hero (pure CSS + inline SVG). */
  background:
    radial-gradient(circle at 18% 18%, rgba(16, 185, 129, 0.30), transparent 58%),
    radial-gradient(circle at 82% 20%, rgba(59, 130, 246, 0.30), transparent 56%),
    radial-gradient(circle at 50% 80%, rgba(99, 102, 241, 0.22), transparent 60%),
    linear-gradient(180deg, #030712 0%, #07162e 35%, #020617 100%);
  filter: saturate(1.08) contrast(1.08);
  transform: translate3d(0, 0, 0) scale(1.03);
  will-change: transform;
  animation: heroFloat 18s ease-in-out infinite;
}
.hero-media::before {
  /* Star trails layer */
  content: "";
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 25% 35%, rgba(255,255,255,0.75) 0 1px, transparent 2px),
    radial-gradient(circle at 70% 30%, rgba(255,255,255,0.65) 0 1px, transparent 2px),
    radial-gradient(circle at 50% 55%, rgba(255,255,255,0.55) 0 1px, transparent 2px),
    repeating-linear-gradient(110deg,
      rgba(255,255,255,0.00) 0px,
      rgba(255,255,255,0.00) 46px,
      rgba(147, 197, 253, 0.10) 47px,
      rgba(147, 197, 253, 0.00) 52px);
  opacity: 0.45;
  mix-blend-mode: screen;
  transform: translate3d(-4%, -2%, 0);
  animation: starDrift 22s linear infinite;
  pointer-events: none;
}
.hero-media::after {
  /* City-light reflections layer + readability (no sailboat) */
  content: "";
  position: absolute;
  inset: 0;
  background:
    /* city light reflections on water */
    repeating-linear-gradient(90deg,
      rgba(16,185,129,0.00) 0px,
      rgba(16,185,129,0.00) 28px,
      rgba(16,185,129,0.08) 30px,
      rgba(59,130,246,0.00) 46px),
    linear-gradient(180deg, rgba(2, 6, 23, 0.40) 0%, rgba(2, 6, 23, 0.18) 42%, rgba(2, 6, 23, 0.72) 100%),
    radial-gradient(circle at 50% 36%, rgba(2, 6, 23, 0.25), transparent 60%);
  background-repeat: repeat, no-repeat, no-repeat;
  background-size: 160% 70%, 100% 100%, 100% 100%;
  background-position: 50% 78%, 50% 0%, 50% 0%;
  animation: reflectionSweep 10s ease-in-out infinite;
  pointer-events: none;
}
.hero-gradient {
  position: absolute;
  inset: 0;
  z-index: 1;
  background: linear-gradient(135deg, rgba(236, 253, 245, 0.35) 0%, rgba(219, 234, 254, 0.25) 30%, rgba(237, 233, 254, 0.22) 60%, rgba(252, 231, 243, 0.18) 100%);
  mix-blend-mode: overlay;
}
html.dark-mode .hero-gradient {
  background: linear-gradient(135deg, rgba(15, 23, 42, 0.55) 0%, rgba(30, 41, 59, 0.45) 50%, rgba(51, 65, 85, 0.35) 100%);
  mix-blend-mode: normal;
}
.hero-content { position: relative; z-index: 10; text-align: center; max-width: 900px; padding: 0 2rem; }
.hero-title {
  font-size: clamp(3.5rem, 8vw, 5.5rem);
  font-weight: 760;
  color: rgba(255, 255, 255, 0.92);
  margin-bottom: 1.5rem; letter-spacing: -1.5px; font-family: 'Georgia', serif; line-height: 1.1;
  text-shadow:
    0 10px 40px rgba(2, 6, 23, 0.55),
    0 0 22px rgba(59, 130, 246, 0.18),
    0 0 18px rgba(16, 185, 129, 0.16);
}
html.dark-mode .hero-title { color: #fff; text-shadow: 0 4px 12px rgba(0,0,0,0.7); }
.gradient-text { background: linear-gradient(135deg, #a7f3d0, #93c5fd); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
html.dark-mode .gradient-text { background: linear-gradient(135deg, #6ee7b7, #60a5fa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.hero-subtitle {
  font-size: clamp(1.1rem, 2.4vw, 1.45rem);
  font-weight: 650;
  color: rgba(226, 232, 240, 0.86);
  margin-bottom: 3rem;
  opacity: 0.95;
  font-family: 'Georgia', serif;
  text-shadow: 0 8px 26px rgba(2, 6, 23, 0.55);
}
html.dark-mode .hero-subtitle { color: rgba(255, 255, 255, 0.90); text-shadow: 0 4px 18px rgba(0,0,0,0.75); }

.hero-value-prop {
  font-size: 0.95rem;
  color: rgba(148, 163, 184, 0.82);
  margin-top: -1.5rem;
  margin-bottom: 3rem;
  letter-spacing: 0.06em;
}
html.dark-mode .hero-value-prop { color: rgba(148, 163, 184, 0.75); }

@keyframes heroFloat {
  0% { transform: translate3d(-1.5%, -1%, 0) scale(1.04); }
  50% { transform: translate3d(1.5%, 1%, 0) scale(1.08); }
  100% { transform: translate3d(-1.5%, -1%, 0) scale(1.04); }
}
@keyframes starDrift {
  0% { transform: translate3d(-6%, -4%, 0); opacity: 0.55; }
  50% { transform: translate3d(6%, 2%, 0); opacity: 0.70; }
  100% { transform: translate3d(-6%, -4%, 0); opacity: 0.55; }
}
@keyframes reflectionSweep {
  0% { background-position: 40% 78%, 50% 0%, 50% 0%; filter: brightness(1.00); }
  50% { background-position: 60% 78%, 50% 0%, 50% 0%; filter: brightness(1.06); }
  100% { background-position: 40% 78%, 50% 0%, 50% 0%; filter: brightness(1.00); }
}
@media (prefers-reduced-motion: reduce) {
  .hero-media { animation: none; transform: none; }
  .hero-media::before, .hero-media::after { animation: none; }
}

/* 表单 */
.search-card {
  padding: 1.5rem 2rem; border-radius: 2rem; max-width: 850px; margin: 0 auto;
  background: rgba(2, 6, 23, 0.45);
  backdrop-filter: blur(22px) saturate(1.15);
  border: 1px solid rgba(255, 255, 255, 0.14);
  box-shadow: 0 18px 58px rgba(2, 6, 23, 0.35);
}
.hero-section .field-label { color: rgba(226, 232, 240, 0.78); }
.hero-section .field-input { color: rgba(255, 255, 255, 0.92); text-shadow: none; }
.hero-section .field-input::placeholder { color: rgba(226, 232, 240, 0.55); }
.search-fields { display: flex; align-items: stretch; gap: 0; margin-bottom: 1.25rem; }
.field-group { flex: 1; padding: 0 1rem; text-align: left; }
.field-group:first-child { padding-left: 0; }
.field-group:last-child { padding-right: 0; }
.field-label { display: block; font-size: 0.65rem; font-weight: 700; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 0.5rem; }
.field-input-wrapper { display: flex; align-items: center; gap: 0.5rem; }
.field-icon { width: 18px; height: 18px; flex-shrink: 0; }
.text-emerald { color: #10B981; } .text-blue { color: #3B82F6; } .text-purple { color: #8B5CF6; } .text-amber { color: #F59E0B; }
html.dark-mode .text-emerald { color: #6ee7b7; } html.dark-mode .text-blue { color: #60a5fa; } html.dark-mode .text-purple { color: #a78bfa; } html.dark-mode .text-amber { color: #fbbf24; }
.field-input { width: 100%; border: none; background: transparent; font-size: 1rem; font-weight: 500; color: var(--text-primary); padding: 0.25rem 0; outline: none; }
.field-input::placeholder { color: var(--text-secondary); }
.field-input.error { border-bottom: 2px solid #ef4444; }
.error-message { font-size: 0.75rem; color: #ef4444; margin-top: 0.25rem; text-align: left; }
.field-divider { width: 1px; background: linear-gradient(to bottom, transparent, var(--border-color), transparent); align-self: stretch; }
.hero-section .field-divider { background: linear-gradient(to bottom, transparent, rgba(255,255,255,0.18), transparent); }
.search-btn {
  width: 100%; padding: 1rem 2rem;
  background: linear-gradient(135deg, #10B981, #059669); color: white; border: none; border-radius: 9999px;
  font-size: 1.1rem; font-weight: 600; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 0.5rem;
  box-shadow: 0 4px 16px rgba(16, 185, 129, 0.35); transition: all 0.3s;
}
.search-btn:hover:not(:disabled) { transform: translateY(-2px); box-shadow: 0 6px 24px rgba(16, 185, 129, 0.45); }
.search-btn:disabled { opacity: 0.7; cursor: not-allowed; }
.btn-icon { width: 20px; height: 20px; transition: transform 0.3s; }
.btn-icon.rotating { animation: spin 1s linear infinite; }
@keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

.quick-examples {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  margin-top: 0.9rem;
  justify-content: center;
}
.example-chip {
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  max-width: 100%;
  padding: 0.55rem 0.85rem;
  border-radius: 9999px;
  border: 1px solid rgba(255, 255, 255, 0.14);
  background: rgba(2, 6, 23, 0.28);
  backdrop-filter: blur(16px) saturate(1.1);
  color: rgba(226, 232, 240, 0.86);
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
  box-shadow: 0 14px 45px rgba(2, 6, 23, 0.25);
  text-align: left;
}
.example-chip:hover { transform: translateY(-2px) scale(1.01); background: rgba(2, 6, 23, 0.34); box-shadow: 0 18px 55px rgba(2, 6, 23, 0.30); }
.example-chip:active { transform: translateY(0px) scale(0.99); }
.chip-ai {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.22), rgba(59, 130, 246, 0.18));
  color: rgba(167, 243, 208, 0.95);
}
.chip-ai svg { width: 16px; height: 16px; }
.chip-text {
  font-size: 0.85rem;
  line-height: 1.25;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
/* keep same in dark-mode (already dark glass) */

.pref-section {
  margin-bottom: 1rem; text-align: center;
}
.pref-label {
  display: block; font-size: 0.8rem; color: rgba(148, 163, 184, 0.65);
  margin-bottom: 0.5rem; letter-spacing: 0.05em;
}
.pref-chips {
  display: flex; flex-wrap: wrap; gap: 0.45rem; justify-content: center;
}
.pref-chip {
  display: inline-flex; align-items: center; gap: 0.3rem;
  padding: 0.35rem 0.75rem; border-radius: 9999px;
  border: 1px solid rgba(255, 255, 255, 0.12);
  background: rgba(2, 6, 23, 0.24);
  color: rgba(203, 213, 225, 0.8); font-size: 0.82rem;
  cursor: pointer; transition: all 0.2s ease;
}
.pref-chip:hover { border-color: rgba(16, 185, 129, 0.4); transform: translateY(-1px); }
.pref-chip.active {
  background: linear-gradient(135deg, #10B981, #059669);
  color: #fff; border-color: transparent;
  box-shadow: 0 2px 12px rgba(16, 185, 129, 0.35);
}
.pref-chip-icon { font-size: 0.85rem; }

/* AI entry */
.ai-entry {
  margin: 1.2rem auto 0;
  max-width: 850px;
  text-align: left;
}
.ai-entry-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: 0.55rem;
}
.ai-entry-title {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  color: rgba(255, 255, 255, 0.92);
  font-weight: 750;
  text-shadow: 0 4px 18px rgba(2, 6, 23, 0.55);
}
.ai-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.25rem 0.55rem;
  border-radius: 9999px;
  background: rgba(255, 255, 255, 0.18);
  border: 1px solid rgba(255, 255, 255, 0.28);
  backdrop-filter: blur(12px);
  font-weight: 900;
  letter-spacing: 0.06em;
}
.ai-pill-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: radial-gradient(circle at 30% 30%, #a7f3d0, #10B981);
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.18);
}
.ai-entry-cta {
  border: none;
  background: transparent;
  color: rgba(255, 255, 255, 0.90);
  font-weight: 700;
  cursor: pointer;
  text-decoration: underline;
  text-underline-offset: 3px;
}
.ai-entry-box {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 0.9rem;
  padding: 1rem 1rem 1rem 1.1rem;
  border-radius: 1.6rem;
  background: rgba(2, 6, 23, 0.42);
  border: 1px solid rgba(255, 255, 255, 0.14);
  backdrop-filter: blur(20px) saturate(1.12);
  box-shadow: 0 18px 60px rgba(2, 6, 23, 0.14);
}
.ai-textarea {
  width: 100%;
  border: none;
  outline: none;
  resize: none;
  background: transparent;
  color: rgba(226, 232, 240, 0.92);
  font-size: 1rem;
  line-height: 1.55;
}
.ai-textarea::placeholder { color: rgba(226, 232, 240, 0.55); }
.ai-send {
  align-self: end;
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  padding: 0.75rem 1rem;
  border-radius: 9999px;
  border: none;
  cursor: pointer;
  background: linear-gradient(135deg, #10B981, #059669);
  color: rgba(255, 255, 255, 0.96);
  font-weight: 800;
  box-shadow: 0 12px 40px rgba(16, 185, 129, 0.32);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.ai-send svg { width: 18px; height: 18px; }
.ai-send:hover:not(:disabled) { transform: translateY(-2px); box-shadow: 0 18px 55px rgba(16, 185, 129, 0.40); }
.ai-send:disabled { opacity: 0.6; cursor: not-allowed; }
.ai-entry-hint { margin-top: 0.55rem; color: rgba(255, 255, 255, 0.82); font-size: 0.88rem; text-shadow: 0 4px 18px rgba(2, 6, 23, 0.55); }
/* same for dark-mode */

/* 功能卡片 */
.features-section { padding: 6rem 2rem; max-width: 1200px; margin: 0 auto; }
.section-head { display: flex; align-items: baseline; justify-content: flex-start; margin-bottom: 1.75rem; }
.section-title { font-size: 2.2rem; font-weight: 800; letter-spacing: -0.02em; margin: 0; color: #111827; }
.features-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 2rem; }
.feature-card {
  border-radius: 1.5rem; text-align: left; text-decoration: none; color: inherit;
  transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
  background: rgba(255, 255, 255, 0.78);
  border: 1px solid rgba(255, 255, 255, 0.35);
  box-shadow: 0 18px 55px rgba(2, 6, 23, 0.10);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}
.feature-card:hover { transform: translateY(-8px) scale(1.015); box-shadow: 0 26px 70px rgba(2, 6, 23, 0.16); }
.feature-card:active { transform: translateY(-2px) scale(1.005); }
.feature-card--image .feature-body { padding: 1.65rem 1.8rem 2rem; }
.feature-media { position: relative; height: 190px; }
.media-img {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  transform: scale(1.03);
  transition: transform 0.4s ease;
}
.feature-card:hover .media-img { transform: scale(1.10); }
.media-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(2, 6, 23, 0.05) 0%, rgba(2, 6, 23, 0.35) 75%, rgba(2, 6, 23, 0.55) 100%);
}
.media-img--inspiration {
  background-image: url("https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1600&q=70");
}
.media-img--guide {
  background-image: url("https://images.unsplash.com/photo-1529692236671-f1f6cf9683ba?auto=format&fit=crop&w=1600&q=70");
}
.media-img--community {
  background-image: url("https://images.unsplash.com/photo-1520975916090-3105956dac38?auto=format&fit=crop&w=1600&q=70");
}
.ai-badge {
  position: absolute;
  top: 14px;
  right: 14px;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.35rem 0.55rem;
  border-radius: 9999px;
  background: rgba(255, 255, 255, 0.22);
  border: 1px solid rgba(255, 255, 255, 0.32);
  backdrop-filter: blur(10px);
  color: rgba(255, 255, 255, 0.92);
}
.ai-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: radial-gradient(circle at 30% 30%, #a7f3d0, #10B981);
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.20);
}
.ai-badge--blue .ai-dot { background: radial-gradient(circle at 30% 30%, #bfdbfe, #3B82F6); box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.20); }
.ai-badge--purple .ai-dot { background: radial-gradient(circle at 30% 30%, #ddd6fe, #8B5CF6); box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.20); }
.ai-text { font-size: 0.78rem; font-weight: 800; letter-spacing: 0.08em; }

.feature-body { display: flex; flex-direction: column; gap: 0.9rem; }
.feature-top { display: flex; align-items: center; gap: 0.75rem; }
.feature-icon { width: 56px; height: 56px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; }
.feature-icon svg { width: 28px; height: 28px; color: white; }
.bg-emerald-light { background: linear-gradient(135deg, var(--primary-color), #34D399); }
.bg-blue-light { background: linear-gradient(135deg, var(--secondary-color), #60A5FA); }
.bg-purple-light { background: linear-gradient(135deg, #8B5CF6, #A78BFA); }
.feature-title { font-size: 1.5rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.75rem; }
.feature-desc { font-size: 0.95rem; color: var(--text-secondary); line-height: 1.7; margin-bottom: 1.5rem; }
.feature-btn-text { color: var(--primary-color); font-weight: 600; font-size: 0.9rem; }
html.dark-mode .feature-card {
  background: rgba(15, 23, 42, 0.64);
  border: 1px solid rgba(255, 255, 255, 0.12);
  box-shadow: 0 26px 80px rgba(0, 0, 0, 0.40);
}
html.dark-mode .media-overlay {
  background: linear-gradient(180deg, rgba(2, 6, 23, 0.10) 0%, rgba(2, 6, 23, 0.55) 75%, rgba(2, 6, 23, 0.72) 100%);
}

/* Social proof */
.social-proof {
  padding: 2.5rem 2rem 6rem;
  max-width: 1200px;
  margin: 0 auto;
}
.social-proof-inner {
  border-radius: 2rem;
  padding: 2.5rem;
  background: rgba(255, 255, 255, 0.55);
  border: 1px solid rgba(255, 255, 255, 0.35);
  backdrop-filter: blur(22px) saturate(1.15);
  box-shadow: 0 26px 85px rgba(2, 6, 23, 0.10);
}
html.dark-mode .social-proof-inner {
  background: rgba(15, 23, 42, 0.55);
  border: 1px solid rgba(255, 255, 255, 0.12);
  box-shadow: 0 28px 90px rgba(0, 0, 0, 0.45);
}
.proof-header { text-align: left; margin-bottom: 1.5rem; }
.proof-title { font-size: 1.9rem; margin: 0 0 0.35rem; color: var(--text-primary); }
.proof-subtitle { margin: 0; color: var(--text-secondary); font-size: 0.98rem; }

.testimonials { display: none; }

.testimonials-marquee { margin-top: 1.2rem; }
.testimonials-marquee--second { margin-top: 0.9rem; opacity: 0.98; }
.marquee-viewport {
  position: relative;
  overflow: hidden;
  border-radius: 1.6rem;
  padding: 0.25rem;
  -webkit-mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent);
  mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent);
}
.marquee-viewport::before,
.marquee-viewport::after {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  width: 80px;
  pointer-events: none;
  z-index: 2;
}
.marquee-viewport::before { left: 0; background: linear-gradient(90deg, rgba(255,255,255,0.98), rgba(255,255,255,0)); }
.marquee-viewport::after { right: 0; background: linear-gradient(270deg, rgba(255,255,255,0.98), rgba(255,255,255,0)); }
html.dark-mode .marquee-viewport::before { background: linear-gradient(90deg, rgba(2,6,23,0.92), rgba(2,6,23,0)); }
html.dark-mode .marquee-viewport::after { background: linear-gradient(270deg, rgba(2,6,23,0.92), rgba(2,6,23,0)); }

.marquee-track {
  display: flex;
  gap: 1.25rem;
  width: max-content;
  padding: 0.5rem 0.5rem;
  animation: testimonials-marquee 28s linear infinite;
  will-change: transform;
}
.marquee-viewport:hover .marquee-track { animation-play-state: paused; }

@keyframes testimonials-marquee {
  from { transform: translateX(0); }
  to { transform: translateX(-50%); }
}

.marquee-track--reverse {
  animation-duration: 32s;
  animation-direction: reverse;
}

.marquee-track .testimonial-card {
  width: 360px;
  flex: 0 0 auto;
}
.testimonial-card {
  padding: 1.2rem 1.2rem 1.1rem;
  border-radius: 1.4rem;
  background: rgba(255, 255, 255, 0.68);
  border: 1px solid rgba(255, 255, 255, 0.35);
  box-shadow: 0 16px 55px rgba(2, 6, 23, 0.10);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.testimonial-card:hover { transform: translateY(-6px); box-shadow: 0 24px 75px rgba(2, 6, 23, 0.14); }
html.dark-mode .testimonial-card {
  background: rgba(2, 6, 23, 0.20);
  border: 1px solid rgba(255, 255, 255, 0.12);
  box-shadow: 0 22px 78px rgba(0, 0, 0, 0.42);
}
.t-top { display: flex; align-items: center; gap: 0.85rem; }
.avatar {
  width: 44px;
  height: 44px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(255, 255, 255, 0.95);
  box-shadow: 0 10px 30px rgba(2, 6, 23, 0.18);
}
.avatar-text { font-weight: 900; letter-spacing: 0.02em; }
.t-meta { display: flex; flex-direction: column; gap: 0.1rem; min-width: 0; }
.t-name { font-weight: 850; color: var(--text-primary); }
.t-sub { font-size: 0.85rem; color: var(--text-secondary); }
.t-rating { margin-left: auto; display: inline-flex; gap: 2px; }
.star { font-size: 0.85rem; color: rgba(148, 163, 184, 0.7); }
.star.on { color: #fbbf24; text-shadow: 0 6px 16px rgba(251,191,36,0.35); }
.t-quote { margin: 0.9rem 0 0.85rem; color: var(--text-primary); line-height: 1.65; font-size: 0.95rem; }
.t-tags { display: flex; flex-wrap: wrap; gap: 0.45rem; }
.tag {
  font-size: 0.78rem;
  padding: 0.25rem 0.55rem;
  border-radius: 9999px;
  background: rgba(16, 185, 129, 0.10);
  border: 1px solid rgba(16, 185, 129, 0.18);
  color: rgba(16, 185, 129, 0.95);
}
html.dark-mode .tag {
  background: rgba(16, 185, 129, 0.16);
  border: 1px solid rgba(16, 185, 129, 0.22);
  color: rgba(167, 243, 208, 0.95);
}

/* Demo */
.demo-section {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem 6rem;
}
.demo-inner {
  border-radius: 2rem;
  padding: 2.5rem;
  background: rgba(255, 255, 255, 0.62);
  border: 1px solid rgba(255, 255, 255, 0.35);
  backdrop-filter: blur(22px) saturate(1.15);
  box-shadow: 0 26px 85px rgba(2, 6, 23, 0.10);
}
html.dark-mode .demo-inner {
  background: rgba(15, 23, 42, 0.58);
  border: 1px solid rgba(255, 255, 255, 0.12);
  box-shadow: 0 28px 90px rgba(0, 0, 0, 0.45);
}
.demo-head { display: flex; flex-wrap: wrap; align-items: baseline; gap: 1rem; justify-content: space-between; }
.demo-title { margin: 0; color: var(--text-primary); font-size: 1.9rem; }
.demo-subtitle { margin: 0; color: var(--text-secondary); }
.demo-open { border: none; background: transparent; cursor: pointer; color: var(--primary-color); font-weight: 800; text-decoration: underline; text-underline-offset: 3px; }
.demo-loading { margin-top: 1.4rem; color: var(--text-secondary); }
.demo-grid { margin-top: 1.4rem; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1rem; }
.demo-card {
  border-radius: 1.5rem;
  padding: 1.2rem 1.25rem;
  background: rgba(255, 255, 255, 0.70);
  border: 1px solid rgba(255, 255, 255, 0.35);
  box-shadow: 0 16px 55px rgba(2, 6, 23, 0.10);
}
html.dark-mode .demo-card { background: rgba(2, 6, 23, 0.20); border: 1px solid rgba(255, 255, 255, 0.12); box-shadow: 0 22px 78px rgba(0, 0, 0, 0.42); }
.demo-card--wide { grid-column: span 2; }
.demo-kpi { display: flex; justify-content: space-between; align-items: baseline; padding: 0.5rem 0; border-bottom: 1px solid rgba(148, 163, 184, 0.22); }
.demo-kpi:last-child { border-bottom: none; }
.kpi-label { color: var(--text-secondary); font-size: 0.85rem; font-weight: 750; }
.kpi-value { color: var(--text-primary); font-size: 1.05rem; font-weight: 900; }
.demo-list-title { font-weight: 900; color: var(--text-primary); margin-bottom: 0.7rem; }
.demo-days { display: grid; gap: 0.65rem; }
.demo-day { display: flex; align-items: center; gap: 0.75rem; }
.day-badge { font-size: 0.78rem; font-weight: 900; color: rgba(16,185,129,0.95); background: rgba(16,185,129,0.12); border: 1px solid rgba(16,185,129,0.20); padding: 0.25rem 0.55rem; border-radius: 9999px; }
.day-title { color: var(--text-primary); font-weight: 800; }
.demo-budget { display: grid; gap: 0.45rem; }
.budget-row { display: flex; justify-content: space-between; color: var(--text-primary); }
.budget-cat { color: var(--text-secondary); font-weight: 750; }
.budget-amt { font-weight: 900; }
.demo-pack { display: flex; flex-wrap: wrap; gap: 0.45rem; }
.demo-pack-item {
  font-size: 0.82rem;
  padding: 0.25rem 0.55rem;
  border-radius: 9999px;
  background: rgba(99, 102, 241, 0.10);
  border: 1px solid rgba(99, 102, 241, 0.18);
  color: rgba(99, 102, 241, 0.95);
}
html.dark-mode .demo-pack-item {
  background: rgba(99, 102, 241, 0.14);
  border: 1px solid rgba(99, 102, 241, 0.22);
  color: rgba(199, 210, 254, 0.92);
}
.demo-pack-hint { margin-top: 0.6rem; color: var(--text-secondary); font-size: 0.86rem; line-height: 1.4; }

/* Drawer planner */
.drawer-backdrop {
  position: fixed;
  inset: 0;
  z-index: 10000;
  background: rgba(2, 6, 23, 0.55);
  backdrop-filter: blur(6px);
  display: flex;
  justify-content: flex-end;
}
.drawer {
  width: min(560px, 92vw);
  height: 100%;
  background: rgba(255, 255, 255, 0.85);
  border-left: 1px solid rgba(255, 255, 255, 0.35);
  backdrop-filter: blur(18px) saturate(1.1);
  display: flex;
  flex-direction: column;
}
html.dark-mode .drawer { background: rgba(2, 6, 23, 0.86); border-left: 1px solid rgba(255, 255, 255, 0.12); }
.drawer-head {
  padding: 1rem 1.1rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid rgba(148, 163, 184, 0.18);
}
.drawer-title { display: inline-flex; align-items: center; gap: 0.6rem; color: var(--text-primary); font-weight: 950; }
.drawer-ai { font-weight: 900; letter-spacing: 0.08em; padding: 0.2rem 0.5rem; border-radius: 9999px; background: rgba(16,185,129,0.12); border: 1px solid rgba(16,185,129,0.22); color: rgba(16,185,129,0.98); }
.drawer-close { border: none; background: transparent; cursor: pointer; font-size: 1.2rem; color: var(--text-secondary); }
.drawer-body { padding: 1rem 1.1rem 1.2rem; overflow: auto; }
.drawer-input { border-radius: 1.4rem; padding: 0.9rem; background: rgba(255, 255, 255, 0.65); border: 1px solid rgba(255, 255, 255, 0.35); box-shadow: 0 16px 55px rgba(2,6,23,0.10); }
html.dark-mode .drawer-input { background: rgba(15, 23, 42, 0.55); border: 1px solid rgba(255, 255, 255, 0.12); box-shadow: 0 22px 78px rgba(0,0,0,0.42); }
.drawer-textarea { width: 100%; border: none; outline: none; resize: none; background: transparent; color: var(--text-primary); font-size: 1rem; line-height: 1.55; }
.drawer-textarea::placeholder { color: var(--text-secondary); }
.drawer-actions { display: flex; gap: 0.7rem; justify-content: flex-end; margin-top: 0.7rem; flex-wrap: wrap; }
.drawer-btn { border: none; cursor: pointer; border-radius: 9999px; padding: 0.7rem 1rem; font-weight: 900; }
.drawer-btn--primary { background: linear-gradient(135deg, #10B981, #059669); color: rgba(255,255,255,0.96); box-shadow: 0 14px 45px rgba(16,185,129,0.30); }
.drawer-btn--secondary { background: rgba(148, 163, 184, 0.18); color: var(--text-primary); }
html.dark-mode .drawer-btn--secondary { background: rgba(148, 163, 184, 0.14); }
.drawer-btn:disabled { opacity: 0.6; cursor: not-allowed; }
.drawer-error { margin-top: 0.9rem; padding: 0.9rem 1rem; border-radius: 1.2rem; background: rgba(239, 68, 68, 0.10); border: 1px solid rgba(239, 68, 68, 0.22); color: rgba(239, 68, 68, 0.95); font-weight: 750; }
.drawer-empty { margin-top: 1.2rem; padding: 1.1rem 1rem; border-radius: 1.4rem; border: 1px dashed rgba(148, 163, 184, 0.35); color: var(--text-secondary); }
.empty-title { font-weight: 950; color: var(--text-primary); margin-bottom: 0.3rem; }
.empty-desc { line-height: 1.6; }
.drawer-preview { margin-top: 1.1rem; }
.preview-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0.9rem; }
.preview-card {
  border-radius: 1.4rem;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.70);
  border: 1px solid rgba(255, 255, 255, 0.35);
  box-shadow: 0 16px 55px rgba(2, 6, 23, 0.10);
}
html.dark-mode .preview-card { background: rgba(15, 23, 42, 0.55); border: 1px solid rgba(255, 255, 255, 0.12); box-shadow: 0 22px 78px rgba(0,0,0,0.42); }
.preview-card--wide { grid-column: span 2; }
.preview-card--map { grid-column: span 2; }
.preview-title { font-weight: 950; color: var(--text-primary); margin-bottom: 0.6rem; }
.preview-kpis { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.6rem; }
.kpi { border-radius: 1rem; padding: 0.7rem; background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.16); }
html.dark-mode .kpi { background: rgba(16,185,129,0.12); border: 1px solid rgba(16,185,129,0.18); }
.kpi-k { color: var(--text-secondary); font-weight: 800; font-size: 0.78rem; }
.kpi-v { color: var(--text-primary); font-weight: 950; margin-top: 0.1rem; }
.days { display: grid; gap: 0.55rem; }
.day { display: flex; justify-content: space-between; align-items: center; padding: 0.65rem 0.7rem; border-radius: 1.1rem; background: rgba(148,163,184,0.10); border: 1px solid rgba(148,163,184,0.18); }
.day-left { display: flex; align-items: center; gap: 0.65rem; }
.day-chip { font-size: 0.78rem; font-weight: 950; color: rgba(59,130,246,0.95); background: rgba(59,130,246,0.10); border: 1px solid rgba(59,130,246,0.18); padding: 0.22rem 0.55rem; border-radius: 9999px; }
.day-name { font-weight: 900; color: var(--text-primary); }
.day-right { color: var(--text-secondary); font-weight: 750; font-size: 0.86rem; }
.packing { display: flex; flex-wrap: wrap; gap: 0.45rem; }
.pack-item { font-size: 0.82rem; padding: 0.25rem 0.55rem; border-radius: 9999px; background: rgba(99,102,241,0.10); border: 1px solid rgba(99,102,241,0.18); color: rgba(99,102,241,0.95); }
html.dark-mode .pack-item { background: rgba(99,102,241,0.14); border: 1px solid rgba(99,102,241,0.22); color: rgba(199,210,254,0.92); }
.map-skeleton { height: 140px; border-radius: 1.2rem; background: linear-gradient(135deg, rgba(59,130,246,0.10), rgba(16,185,129,0.10)); border: 1px solid rgba(148,163,184,0.22); position: relative; overflow: hidden; }
.map-pin { position: absolute; left: 18%; top: 40%; width: 14px; height: 14px; border-radius: 50%; background: rgba(16,185,129,0.95); box-shadow: 0 0 0 10px rgba(16,185,129,0.16); }
.map-line { position: absolute; left: 24%; top: 44%; width: 55%; height: 10px; border-radius: 9999px; background: rgba(59,130,246,0.22); }
.map-line--2 { top: 62%; width: 70%; left: 14%; background: rgba(99,102,241,0.18); }
.map-hint { margin-top: 0.55rem; color: var(--text-secondary); font-size: 0.88rem; line-height: 1.4; }
.drawer-footer { margin-top: 0.9rem; display: flex; justify-content: flex-end; }

.drawer-enter-active, .drawer-leave-active { transition: opacity 0.2s ease; }
.drawer-enter-from, .drawer-leave-to { opacity: 0; }
.drawer-enter-active .drawer, .drawer-leave-active .drawer { transition: transform 0.25s ease; }
.drawer-enter-from .drawer { transform: translateX(24px); }
.drawer-leave-to .drawer { transform: translateX(24px); }

/* 加载 */
.loading-overlay {
  position: fixed; inset: 0; z-index: 9999;
  background: var(--bg-nav); backdrop-filter: blur(10px);
  display: flex; align-items: center; justify-content: center;
}
.loading-content { text-align: center; }
.loading-spinner { position: relative; width: 120px; height: 120px; margin: 0 auto 2rem; }
.spinner-ring { position: absolute; inset: 0; border: 4px solid var(--border-color); border-top-color: #10B981; border-radius: 50%; animation: spin 1s linear infinite; }
.spinner-icon { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; color: #10B981; animation: pulse 2s ease-in-out infinite; }
.spinner-icon svg { width: 48px; height: 48px; }
@keyframes pulse { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.7; transform: scale(0.95); } }
.loading-title { font-size: 1.75rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.75rem; font-family: 'Georgia', serif; }
.loading-text { font-size: 1rem; color: var(--text-secondary); margin-bottom: 2rem; }
.loading-progress { width: 300px; height: 4px; background: var(--border-color); border-radius: 2px; overflow: hidden; margin: 0 auto; }
.progress-bar { height: 100%; background: linear-gradient(90deg, #10B981, #3B82F6); border-radius: 2px; transition: width 0.3s; }
.fade-enter-active, .fade-leave-active { transition: opacity 0.3s; }
.fade-enter-from, .fade-leave-to { opacity: 0; }

/* 历史行程 */
.history-section {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem 5rem;
}
.history-inner {
  border-radius: 2rem;
  padding: 2.5rem;
  background: rgba(255, 255, 255, 0.62);
  border: 1px solid rgba(255, 255, 255, 0.35);
  backdrop-filter: blur(22px) saturate(1.15);
  box-shadow: 0 26px 85px rgba(2, 6, 23, 0.10);
}
html.dark-mode .history-inner {
  background: rgba(15, 23, 42, 0.58);
  border: 1px solid rgba(255, 255, 255, 0.12);
  box-shadow: 0 28px 90px rgba(0, 0, 0, 0.45);
}
.history-count {
  font-size: 0.9rem;
  color: var(--text-secondary);
  margin-left: auto;
}
.history-loading, .history-empty {
  margin-top: 1.2rem;
  color: var(--text-secondary);
}
.history-scroll {
  margin-top: 1.2rem;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 1rem;
}
.history-card {
  padding: 1.15rem 1.1rem;
  border-radius: 1.35rem;
  background: rgba(255, 255, 255, 0.72);
  border: 1px solid rgba(255, 255, 255, 0.35);
  box-shadow: 0 14px 45px rgba(2, 6, 23, 0.08);
  cursor: pointer;
  transition: transform 0.22s ease, box-shadow 0.22s ease;
}
.history-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 22px 70px rgba(2, 6, 23, 0.14);
}
html.dark-mode .history-card {
  background: rgba(2, 6, 23, 0.22);
  border: 1px solid rgba(255, 255, 255, 0.12);
  box-shadow: 0 20px 70px rgba(0, 0, 0, 0.42);
}
.h-card-top {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 0.7rem;
}
.h-dest {
  font-size: 1.25rem;
  font-weight: 850;
  color: var(--text-primary);
}
.h-date {
  font-size: 0.78rem;
  color: var(--text-secondary);
  font-weight: 600;
}
.h-card-body {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}
.h-stat {
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
}
.h-label {
  font-size: 0.68rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-secondary);
  font-weight: 750;
}
.h-val {
  font-weight: 800;
  color: var(--text-primary);
}

/* History detail modal */
.history-detail-backdrop {
  position: fixed;
  inset: 0;
  z-index: 11000;
  background: rgba(2, 6, 23, 0.55);
  backdrop-filter: blur(6px);
  display: flex;
  align-items: center;
  justify-content: center;
}
.history-detail {
  width: min(640px, 94vw);
  max-height: 85vh;
  overflow-y: auto;
  border-radius: 1.8rem;
  background: rgba(255, 255, 255, 0.92);
  border: 1px solid rgba(255, 255, 255, 0.35);
  backdrop-filter: blur(18px) saturate(1.1);
  box-shadow: 0 28px 90px rgba(2, 6, 23, 0.25);
}
html.dark-mode .history-detail {
  background: rgba(15, 23, 42, 0.94);
  border: 1px solid rgba(255, 255, 255, 0.12);
}
.hd-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.2rem 1.4rem;
  border-bottom: 1px solid rgba(148, 163, 184, 0.20);
}
.hd-title {
  margin: 0;
  font-size: 1.2rem;
  font-weight: 850;
  color: var(--text-primary);
}
.hd-close {
  border: none;
  background: transparent;
  cursor: pointer;
  font-size: 1.2rem;
  color: var(--text-secondary);
}
.hd-loading {
  padding: 2rem 1.4rem;
  color: var(--text-secondary);
}
.hd-body {
  padding: 1.2rem 1.4rem 1.6rem;
}
.hd-kpis {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0.7rem;
  margin-bottom: 1.2rem;
}
.hd-kpi {
  border-radius: 1rem;
  padding: 0.7rem;
  background: rgba(16, 185, 129, 0.08);
  border: 1px solid rgba(16, 185, 129, 0.16);
  text-align: center;
}
.hd-kpi-label {
  display: block;
  font-size: 0.68rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-secondary);
  font-weight: 750;
  margin-bottom: 0.2rem;
}
.hd-kpi-val {
  font-weight: 900;
  color: var(--text-primary);
}
.hd-block {
  margin-bottom: 1.1rem;
}
.hd-block-title {
  font-weight: 900;
  color: var(--text-primary);
  margin-bottom: 0.55rem;
}
.hd-overview-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.5rem;
}
.hd-ov-item {
  display: flex;
  justify-content: space-between;
  padding: 0.5rem 0.65rem;
  border-radius: 0.8rem;
  background: rgba(148, 163, 184, 0.10);
}
.hd-ov-label {
  color: var(--text-secondary);
  font-weight: 700;
}
.hd-ov-val {
  font-weight: 800;
  color: var(--text-primary);
}
.hd-days {
  display: grid;
  gap: 0.55rem;
}
.hd-day {
  padding: 0.65rem 0.7rem;
  border-radius: 1.1rem;
  background: rgba(148, 163, 184, 0.10);
  border: 1px solid rgba(148, 163, 184, 0.18);
}
.hd-day-head {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  margin-bottom: 0.5rem;
}
.hd-day-badge {
  font-size: 0.78rem;
  font-weight: 950;
  color: rgba(59, 130, 246, 0.95);
  background: rgba(59, 130, 246, 0.10);
  border: 1px solid rgba(59, 130, 246, 0.18);
  padding: 0.2rem 0.55rem;
  border-radius: 9999px;
}
.hd-day-name {
  font-weight: 900;
  color: var(--text-primary);
}
.hd-acts {
  display: grid;
  gap: 0.35rem;
}
.hd-act {
  display: flex;
  gap: 0.7rem;
  padding: 0.35rem 0.55rem;
  border-radius: 0.65rem;
  background: rgba(148, 163, 184, 0.06);
}
.hd-act-time {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--text-secondary);
  white-space: nowrap;
}
.hd-act-title {
  font-size: 0.88rem;
  color: var(--text-primary);
}
.hd-budget {
  display: grid;
  gap: 0.45rem;
}
.hd-budget-row {
  display: flex;
  justify-content: space-between;
  color: var(--text-primary);
  font-weight: 700;
}
.hd-budget-amt {
  font-weight: 900;
}
.hd-pack {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}
.hd-pack-item {
  font-size: 0.82rem;
  padding: 0.25rem 0.55rem;
  border-radius: 9999px;
  background: rgba(99, 102, 241, 0.10);
  border: 1px solid rgba(99, 102, 241, 0.18);
  color: rgba(99, 102, 241, 0.95);
}
html.dark-mode .hd-pack-item {
  background: rgba(99, 102, 241, 0.14);
  border: 1px solid rgba(99, 102, 241, 0.22);
  color: rgba(199, 210, 254, 0.92);
}

@media (max-width: 768px) {
  .history-section { padding: 0 1rem 4rem; }
  .history-inner { padding: 1.5rem; }
  .history-scroll { grid-template-columns: 1fr; }
  .hd-kpis { grid-template-columns: repeat(2, 1fr); }
  .hd-overview-grid { grid-template-columns: 1fr; }
}

/* 底部 */
.footer { background: var(--bg-secondary); padding: 4rem 2rem 2rem; border-top: 1px solid var(--border-color); }
.footer-content { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 3fr; gap: 4rem; align-items: start; }
.footer-brand { display: flex; flex-direction: column; gap: 1rem; }
.brand-header { display: flex; align-items: center; gap: 1rem; }
.brand-desc { color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6; max-width: 300px; }
.footer-links { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; }
.link-group { display: flex; flex-direction: column; gap: 1rem; }
.link-title { font-size: 1.1rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.5rem; }
.footer-link { color: var(--text-secondary); text-decoration: none; font-size: 0.95rem; transition: all 0.3s; display: block; }
.footer-link:hover { color: var(--primary-color); transform: translateX(4px); }
.footer-trust {
  max-width: 1200px; margin: 2.5rem auto 0;
  display: flex; justify-content: center; gap: 3rem; flex-wrap: wrap;
}
.trust-item {
  display: flex; align-items: center; gap: 0.5rem;
  color: var(--text-secondary); font-size: 0.85rem;
}
.trust-item svg { width: 18px; height: 18px; opacity: 0.55; }

.footer-bottom { max-width: 1200px; margin: 1.5rem auto 0; padding-top: 1.5rem; border-top: 1px solid var(--border-color); text-align: center; }
.copyright { color: var(--text-secondary); font-size: 0.9rem; }

@media (max-width: 768px) {
  .nav-links { display: none; }
  .desktop-only { display: none; }
  .hamburger { display: flex; }
  .mobile-menu { display: flex; flex-direction: column; padding: 1rem 1.5rem; background: var(--bg-nav); backdrop-filter: blur(20px); border-top: 1px solid var(--border-color); }
  .mobile-link { padding: 0.8rem 0; font-size: 1rem; font-weight: 500; color: var(--text-primary); text-decoration: none; border-bottom: 1px solid var(--border-color); }
  .mobile-link:hover { color: var(--primary-color); }
  .mobile-cta { margin-top: 1rem; width: 100%; justify-content: center; }
  .menu-enter-active, .menu-leave-active { transition: all 0.3s ease; max-height: 400px; overflow: hidden; }
  .menu-enter-from, .menu-leave-to { max-height: 0; opacity: 0; }
  .search-fields { flex-direction: column; gap: 1rem; }
  .field-divider { display: none; }
  .field-group { padding: 0; }
  .features-section { padding: 4rem 1rem; }
  .section-head { margin-bottom: 1.25rem; }
  .section-title { font-size: 1.8rem; }
  .features-grid { grid-template-columns: 1fr; gap: 1.25rem; }
  .feature-media { height: 170px; }
  .ai-entry { margin-top: 1rem; }
  .ai-entry-box { grid-template-columns: 1fr; }
  .ai-send { width: 100%; justify-content: center; }
  .social-proof { padding: 1.75rem 1rem 4rem; }
  .social-proof-inner { padding: 1.5rem; }
  .marquee-viewport { -webkit-mask-image: none; mask-image: none; }
  .marquee-track { animation-duration: 34s; }
  .marquee-track .testimonial-card { width: 290px; }
  .demo-section { padding: 0 1rem 4rem; }
  .demo-inner { padding: 1.5rem; }
  .demo-grid { grid-template-columns: 1fr; }
  .demo-card--wide { grid-column: span 1; }
  .drawer { width: 100vw; }
  .preview-grid { grid-template-columns: 1fr; }
  .preview-card--wide, .preview-card--map { grid-column: span 1; }
  .footer-content { grid-template-columns: 1fr; gap: 2rem; }
  .footer-links { grid-template-columns: repeat(2, 1fr); gap: 1.5rem; }
  .chip-text { white-space: normal; }
}

@media (prefers-reduced-motion: reduce) {
  .marquee-track { animation: none; transform: none; }
  .marquee-viewport { overflow-x: auto; }
}
.hamburger { display: none; flex-direction: column; gap: 5px; padding: 0.5rem; cursor: pointer; background: none; border: none; }
.hamburger span { display: block; width: 22px; height: 2px; background: var(--text-primary); border-radius: 2px; transition: all 0.3s; }
.hamburger.active span:nth-child(1) { transform: rotate(45deg) translate(5px, 5px); }
.hamburger.active span:nth-child(2) { opacity: 0; }
.hamburger.active span:nth-child(3) { transform: rotate(-45deg) translate(5px, -5px); }
.mobile-menu { display: none; }
</style>
