#!/usr/bin/env python3
"""
AI 模型价格自动获取脚本（MVP 版本）
功能：从 Helicone 获取 LLM 价格数据并保存为 JSON
"""

import requests
import json
from datetime import datetime
import sys

def fetch_litellm_prices():
    """从 LiteLLM 获取价格数据"""
    print("📡 正在获取 LiteLLM 价格数据...")
    
    # LiteLLM 的价格数据源（持续维护中）
    url = "https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json"
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        print(f"✅ 成功获取数据")
        return data
    except requests.exceptions.RequestException as e:
        print(f"❌ 获取失败: {e}")
        sys.exit(1)

def format_prices(raw_data):
    """格式化价格数据"""
    print("🔄 正在格式化数据...")
    
    formatted_data = {
        "updated_at": datetime.now().isoformat(),
        "total_models": 0,
        "models": []
    }
    
    for model_name, info in raw_data.items():
        # 提取供应商和模型名称
        parts = model_name.split("/")
        vendor = parts[0] if len(parts) > 1 else "unknown"
        model = "/".join(parts[1:]) if len(parts) > 1 else model_name
        
        # LiteLLM 数据格式: input_cost_per_token, output_cost_per_token
        input_price = info.get("input_cost_per_token", 0)
        output_price = info.get("output_cost_per_token", 0)
        
        # 转换为每百万 tokens 的价格
        input_price_per_million = input_price * 1_000_000 if input_price else 0
        output_price_per_million = output_price * 1_000_000 if output_price else 0
        
        formatted_data["models"].append({
            "vendor": vendor,
            "model": model,
            "full_name": model_name,
            "input_price": input_price_per_million,
            "output_price": output_price_per_million,
            "context_window": info.get("max_tokens", "N/A"),
            "currency": "USD",
            "unit": "per_1M_tokens"
        })
    
    formatted_data["total_models"] = len(formatted_data["models"])
    print(f"✅ 格式化完成，共 {formatted_data['total_models']} 个模型")
    
    return formatted_data

def save_to_json(data, filename="model_prices.json"):
    """保存数据到 JSON 文件"""
    print(f"💾 正在保存到 {filename}...")
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ 保存成功！")

def main():
    print("=" * 50)
    print("🚀 AI 模型价格获取工具 - MVP 版本")
    print("=" * 50)
    print()
    
    # 1. 获取原始数据
    raw_data = fetch_litellm_prices()
    
    # 2. 格式化数据
    formatted_data = format_prices(raw_data)
    
    # 3. 保存到文件
    save_to_json(formatted_data)
    
    # 4. 显示统计信息
    print()
    print("📊 统计信息:")
    print(f"   - 更新时间: {formatted_data['updated_at']}")
    print(f"   - 模型总数: {formatted_data['total_models']}")
    print(f"   - 文件位置: model_prices.json")
    print()
    print("🎉 完成！")

if __name__ == "__main__":
    main()

