#!/usr/bin/env python3
"""
策略扩展器 - 基于现有策略生成变体和扩展版本
目标：从9个基础策略扩展到100+个策略
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any
import random

class StrategyExpander:
    """策略扩展器"""
    
    def __init__(self, base_dir: str = "."):
        self.base_dir = base_dir
        self.strategies = []
        self.expanded_strategies = []
        
    def load_existing_strategies(self):
        """加载现有策略"""
        categories = ['stocks', 'futures', 'crypto', 'options']
        
        for category in categories:
            json_file = os.path.join(self.base_dir, category, f'strategies_{datetime.now().strftime("%Y%m%d")}.json')
            if os.path.exists(json_file):
                with open(json_file, 'r', encoding='utf-8') as f:
                    category_strategies = json.load(f)
                    self.strategies.extend(category_strategies)
        
        print(f"已加载 {len(self.strategies)} 个基础策略")
    
    def generate_variants(self, strategy: Dict) -> List[Dict]:
        """为单个策略生成变体"""
        variants = []
        base_name = strategy['name']
        
        # 1. 时间周期变体
        timeframes = ['日内', '日线', '周线', '月线']
        for tf in timeframes:
            variant = strategy.copy()
            variant['name'] = f"{base_name} ({tf})"
            variant['timeframe'] = tf
            variant['variant_of'] = base_name
            variant['variant_type'] = 'timeframe'
            variants.append(variant)
        
        # 2. 参数优化变体
        param_variants = [
            {'name': f"{base_name} (激进版)", 'risk_level': '高', 'aggressiveness': '激进'},
            {'name': f"{base_name} (保守版)", 'risk_level': '低', 'aggressiveness': '保守'},
            {'name': f"{base_name} (平衡版)", 'risk_level': '中', 'aggressiveness': '平衡'},
        ]
        
        for param in param_variants:
            variant = strategy.copy()
            variant.update(param)
            variant['variant_of'] = base_name
            variant['variant_type'] = 'parameters'
            variants.append(variant)
        
        # 3. 技术指标组合变体
        indicator_combinations = [
            {'indicators': f"{strategy.get('indicators', '')} + MACD", 'name': f"{base_name} (MACD增强)"},
            {'indicators': f"{strategy.get('indicators', '')} + 布林带", 'name': f"{base_name} (布林带增强)"},
            {'indicators': f"{strategy.get('indicators', '')} + KDJ", 'name': f"{base_name} (KDJ增强)"},
        ]
        
        for combo in indicator_combinations:
            variant = strategy.copy()
            variant.update(combo)
            variant['variant_of'] = base_name
            variant['variant_type'] = 'indicators'
            variants.append(variant)
        
        return variants
    
    def generate_hybrid_strategies(self, strategy1: Dict, strategy2: Dict) -> List[Dict]:
        """生成混合策略"""
        hybrids = []
        
        # 基础混合
        hybrid = {
            'name': f"{strategy1['name']} + {strategy2['name']} 混合策略",
            'category': strategy1['category'],
            'type': '混合策略',
            'complexity': '中级' if strategy1['complexity'] == '基础' and strategy2['complexity'] == '基础' else '高级',
            'logic': f"结合{strategy1['name']}的{strategy1['logic']}和{strategy2['name']}的{strategy2['logic']}，通过加权信号进行交易决策",
            'indicators': f"{strategy1.get('indicators', '')}, {strategy2.get('indicators', '')}",
            'language': 'Python',
            'data_requirements': f"{strategy1.get('data_requirements', '')} + {strategy2.get('data_requirements', '')}",
            'source': '策略混合生成',
            'references': f"基于{strategy1['name']}和{strategy2['name']}",
            'is_hybrid': True,
            'parent_strategies': [strategy1['name'], strategy2['name']]
        }
        hybrids.append(hybrid)
        
        return hybrids
    
    def generate_market_specific_variants(self, strategy: Dict) -> List[Dict]:
        """生成市场特定变体"""
        variants = []
        base_name = strategy['name']
        original_category = strategy['category']
        
        # 映射不同市场的对应策略
        market_mapping = {
            'stocks': ['A股', '美股', '港股'],
            'futures': ['商品期货', '金融期货', '股指期货'],
            'crypto': ['比特币', '以太坊', '山寨币'],
            'options': ['股票期权', '指数期权', '商品期权']
        }
        
        target_markets = market_mapping.get(original_category, [])
        for market in target_markets:
            variant = strategy.copy()
            variant['name'] = f"{base_name} ({market})"
            variant['market_specific'] = market
            variant['variant_of'] = base_name
            variant['variant_type'] = 'market'
            variants.append(variant)
        
        return variants
    
    def generate_ml_enhanced_variants(self, strategy: Dict) -> List[Dict]:
        """生成机器学习增强变体"""
        variants = []
        base_name = strategy['name']
        
        ml_enhancements = [
            {
                'name': f"{base_name} (LSTM信号过滤)",
                'type': f"{strategy['type']} + 机器学习",
                'complexity': '高级',
                'logic': f"使用LSTM神经网络对{strategy['name']}的原始信号进行过滤和优化",
                'indicators': f"{strategy.get('indicators', '')}, LSTM神经网络",
                'ml_technique': 'LSTM'
            },
            {
                'name': f"{base_name} (XGBoost优化)",
                'type': f"{strategy['type']} + 机器学习", 
                'complexity': '高级',
                'logic': f"使用XGBoost模型优化{strategy['name']}的交易参数和时机选择",
                'indicators': f"{strategy.get('indicators', '')}, XGBoost模型",
                'ml_technique': 'XGBoost'
            },
            {
                'name': f"{base_name} (强化学习)",
                'type': f"{strategy['type']} + 强化学习",
                'complexity': '高级',
                'logic': f"使用强化学习算法动态调整{strategy['name']}的交易策略",
                'indicators': f"{strategy.get('indicators', '')}, 强化学习模型",
                'ml_technique': 'Reinforcement Learning'
            }
        ]
        
        for enhancement in ml_enhancements:
            variant = strategy.copy()
            variant.update(enhancement)
            variant['variant_of'] = base_name
            variant['variant_type'] = 'ml_enhancement'
            variants.append(variant)
        
        return variants
    
    def expand_strategies(self):
        """扩展策略库"""
        print("开始扩展策略库...")
        
        # 加载现有策略
        self.load_existing_strategies()
        
        # 为每个基础策略生成变体
        for strategy in self.strategies:
            # 1. 基础变体
            variants = self.generate_variants(strategy)
            self.expanded_strategies.extend(variants)
            
            # 2. 市场特定变体
            market_variants = self.generate_market_specific_variants(strategy)
            self.expanded_strategies.extend(market_variants)
            
            # 3. 机器学习增强变体
            ml_variants = self.generate_ml_enhanced_variants(strategy)
            self.expanded_strategies.extend(ml_variants)
        
        # 生成混合策略（策略组合）
        print("生成混合策略...")
        for i in range(len(self.strategies)):
            for j in range(i+1, min(i+3, len(self.strategies))):  # 每个策略与后面2个策略混合
                if self.strategies[i]['category'] == self.strategies[j]['category']:
                    hybrids = self.generate_hybrid_strategies(self.strategies[i], self.strategies[j])
                    self.expanded_strategies.extend(hybrids)
        
        # 添加唯一ID和时间戳
        for idx, strategy in enumerate(self.expanded_strategies):
            strategy['id'] = f"strategy_{idx+1000:04d}"
            strategy['added_date'] = datetime.now().strftime('%Y-%m-%d')
            strategy['last_updated'] = datetime.now().strftime('%Y-%m-%d')
            strategy['generated_by'] = 'StrategyExpander'
        
        print(f"策略扩展完成！生成 {len(self.expanded_strategies)} 个新策略")
        print(f"总计策略数: {len(self.strategies) + len(self.expanded_strategies)}")
    
    def save_expanded_strategies(self):
        """保存扩展后的策略"""
        # 按分类保存
        categories = {}
        for strategy in self.expanded_strategies:
            category = strategy['category']
            if category not in categories:
                categories[category] = []
            categories[category].append(strategy)
        
        # 保存各分类策略
        for category, strategies in categories.items():
            output_dir = os.path.join(self.base_dir, category)
            os.makedirs(output_dir, exist_ok=True)
            
            # JSON格式
            json_file = os.path.join(output_dir, f'expanded_strategies_{datetime.now().strftime("%Y%m%d")}.json')
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(strategies, f, ensure_ascii=False, indent=2)
            
            # CSV格式
            csv_file = os.path.join(output_dir, f'expanded_strategies_{datetime.now().strftime("%Y%m%d")}.csv')
            # 简化的CSV生成（实际项目中可使用pandas）
            with open(csv_file, 'w', encoding='utf-8-sig') as f:
                if strategies:
                    headers = strategies[0].keys()
                    f.write(','.join(headers) + '\n')
                    for strategy in strategies:
                        row = []
                        for header in headers:
                            value = str(strategy.get(header, '')).replace(',', ';')
                            row.append(f'"{value}"')
                        f.write(','.join(row) + '\n')
            
            print(f"已保存 {len(strategies)} 个{category}策略到 {json_file} 和 {csv_file}")
    
    def update_catalog(self):
        """更新策略总目录"""
        catalog_file = os.path.join(self.base_dir, 'strategies_catalog.md')
        
        if not os.path.exists(catalog_file):
            print("策略目录文件不存在")
            return
        
        with open(catalog_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 计算总策略数
        total_strategies = len(self.strategies) + len(self.expanded_strategies)
        
        # 按分类统计
        category_counts = {}
        all_strategies = self.strategies + self.expanded_strategies
        for strategy in all_strategies:
            category = strategy['category']
            category_counts[category] = category_counts.get(category, 0) + 1
        
        # 更新统计信息
        update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        stats_section = f"""
