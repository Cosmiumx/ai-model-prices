# AI 模型价格自动获取工具（MVP 版本）

[![自动更新](https://github.com/YOUR_USERNAME/ai-model-prices/workflows/更新%20AI%20模型价格/badge.svg)](https://github.com/YOUR_USERNAME/ai-model-prices/actions)

## 功能
- 🤖 自动从 **LiteLLM** 获取 1700+ AI 模型的价格信息
- 📊 包含价格、上下文窗口等详细数据
- 🔄 支持 GitHub Actions 自动化每日更新
- 💰 完全免费运行（0 成本）

## 快速开始

### 1. 创建虚拟环境（推荐）
```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境（macOS/Linux）
source venv/bin/activate

# 激活虚拟环境（Windows）
# venv\Scripts\activate
```

### 2. 安装依赖
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. 运行脚本
```bash
python fetch_prices.py
```

### 4. 查看结果
生成的 `model_prices.json` 包含所有模型的价格信息（约 1752 个模型）。

## 输出格式
```json
{
  "updated_at": "2025-11-14T...",
  "total_models": 100,
  "models": [
    {
      "vendor": "openai",
      "model": "gpt-4",
      "full_name": "openai/gpt-4",
      "input_price": 0.03,
      "output_price": 0.06,
      "currency": "USD",
      "unit": "per_1M_tokens"
    }
  ]
}
```

## 后续计划
- [ ] 添加 GitHub Actions 自动化
- [ ] 多数据源聚合
- [ ] 价格历史记录
- [ ] 前端展示页面

