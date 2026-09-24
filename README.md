Plan a complete trip from destination, days and budget with AI. / 输入目的地、天数和预算，让 AI 生成完整旅行攻略。

<!-- README-V2-BILINGUAL -->

# VoyageAI

> **EN:** Plan a complete trip from destination, days and budget with AI.  
> **中文：** 输入目的地、天数和预算，让 AI 生成完整旅行攻略。

## Demo / 演示

[Live Demo / 在线体验](https://voyageai.seanwalter.top/) · Existing screenshots are kept below / 现有截图保留在下方。

## Quick Start / 5 分钟快速开始

```bash
git clone https://github.com/Dream22180971/VoyageAI.git
cd VoyageAI
pip install -r requirements.txt
python main.py
# open another terminal for the frontend
npm install
npm run dev
```

> **EN:** The commands above are intentionally kept short: clone, install, run. Project-specific configuration and advanced usage stay in the detailed documentation below.  
> **中文：** 上面的命令刻意保持最短路径：克隆、安装、运行。项目特定配置与高级用法继续保留在下方详细文档中。

## Why this project / 为什么做这个项目

**EN:** This repository is built around one concrete problem and aims to be understandable, runnable and useful before becoming complex.

**中文：** 这个仓库围绕一个明确问题构建，优先做到易理解、能运行、真正有用，再逐步增加复杂能力。

---

<!-- ORIGINAL-DOCS -->
# VoyageAI - 智能旅行规划

> 告诉 AI 你想去哪、玩几天、预算多少——它帮你生成一份完整的旅行攻略。

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Vue 3](https://img.shields.io/badge/Vue-3-blue?style=flat)](https://vuejs.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat)](https://fastapi.tiangolo.com)
[![DeepSeek](https://img.shields.io/badge/DeepSeek-AI-536DFE?style=flat)](https://deepseek.com)

<p align="center">
  <a href="https://voyageai.seanwalter.top/">在线体验</a>
</p>

<img width="1910" height="911" alt="VoyageAI 首页" src="https://github.com/user-attachments/assets/01199332-3089-43ee-a543-7c0c37db3b57" />
<img width="1910" height="904" alt="行程结果" src="https://github.com/user-attachments/assets/957a7d06-f853-471d-9f52-bcef4dc2c3a1" />
<img width="1910" height="908" alt="目的地指南" src="https://github.com/user-attachments/assets/a3ad3d10-7b1c-4bb8-b59b-30491cdfee87" />
<img width="1910" height="912" alt="灵感发现" src="https://github.com/user-attachments/assets/7f9add7d-f668-4d1e-8c4e-183003332de5" />

---

## 目录

- [它是什么](#它是什么)
- [为什么做](#为什么做)
- [核心功能](#核心功能)
- [页面导航](#页面导航)
- [快速开始](#快速开始)
- [技术架构](#技术架构)
- [API 接口](#api-接口)
- [安全设计](#安全设计)
- [Roadmap](#roadmap)
- [FAQ](#faq)
- [谁适合用](#谁适合用)
- [关于我](#关于我)

---

## 它是什么

一个**AI 旅行规划系统**，帮你做三件事：

1. **生成行程**：输入目的地、天数、预算，AI 自动生成每日行程
2. **实时天气**：自动查目的地天气，给出穿搭和出行建议
3. **预算分析**：自动拆分交通、住宿、餐饮、门票费用，图表可视化

不需要翻攻略、做表格，AI 帮你搞定。

---

## 为什么做

每次出去玩最累的不是旅途本身，而是**出发前做攻略**——翻十几篇小红书笔记、对比酒店价格、算预算、排每天的行程，花两三天才勉强拼出一份攻略。

而且每个人的喜好不同——有人爱美食，有人爱打卡，有人预算紧，通用攻略根本不适用。

这个项目的思路：**告诉 AI 你的需求，它帮你生成个性化行程**。预算紧就推荐经济型，爱吃就多排美食，几天就排几天，比通用攻略靠谱。

---

## 核心功能

| 你能做什么 | 说明 |
|-----------|------|
| **AI 行程生成** | 输入目的地、天数、预算，AI 生成每日行程 |
| **实时天气预警** | 高德地图天气 API，目的地实时天气和出行建议 |
| **智能预算分析** | 自动拆分费用，ECharts 图表可视化 |
| **行前清单** | 根据目的地气候和行程，自动生成打包清单 |
| **导出文档** | 一键导出 Markdown / JSON，方便保存和分享 |
| **深色模式** | 浅色/深色双主题，偏好自动保存 |
| **移动端适配** | 响应式设计 + 汉堡菜单，手机浏览流畅 |
| **5 城市定制** | 北京、上海、成都、西安、杭州有专属行程数据 |

---

## 页面导航

| 页面 | 路由 | 功能 |
|------|------|------|
| 首页 | `/` | 行程规划表单、功能入口卡片 |
| 灵感发现 | `/inspiration` | 热门目的地、主题旅行、最佳出行时间 |
| 目的地指南 | `/guide` | 成都/大理/西安/厦门详细攻略 |
| 社区足迹 | `/community` | 旅行故事、活跃排行、热门话题 |
| 结果页 | `/result` | AI 生成的行程详情、天气、预算、清单 |
| 关于我们 | `/about` | 项目介绍、核心功能、技术栈 |

---

## 快速开始

### 后端

```bash
cd backend
pip install -r requirements.txt
# 配置 .env（填入 DeepSeek API Key 和高德地图 Key）
python main.py          # http://localhost:8000
```

### 前端

```bash
cd frontend
npm install
npm run dev            # http://localhost:5173
```

---

## 技术架构

### 后端
- **FastAPI** — 高性能异步 Python Web 框架
- **DeepSeek API** — AI 行程生成引擎
- **高德地图 API** — 实时天气数据
- **SQLAlchemy + SQLite** — 数据持久化
- **TTL 内存缓存** — 避免重复 API 调用

### 前端
- **Vue 3** — 组合式 API，现代化前端框架
- **Vue Router** — 6 个页面路由
- **ECharts** — Canvas 预算图表
- **CSS Variables** — 浅色/深色双主题

### 部署
- **Nginx** — 反向代理 + HTTPS
- **Systemd** — 后端进程管理
- **宝塔面板** — 服务器管理

---

## API 接口

| 方法 | 路径 | 描述 |
|------|------|------|
| GET | `/api/health` | 健康检查 |
| GET | `/api/weather?city=北京` | 实时天气 |
| GET | `/api/history?skip=0&limit=20` | 历史行程列表 |
| GET | `/api/itinerary/{id}` | 行程详情 |
| POST | `/api/plan` | 生成行程 |

---

## 安全设计

- API 密钥通过 `.env` 管理，不入 Git
- URL 参数 Base64 编码，避免数据明文暴露
- Pydantic 严格输入验证
- CORS 白名单配置
- 自签名 HTTPS 证书

---

## Roadmap

- [x] AI 行程生成（DeepSeek）
- [x] 实时天气预警（高德地图）
- [x] 预算分析 + ECharts 图表
- [x] 5 城市定制行程
- [x] 深色/浅色双主题
- [x] 移动端适配
- [x] 行程历史查询
- [ ] 多轮对话修改行程
- [ ] 微信/小红书一键分享
- [ ] 更多城市定制数据
- [ ] 团队协作规划

---

## FAQ

**Q: 需要什么 API Key？**
A: 需要两个：DeepSeek API Key（AI 生成行程）和高德地图 Key（天气查询）。

**Q: 没有 API Key 能用吗？**
A: 可以体验界面和已有行程数据，但 AI 生成新行程需要 DeepSeek Key。

**Q: 支持哪些城市？**
A: 目前北京、上海、成都、西安、杭州有专属定制数据。其他城市用通用行程模板。

**Q: 数据安全吗？**
A: API Key 存在 `.env` 文件不入 Git，行程数据存在本地 SQLite，不上传任何服务器。

---

## 谁适合用

- **旅行爱好者**：快速生成个性化行程，省掉做攻略的时间
- **Vue 3 + FastAPI 开发者**：前后端分离的完整实战案例
- **想做 AI 应用的人**：DeepSeek + 天气 API 的集成参考
- **独立开发者**：从 0 到 1 上线一个完整产品的参考

---

## 关于我

我是**肖恩沃尔特**（Sean Walter），一个从测试工程师正在转型为 AI 独立开发者的程序员。

VoyageAI 是我做的第一个 AI 驱动的完整产品——从前端到后端，从 AI 集成到部署上线，全流程自己搞定。

- GitHub: [Dream22180971](https://github.com/Dream22180971)
- Twitter/X: [@sean_walter0717](https://x.com/sean_walter0717)
- 博客: [seanwalter.top](https://seanwalter.top)

---

## License

[MIT](./LICENSE)
