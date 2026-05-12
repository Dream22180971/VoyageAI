# VoyageAI - 智能旅行规划系统

<p align="center">
  <strong>AI 驱动的智能旅行规划，让每一次出发都充满期待</strong><br>
  <a href="https://voyageai.seanwalter.top/">在线体验</a> · Vue 3 + FastAPI + DeepSeek
</p>


<img width="1910" height="911" alt="image" src="https://github.com/user-attachments/assets/01199332-3089-43ee-a543-7c0c37db3b57" />
<img width="1910" height="904" alt="image" src="https://github.com/user-attachments/assets/957a7d06-f853-471d-9f52-bcef4dc2c3a1" />
<img width="1910" height="908" alt="image" src="https://github.com/user-attachments/assets/a3ad3d10-7b1c-4bb8-b59b-30491cdfee87" />

<img width="1910" height="912" alt="image" src="https://github.com/user-attachments/assets/7f9add7d-f668-4d1e-8c4e-183003332de5" />

---

## ✨ 功能亮点

- 🤖 **AI 智能行程生成** — 基于 DeepSeek 大模型，深度理解用户需求，生成个性化行程方案
- 🌤️ **实时天气预警** — 集成高德地图天气 API，提供目的地实时天气及出行建议
- 💰 **智能预算分析** — 自动拆分交通、住宿、餐饮、门票费用，Canvas 图表可视化
- ✅ **智能行前清单** — 根据目的地气候和行程特点，自动生成个性化打包清单
- 📝 **导出 MD / JSON** — 一键导出可读文档与结构化数据，稳定不易出错
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
- **TTL 内存缓存** — 行程/天气结果缓存，避免重复 API 调用

### 前端
- **Vue 3** — 组合式 API，现代化前端框架
- **Vue Router** — 单页应用路由（6 个页面）
- **Vite** — 极速构建工具
- **Axios** — HTTP 请求
- **ECharts** — Canvas 预算图表
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
│   ├── cache.py             # TTL 内存缓存模块
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
| GET | `/api/history?skip=0&limit=20` | 历史行程列表 |
| GET | `/api/itinerary/{id}` | 行程详情 |
| POST | `/api/plan` | 生成行程（需 `{start, dest, days, budget}`） |

## 🔒 安全设计

- API 密钥通过 `.env` 管理，不入 Git
- URL 参数 Base64 编码，避免数据明文暴露
- Pydantic 严格输入验证
- CORS 白名单配置
- 自签名 HTTPS 证书

## 📝 更新日志

- **2026-05-13** — 出发日期+出行人数字段、8个偏好标签chip、ECharts甘特图时间轴(卡片/时间轴切换)、高德地图打点、天气出行建议、多轮对话修改行程、一键复制微信/小红书格式
- **2026-05-12** — 新增行程历史查询（列表+详情）让数据库从"只写"变读写闭环；实现 TTL 内存缓存层，相同行程/天气请求 18ms 命中不再重复调 AI；API Key 安全加固（.env 600 权限 + .env.example 模板）；修复 HTTPS 443 端口 fallback 到博客问题
- **2026-04-29** — 结果页新增"交通/耗时/用餐推荐/备选方案/预约提示"等更可执行的活动细节；目的地字段清洗避免"北京玩5天"类脏数据；无 AI Key 时兜底行程更真实并支持"日本→东京"等归一化；首页"用户声音"双行滚动卡片与快捷提示词一键生成；导出改为 MD/JSON 并移除 PDF
- **2026-04-29** — 首页新增 AI 输入区与侧边规划器预览（含 5 天游示例），增强"即时交互"体验；统一各页面导航与 Hero 视觉风格；后端 `httpx` 禁用环境代理，修复本地 `socks4` 代理导致的 `/api/plan` 失败
- **2026-04-01** — 新增灵感发现、目的地指南、社区足迹、关于我们 4 个页面；统一双主题商务风格；移动端汉堡菜单；PDF 导出；5 城市定制行程；Logo 更新为飞机图标；URL 数据加密

## 📄 许可证

MIT License