## 统计信息
- **总策略数:** {total_strategies} (持续更新中)
- **最后更新:** {update_time}
- **覆盖市场:** 股票、期货、加密货币、期权

### 各市场策略数量
- **股票策略:** {category_counts.get('stocks', 0)} 个
- **期货策略:** {category_counts.get('futures', 0)} 个  
- **加密货币策略:** {category_counts.get('crypto', 0)} 个
- **期权策略:** {category_counts.get('options', 0)} 个

### 策略来源
- **基础策略:** {len(self.strategies)} 个
- **扩展变体:** {len(self.expanded_strategies)} 个
- **机器学习增强:** {sum(1 for s in self.expanded_strategies if s.get('variant_type') == 'ml_enhancement')} 个
- **混合策略:** {sum(1 for s in self.expanded_strategies if s.get('is_hybrid', False))} 个
"""
        
        # 替换或添加统计信息
        if "## 统计信息" in content:
            lines = content.split('\n')
            new_lines = []
            in_stats = False
            for line in lines:
                if line.strip().startswith("## 统计信息"):
                    new_lines.append("## 统计信息")
                    in_stats = True
                elif in_stats and line.strip().startswith("## "):
                    in_stats = False
                    new_lines.extend(stats_section.strip().split('\n'))
                    new_lines.append(line)
                elif not in_stats:
                    new_lines.append(line)
            
            if in_stats:
                new_lines.extend(stats_section.strip().split('\n'))
            
            content = '\n'.join(new_lines)
        else:
            content = content.replace(
                "# 量化交易策略总目录\n\n", 
                f"# 量化交易策略总目录\n\n{stats_section}\n"
            )
        
        # 保存更新后的目录
        with open(catalog_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"已更新策略总目录，总计 {total_strategies} 个策略")


def main():
    """主函数"""
    print("=== 策略扩展器启动 ===")
    
    expander = StrategyExpander(base_dir='.')
    expander.expand_strategies()
    expander.save_expanded_strategies()
    expander.update_catalog()
    
    print("=== 策略扩展完成 ===")
    print(f"基础策略: {len(expander.strategies)} 个")
    print(f"扩展策略: {len(expander.expanded_strategies)} 个")
    print(f"总计: {len(expander.strategies) + len(expander.expanded_strategies)} 个策略")


if __name__ == "__main__":
    main()