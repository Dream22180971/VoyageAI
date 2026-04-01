# VoyageAI - 智能旅行规划系统

VoyageAI 是一个基于 AI 的智能旅行规划系统，使用 FastAPI 作为后端框架，Vue3 作为前端框架，为用户提供个性化的旅行行程规划服务。

## 技术栈

### 后端
- **FastAPI**：现代化的 Python Web 框架，提供高性能的异步 API 服务
- **SQLite/MySQL**：轻量级数据库，用于存储用户和行程数据
- **DeepSeek API**：提供 AI 行程生成功能
- **OpenWeatherMap API**：提供实时天气信息
- **Pydantic**：数据验证和设置管理
- **SQLAlchemy**：ORM 数据库工具

### 前端
- **Vue3**：现代化的前端框架
- **Vue Router**：前端路由管理
- **Axios**：HTTP 客户端，用于 API 调用
- **ECharts**：数据可视化图表
- **Vite**：前端构建工具
- **深色模式支持**：可切换的浅色/深色主题

## 项目结构

```
VoyageAI/
├── backend/            # FastAPI 后端
│   ├── __pycache__/    # Python 缓存文件
│   ├── main.py         # 主应用文件
│   ├── config.py       # 配置文件
│   ├── database.py     # 数据库连接
│   ├── models.py       # 数据库模型
│   ├── requirements.txt # 依赖文件
│   ├── voyageai.db     # SQLite 数据库文件
│   └── .env            # 环境变量
├── frontend/           # Vue3 前端
│   ├── .vscode/        # VS Code 配置
│   ├── public/         # 静态资源
│   │   ├── favicon.svg # 网站图标
│   │   └── icons.svg   # SVG 图标
│   ├── src/
│   │   ├── assets/     # 资源文件
│   │   │   └── hero.png # 首页背景图
│   │   ├── components/ # 组件目录
│   │   │   └── HelloWorld.vue # 示例组件
│   │   ├── views/      # 页面组件
│   │   │   ├── Home.vue    # 首页（行程规划表单）
│   │   │   └── Result.vue  # 结果页（行程详情）
│   │   ├── router/     # 路由配置
│   │   │   └── index.js     # 路由入口
│   │   ├── main.js     # 入口文件
│   │   ├── App.vue     # 根组件
│   │   └── style.css   # 全局样式
│   ├── package.json    # 前端依赖
│   ├── package-lock.json # 依赖锁定文件
│   └── vite.config.js  # Vite 配置
├── oldtest/            # 旧测试代码（保留）
└── README.md           # 项目说明
```

## 功能特性

### 核心功能
1. **智能行程规划**：基于用户输入的出发地、目的地、天数和预算，生成个性化的行程计划
2. **实时天气预警**：集成 OpenWeatherMap API，提供目的地的实时天气信息和预警
3. **预算分析**：智能分析行程预算，提供详细的费用分配
4. **行前清单**：根据行程特点，生成个性化的行前准备清单
5. **行程保存**：将生成的行程保存到数据库，方便后续查看

### 技术特性
1. **异步处理**：使用 FastAPI 的异步特性，提高并发性能
2. **响应式设计**：前端采用响应式布局，适配不同屏幕尺寸
3. **实时加载**：添加加载动画和进度条，提升用户体验
4. **数据可视化**：使用 ECharts 实现预算数据的可视化展示
5. **自动 API 文档**：FastAPI 自动生成 Swagger 文档
6. **深色模式支持**：可切换的浅色/深色主题，提供舒适的阅读体验
7. **主题持久化**：使用 localStorage 保存用户主题偏好设置
8. **现代化 UI**：采用玻璃态设计和渐变色彩，提升视觉体验

## 安装与运行

### 后端安装

1. 进入后端目录
   ```bash
   cd backend
   ```

2. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```

3. 配置环境变量
   编辑 `.env` 文件，填写相关 API 密钥：
   ```
   # DeepSeek API Key
   deepseek_api_key=your_deepseek_api_key_here

   # OpenWeatherMap API Key
   openweather_api_key=your_openweather_api_key_here

   # Database URL
   database_url=sqlite:///./voyageai.db

   # Cache settings
   cache_timeout=300
   ```

4. 启动后端服务
   ```bash
   python main.py
   ```
   服务将运行在 `http://localhost:8000`

### 前端安装

1. 进入前端目录
   ```bash
   cd frontend
   ```

2. 安装依赖
   ```bash
   npm install
   ```

3. 启动前端服务
   ```bash
   npm run dev
   ```
   服务将运行在 `http://localhost:5173`

4. **主题切换**：点击导航栏中的月亮/太阳图标可以切换浅色/深色模式，主题设置会自动保存到浏览器本地存储

## API 接口

### 健康检查
- **URL**: `/api/health`
- **Method**: GET
- **Description**: 检查服务健康状态

### 配置信息
- **URL**: `/api/config`
- **Method**: GET
- **Description**: 获取当前配置信息

### 行程生成
- **URL**: `/api/plan`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "start": "出发地",
    "dest": "目的地",
    "days": 游玩天数,
    "budget": "预算范围"
  }
  ```
- **Response**:
  ```json
  {
    "overview": {
      "destination": "目的地",
      "days": 游玩天数,
      "budget": "预算范围",
      "best_season": "最佳旅行季节",
      "pace": "游玩节奏",
      "highlights_count": 核心体验数量
    },
    "daily_plan": [
      {
        "day": 1,
        "title": "当日主题",
        "activities": [
          {
            "time": "时间段",
            "title": "活动名称",
            "description": "详细描述",
            "icon": "图标"
          }
        ]
      }
    ],
    "budget_breakdown": [
      { "category": "机票/交通", "amount": 金额 },
      { "category": "酒店住宿", "amount": 金额 },
      { "category": "美食餐饮", "amount": 金额 },
      { "category": "门票娱乐", "amount": 金额 }
    ],
    "packing_list": ["物品 1", "物品 2", ...],
    "weather_alert": {
      "city": "城市",
      "temp": "温度",
      "condition": "天气状况",
      "warning": "预警信息"
    }
  }
  ```

## 开发指南

### 后端开发
- 使用 FastAPI 的异步特性，提高并发性能
- 使用 Pydantic 进行数据验证
- 使用 SQLAlchemy 进行数据库操作
- 遵循 RESTful API 设计规范

### 前端开发
- 使用 Vue3 的组合式 API
- 使用 Vue Router 进行路由管理
- 使用 Axios 进行 API 调用
- 使用 ECharts 进行数据可视化
- 使用 CSS 变量实现主题切换功能
- 使用 localStorage 实现主题持久化
- 遵循组件化开发原则
- 采用玻璃态设计和渐变色彩提升视觉体验

## 部署指南

### 后端部署
1. 安装依赖
2. 配置环境变量
3. 启动服务

### 前端部署
1. 构建生产版本
   ```bash
   npm run build
   ```
2. 将 `dist` 目录部署到静态文件服务器

## 注意事项

1. **API 密钥**：需要注册 DeepSeek 和 OpenWeatherMap 账号，获取 API 密钥
2. **数据库**：默认使用 SQLite，可根据需要切换到 MySQL
3. **CORS**：已配置 CORS 中间件，允许跨域请求
4. **缓存**：使用内存缓存，提高 API 响应速度

## 未来规划

1. **用户认证**：添加用户注册、登录功能
2. **行程管理**：实现行程的保存、编辑、删除功能
3. **多语言支持**：添加国际化功能
4. **性能优化**：进一步优化 API 响应速度和前端加载性能
5. **部署优化**：配置 Docker 容器化部署

## 贡献

欢迎提交 Issue 和 Pull Request，共同改进这个项目。

## 许可证

MIT License
