---
name: "background-optimization"
description: "Optimizes background images for websites by matching theme, adjusting overlays, and ensuring text readability. Invoke when users need to update or improve background images to match website style."
---

# 背景图片优化技能

## 功能说明

这个技能用于优化网站背景图片，确保图片与网站主题协调，并保证文字在背景上的可读性。

## 使用场景

- 当用户需要更换背景图片以匹配网站主题时
- 当背景图片与文字颜色不搭配，影响可读性时
- 当需要为特定主题（如赛博朋克、远航等）生成背景图片时

## 优化步骤

### 1. 主题匹配分析

- 分析网站整体风格和品牌定位
- 确定适合的背景主题（如自然风景、城市夜景、抽象图案等）
- 选择与网站色彩方案协调的图片

### 2. 图片生成

使用图片生成API创建符合主题的背景图片：

```
https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt={prompt}&image_size=landscape_16_9
```

**提示词示例：**
- 赛博朋克风格：`cyberpunk city skyline at night with neon lights, futuristic architecture, rain, dramatic lighting`
- 远航主题：`voyage sailing ship at sunset on ocean with distant horizon, warm golden light, deep blue water`

### 3. 叠加层优化

调整叠加层样式以提高文字可读性：

```css
.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    rgba(15, 23, 42, 0.4) 0%,
    rgba(15, 23, 42, 0.6) 50%,
    rgba(15, 23, 42, 0.8) 100%
  );
}
```

### 4. 文字颜色调整

根据背景调整文字颜色和阴影：

```css
.hero-title {
  color: #ffffff;
  text-shadow: 0 4px 12px rgba(0, 0, 0, 0.7);
}

.hero-subtitle {
  color: #e2e8f0;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.6);
}
```

### 5. 字体选择

根据背景风格选择合适的字体：

- 现代简约背景：无衬线字体（Arial, Helvetica）
- 优雅/传统背景：衬线字体（Georgia, Times New Roman）

## 最佳实践

1. **测试不同背景**：尝试多种背景图片，选择最适合的
2. **确保可读性**：始终优先保证文字清晰可读
3. **保持一致性**：背景风格应与网站整体设计保持一致
4. **响应式考虑**：确保背景在不同屏幕尺寸下都能正常显示
5. **性能优化**：使用适当分辨率的图片，避免过大的文件尺寸

## 示例实现

```vue
<div class="hero-bg">
  <img 
    src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=voyage%20sailing%20ship%20at%20sunset&image_size=landscape_16_9" 
    alt="远航背景" 
    class="hero-bg-img"
  >
  <div class="hero-overlay"></div>
</div>
```

## 故障排除

- **文字模糊**：增加文字阴影或调整叠加层透明度
- **颜色不匹配**：尝试不同的叠加层颜色组合
- **图片加载慢**：优化图片尺寸或使用CDN加速
- **主题不匹配**：重新生成更符合网站风格的背景图片