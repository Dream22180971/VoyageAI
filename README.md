# VoyageAI - 智能旅行规划系统

<p align="center">
  <strong>AI 驱动的智能旅行规划，让每一次出发都充满期待</strong><br>
  <a href="https://47.103.214.75">在线体验</a> · Vue 3 + FastAPI + DeepSeek
</p>

---

## ✨ 功能亮点

- 🤖 **AI 智能行程生成** — 基于 DeepSeek 大模型，深度理解用户需求，生成个性化行程方案
- 🌤️ **实时天气预警** — 集成高德地图天气 API，提供目的地实时天气及出行建议
- 💰 **智能预算分析** — 自动拆分交通、住宿、餐饮、门票费用，Canvas 图表可视化
- ✅ **智能行前清单** — 根据目的地气候和行程特点，自动生成个性化打包清单
- 📄 **PDF 导出** — 一键导出精美 PDF 行程文件
- 🌙 **深色模式** — 浅色/深色双主题切换，主题偏好自动保存
- 📱 **移动端适配** — 响应式设计 + 汉堡菜单，手机浏览体验流畅
- 🏙️ **目的地定制化** — 北京、上海、成都、西安、杭州等热门城市拥有专属行程数据

## 📱 页面导航

| 页面 | 路由 | 功能 |
|------|------|------|
| 首页 | `/` | 行程规划表单、功能入口卡片 |
| 灵感发现 | `/inspiration` | 热门目的地、主题旅行、最佳出行时间 |
| 目的地指南 | `/guide` | 成都/大理/西安/厦门详细攻略，含搜索功能 |
| 社区足迹 | `/community` | 旅行故事、活跃排行、热门话题 |
| 结果页 | `/result` | AI 生成的行程详情、天气、预算、清单 |
| 关于我们 | `/about` | 项目介绍、核心功能、技术栈 |

## 🛠️ 技术栈

### 后端
- **FastAPI** — 高性能异步 Python Web 框架
- **DeepSeek API** — AI 行程生成引擎
- **高德地图 API** — 实时天气数据（地理编码 + 天气查询）
- **SQLAlchemy** — ORM 数据库管理
- **SQLite** — 轻量级数据存储

### 前端
- **Vue 3** — 组合式 API，现代化前端框架
- **Vue Router** — 单页应用路由（6 个页面）
- **Vite** — 极速构建工具
- **Axios** — HTTP 请求
- **ECharts** — Canvas 预算图表
- **html2canvas + jsPDF** — PDF 导出
- **CSS Variables** — 浅色/深色双主题系统

### 部署
- **Nginx** — 反向代理 + 静态文件服务 + HTTPS
- **Systemd** — 后端进程管理
- **宝塔面板** — 服务器管理面板
- **SCP + SSH** — 自动化部署脚本

## 📁 项目结构

```
VoyageAI/
├── backend/
│   ├── main.py              # FastAPI 主应用（含 AI 调用、天气、5 城市定制数据）
│   ├── config.py            # 配置管理
│   ├── database.py          # 数据库连接
│   ├── models.py            # SQLAlchemy 数据模型
│   ├── requirements.txt     # Python 依赖
│   └── .env                 # 环境变量（API Key，不入 Git）
├── frontend/
│   ├── src/
│   │   ├── views/
│   │   │   ├── Home.vue         # 首页（表单 + 功能卡片）
│   │   │   ├── Inspiration.vue  # 灵感发现
│   │   │   ├── Guide.vue        # 目的地指南
│   │   │   ├── Community.vue    # 社区足迹
│   │   │   ├── About.vue        # 关于我们
│   │   │   └── Result.vue       # 结果页（行程+天气+预算+清单+PDF）
│   │   ├── router/index.js      # 路由配置（6 页面）
│   │   ├── App.vue
│   │   ├── main.js
│   │   └── style.css
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── deploy.sh                    # 一键部署脚本
├── .gitignore
├── README.md
├── 产品需求文档.md
└── 技术架构文档.md
```

## 🚀 快速开始

### 后端

```bash
cd backend
pip install -r requirements.txt
# 配置 .env
python main.py          # http://localhost:8000
```

### 前端

```bash
cd frontend
npm install
npm run dev            # http://localhost:5173
npm run build          # 生产构建 → dist/
```

## 🔌 API 接口

| 方法 | 路径 | 描述 |
|------|------|------|
| GET | `/` | 服务状态 |
| GET | `/api/health` | 健康检查 |
| GET | `/api/config` | 配置信息 |
| GET | `/api/weather?city=北京` | 实时天气 |
| POST | `/api/plan` | 生成行程（需 `{start, dest, days, budget}`） |

## 🔒 安全设计

- API 密钥通过 `.env` 管理，不入 Git
- URL 参数 Base64 编码，避免数据明文暴露
- Pydantic 严格输入验证
- CORS 白名单配置
- 自签名 HTTPS 证书

## 📝 更新日志

- **2026-04-29** — 首页新增 AI 输入区与侧边规划器预览（含 5 天游示例），增强“即时交互”体验；统一各页面导航与 Hero 视觉风格；后端 `httpx` 禁用环境代理，修复本地 `socks4` 代理导致的 `/api/plan` 失败
- **2026-04-01** — 新增灵感发现、目的地指南、社区足迹、关于我们 4 个页面；统一双主题商务风格；移动端汉堡菜单；PDF 导出；5 城市定制行程；Logo 更新为飞机图标；URL 数据加密

## 📄 许可证

MIT License
