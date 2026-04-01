---
name: "dark-mode-implementation"
description: "Implements dark mode support for Vue3 websites with theme toggle, CSS variables, and localStorage persistence. Invoke when users need to add dark mode functionality to their Vue3 applications."
---

# 深色模式实现技能

## 功能说明

这个技能用于为Vue3网站实现深色模式支持，包括主题切换按钮、CSS变量管理和本地存储持久化功能。

## 使用场景

- 当用户需要为网站添加深色模式支持时
- 当网站需要同时适配浅色和深色主题时
- 当需要保存用户的主题偏好设置时

## 实现步骤

### 1. 定义CSS变量

在样式文件中定义浅色和深色模式的CSS变量：

```css
/* CSS变量定义 */
:root {
  /* 浅色模式 */
  --bg-primary: #F8F9FA;
  --bg-secondary: #FFFFFF;
  --bg-nav: rgba(255, 255, 255, 0.8);
  --bg-card: rgba(255, 255, 255, 0.95);
  --bg-overlay: rgba(255, 255, 255, 0.3);
  
  --text-primary: #1e293b;
  --text-secondary: #64748b;
  --text-light: #e2e8f0;
  --text-white: #ffffff;
  
  --border-color: rgba(255, 255, 255, 0.5);
  --shadow-color: rgba(0, 0, 0, 0.05);
  
  --primary-color: #10B981;
  --secondary-color: #3B82F6;
}

/* 深色模式 */
.dark-mode {
  --bg-primary: #0f172a;
  --bg-secondary: #1e293b;
  --bg-nav: rgba(15, 23, 42, 0.85);
  --bg-card: rgba(30, 41, 59, 0.95);
  --bg-overlay: rgba(15, 23, 42, 0.4);
  
  --text-primary: #ffffff;
  --text-secondary: #94a3b8;
  --text-light: #cbd5e1;
  --text-white: #ffffff;
  
  --border-color: rgba(255, 255, 255, 0.1);
  --shadow-color: rgba(0, 0, 0, 0.2);
  
  --primary-color: #10B981;
  --secondary-color: #3B82F6;
}
```

### 2. 更新现有样式

将所有硬编码的颜色替换为CSS变量：

```css
.home-container {
  background: var(--bg-primary);
}

.nav-bar {
  background: var(--bg-nav);
  border-bottom: 1px solid var(--border-color);
  box-shadow: 0 4px 20px var(--shadow-color);
}

.brand-text {
  color: var(--text-primary);
}

.nav-link {
  color: var(--text-secondary);
}
```

### 3. 添加主题切换按钮

在导航栏中添加主题切换按钮：

```vue
<button 
  class="btn btn-outline theme-toggle"
  @click="toggleTheme"
  title="切换主题"
>
  <svg v-if="!isDark" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
  </svg>
  <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/>
  </svg>
</button>
```

### 4. 添加主题切换逻辑

在Vue组件的JavaScript部分添加主题切换逻辑：

```javascript
export default {
  data() {
    return {
      isDark: false
    }
  },
  mounted() {
    // 从localStorage读取主题设置
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
      this.isDark = savedTheme === 'dark';
    } else {
      // 默认浅色模式
      this.isDark = false;
    }
    this.applyTheme();
  },
  methods: {
    toggleTheme() {
      this.isDark = !this.isDark;
      this.applyTheme();
      // 保存到localStorage
      localStorage.setItem('theme', this.isDark ? 'dark' : 'light');
    },
    applyTheme() {
      if (this.isDark) {
        document.documentElement.classList.add('dark-mode');
      } else {
        document.documentElement.classList.remove('dark-mode');
      }
    }
  }
}
```

### 5. 添加按钮样式

为主题切换按钮添加样式：

```css
.theme-toggle {
  padding: 0.6rem;
  min-width: auto;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.theme-toggle svg {
  width: 20px;
  height: 20px;
}
```

## 最佳实践

1. **默认浅色模式**：网站默认使用浅色模式，符合大多数用户习惯
2. **平滑切换**：使用CSS变量实现主题的平滑切换
3. **持久化存储**：使用localStorage保存用户的主题偏好
4. **完整适配**：确保所有组件和样式都适配深色模式
5. **可访问性**：确保在深色模式下文字仍然清晰可读

## 示例实现

完整的主题切换按钮和逻辑示例：

```vue
<template>
  <button 
    class="btn btn-outline theme-toggle"
    @click="toggleTheme"
    title="切换主题"
  >
    <svg v-if="!isDark" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
    </svg>
    <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <path d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/>
    </svg>
  </button>
</template>

<script>
export default {
  data() {
    return {
      isDark: false
    }
  },
  mounted() {
    const savedTheme = localStorage.getItem('theme');
    this.isDark = savedTheme === 'dark';
    this.applyTheme();
  },
  methods: {
    toggleTheme() {
      this.isDark = !this.isDark;
      this.applyTheme();
      localStorage.setItem('theme', this.isDark ? 'dark' : 'light');
    },
    applyTheme() {
      if (this.isDark) {
        document.documentElement.classList.add('dark-mode');
      } else {
        document.documentElement.classList.remove('dark-mode');
      }
    }
  }
}
</script>
```

## 故障排除

- **主题不生效**：检查CSS变量是否正确定义和使用
- **切换按钮不显示**：检查按钮样式和图标是否正确
- **持久化失效**：检查localStorage是否被正确设置和读取
- **部分组件未适配**：确保所有样式都使用CSS变量而不是硬编码颜色