# VoyageAI - 智能旅行规划

<p align="center">
  <strong>AI 驱动的智能旅行规划，让每一次出发都充满期待</strong><br>
  <a href="https://voyageai.seanwalter.top/">在线体验</a> · Vue 3 + FastAPI + DeepSeek
</p>

**线上地址**: https://voyageai.seanwalter.top/

<img width="1910" height="911" alt="image" src="https://github.com/user-attachments/assets/01199332-3089-43ee-a543-7c0c37db3b57" />
<img width="1910" height="904" alt="image" src="https://github.com/user-attachments/assets/957a7d06-f853-471d-9f52-bcef4dc2c3a1" />
<img width="1910" height="908" alt="image" src="https://github.com/user-attachments/assets/a3ad3d10-7b1c-4bb8-b59b-30491cdfee87" />
<img width="1910" height="912" alt="image" src="https://github.com/user-attachments/assets/7f9add7d-f668-4d1e-8c4e-183003332de5" />

## 技术栈

| 层 | 技术 |
|---|------|
| 前端 | Vue 3 + Vite + Vue Router + ECharts + 高德地图 |
| 后端 | FastAPI + SQLAlchemy + SQLite |
| AI | DeepSeek API |
| 部署 | Vercel (前端) + 阿里云 ECS (后端) + Nginx 反向代理 |

## 功能

- 自然语言/表单双模式输入（出发地、目的地、天数、预算、日期、人数）
- 8个旅行偏好标签（美食/拍照/亲子/户外/文化/购物/放松/冒险）
- AI 生成结构化行程：每日活动、交通方式、餐饮推荐、预约提示
- ECharts 甘特图时间轴 + 卡片视图切换
- 高德地图打点连线
- 天气出行建议（穿衣/防晒/带伞等）
- 多轮对话修改行程
- 一键复制微信/小红书格式化文本
- 行程历史查询
- TTL 缓存（同参数直接返回）

## 本地开发

```bash
# 后端
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

# 前端
cd frontend
npm install
npm run dev
```

## 部署

```bash
# 后端部署到 ECS
scp -i aliyun-test.pem backend/main.py root@47.103.214.75:/opt/voyageai/backend/
ssh -i aliyun-test.pem root@47.103.214.75 "systemctl restart voyageai"

# 前端部署到 Vercel
cd frontend && npx vercel deploy --prod
```

## 项目结构

```
VoyageAI/
├── backend/
│   ├── main.py          # FastAPI 应用（API端点、AI集成、缓存）
│   ├── models.py         # SQLAlchemy 数据模型
│   └── requirements.txt  # Python 依赖
├── frontend/
│   ├── src/
│   │   ├── views/
│   │   │   ├── Home.vue     # 首页（表单、偏好标签）
│   │   │   └── Result.vue   # 结果页（时间轴、地图、天气、聊天、复制）
│   │   └── router/index.js  # 路由（懒加载）
│   ├── vercel.json          # Vercel 部署配置
│   └── package.json
└── README.md
```

## API 端点

| 端点 | 说明 |
|------|------|
| `POST /api/plan` | 生成行程（含缓存） |
| `POST /api/chat` | 多轮对话修改行程 |
| `GET /api/history` | 历史行程列表 |
| `GET /api/history/:id` | 单个行程详情 |
| `DELETE /api/history/:id` | 删除行程 |
| `GET /api/weather` | 天气出行建议 |
| `GET /api/amap-config` | 高德地图密钥 |
| `GET /api/health` | 健康检查 |

## 变更日志

- **2026.05.12** — 出发日期+人数、偏好标签、甘特图时间轴、高德地图、天气建议、多轮对话、微信/小红书一键复制
- **2026.05.10** — 行程历史查询、TTL 缓存、安全加固
- **2026.05.08** — 行程真实感增强、首页 UX 优化
