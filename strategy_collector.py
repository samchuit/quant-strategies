#!/usr/bin/env python3
"""
量化交易策略搜集器
自动搜集全网量化交易策略并整理归纳
"""

import os
import json
import time
from datetime import datetime
from typing import Dict, List, Optional
import pandas as pd

class StrategyCollector:
    """策略搜集器基类"""
    
    def __init__(self, output_dir: str = "."):
        self.output_dir = output_dir
        self.strategies = []
        self.categories = {
            'stocks': '股票策略',
            'futures': '期货策略', 
            'crypto': '加密货币策略',
            'options': '期权策略'
        }
        
        # 创建输出目录
        for category in self.categories.keys():
            os.makedirs(os.path.join(output_dir, category), exist_ok=True)
    
    def add_strategy(self, strategy: Dict):
        """添加策略到列表"""
        strategy['added_date'] = datetime.now().strftime('%Y-%m-%d')
        strategy['last_updated'] = datetime.now().strftime('%Y-%m-%d')
        self.strategies.append(strategy)
    
    def save_to_json(self, category: str):
        """保存策略到JSON文件"""
        category_strategies = [
            s for s in self.strategies 
            if s.get('category') == category
        ]
        
        if not category_strategies:
            return
        
        output_file = os.path.join(
            self.output_dir, 
            category, 
            f'strategies_{datetime.now().strftime("%Y%m%d")}.json'
        )
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(category_strategies, f, ensure_ascii=False, indent=2)
        
        print(f"已保存 {len(category_strategies)} 个{self.categories[category]}到 {output_file}")
    
    def save_to_csv(self, category: str):
        """保存策略到CSV文件"""
        category_strategies = [
            s for s in self.strategies 
            if s.get('category') == category
        ]
        
        if not category_strategies:
            return
        
        df = pd.DataFrame(category_strategies)
        output_file = os.path.join(
            self.output_dir, 
            category, 
            f'strategies_{datetime.now().strftime("%Y%m%d")}.csv'
        )
        
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f"已保存 {len(category_strategies)} 个{self.categories[category]}到 {output_file}")
    
    def update_catalog(self):
        """更新策略总目录"""
        catalog_file = os.path.join(self.output_dir, 'strategies_catalog.md')
        
        # 读取现有目录
        if os.path.exists(catalog_file):
            with open(catalog_file, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            content = "# 量化交易策略总目录\n\n## 统计信息\n"
        
        # 更新统计信息
        stats = {}
        for category in self.categories.keys():
            count = len([s for s in self.strategies if s.get('category') == category])
            stats[category] = count
        
        total = sum(stats.values())
        
        # 生成更新内容
        update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        stats_section = f"""
## 统计信息
- **总策略数:** {total} (持续更新中)
- **最后更新:** {update_time}
- **覆盖市场:** 股票、期货、加密货币、期权

### 各市场策略数量
- **股票策略:** {stats.get('stocks', 0)} 个
- **期货策略:** {stats.get('futures', 0)} 个  
- **加密货币策略:** {stats.get('crypto', 0)} 个
- **期权策略:** {stats.get('options', 0)} 个
"""
        
        # 替换或添加统计信息
        if "## 统计信息" in content:
            # 找到统计信息部分并替换
            lines = content.split('\n')
            new_lines = []
            in_stats = False
            for line in lines:
                if line.strip().startswith("## 统计信息"):
                    new_lines.append("## 统计信息")
                    in_stats = True
                elif in_stats and line.strip().startswith("## "):
                    # 遇到下一个章节，结束替换
                    in_stats = False
                    new_lines.extend(stats_section.strip().split('\n'))
                    new_lines.append(line)
                elif not in_stats:
                    new_lines.append(line)
            
            if in_stats:
                # 如果直到文件结束都在统计信息部分
                new_lines.extend(stats_section.strip().split('\n'))
            
            content = '\n'.join(new_lines)
        else:
            # 在文件开头添加统计信息
            content = content.replace(
                "# 量化交易策略总目录\n\n", 
                f"# 量化交易策略总目录\n\n{stats_section}\n"
            )
        
        # 保存更新后的目录
        with open(catalog_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"已更新策略总目录，总计 {total} 个策略")


class KnownStrategiesCollector(StrategyCollector):
    """已知策略搜集器（手动添加知名策略）"""
    
    def collect_known_strategies(self):
        """搜集已知的知名量化策略"""
        
        # 股票策略
        stock_strategies = [
            {
                'name': '双均线策略',
                'category': 'stocks',
                'type': '趋势跟踪',
                'complexity': '基础',
                'logic': '短期均线上穿长期均线时买入，下穿时卖出',
                'indicators': 'SMA, EMA',
                'language': 'Python',
                'data_requirements': '日级行情数据',
                'source': '传统技术分析',
                'references': 'https://www.investopedia.com/terms/m/movingaverage.asp'
            },
            {
                'name': 'RSI超买超卖策略',
                'category': 'stocks',
                'type': '均值回归',
                'complexity': '基础',
                'logic': 'RSI低于30超卖买入，高于70超买卖出',
                'indicators': 'RSI',
                'language': 'Python',
                'data_requirements': '日级行情数据',
                'source': '传统技术分析',
                'references': 'https://www.investopedia.com/terms/r/rsi.asp'
            },
            {
                'name': '配对交易策略',
                'category': 'stocks',
                'type': '统计套利',
                'complexity': '中级',
                'logic': '寻找相关性高的股票对，做多低估股票，做空高估股票',
                'indicators': '协整关系、价差Z-score',
                'language': 'Python',
                'data_requirements': '多股票日级行情数据',
                'source': '统计套利经典策略',
                'references': 'https://en.wikipedia.org/wiki/Pairs_trade'
            }
        ]
        
        # 期货策略
        futures_strategies = [
            {
                'name': '海龟交易法则',
                'category': 'futures',
                'type': '趋势跟踪',
                'complexity': '基础',
                'logic': '突破N日高低点入场，ATR止损',
                'indicators': '突破点、ATR',
                'language': 'Python',
                'data_requirements': '日级期货行情数据',
                'source': '经典CTA策略',
                'references': 'https://en.wikipedia.org/wiki/Turtle_traders'
            },
            {
                'name': 'Dual Thrust策略',
                'category': 'futures',
                'type': '趋势跟踪',
                'complexity': '基础',
                'logic': '基于开盘价和收盘价计算上下轨，突破上轨做多，突破下轨做空',
                'indicators': '最高价、最低价、开盘价、收盘价',
                'language': 'Python',
                'data_requirements': '日级期货行情数据',
                'source': '经典日内交易策略',
                'references': 'https://www.quantconnect.com/tutorials/strategy-library/dual-thrust-trading-algorithm'
            }
        ]
        
        # 加密货币策略
        crypto_strategies = [
            {
                'name': '比特币动量策略',
                'category': 'crypto',
                'type': '趋势跟踪',
                'complexity': '基础',
                'logic': '基于比特币价格动量进行趋势交易',
                'indicators': '价格动量、移动平均',
                'language': 'Python',
                'data_requirements': '加密货币分钟级/日级数据',
                'source': '加密货币经典策略',
                'references': 'https://github.com/quantopian/research_public'
            },
            {
                'name': '跨交易所套利',
                'category': 'crypto',
                'type': '统计套利',
                'complexity': '中级',
                'logic': '利用不同交易所之间的价格差异进行套利',
                'indicators': '价差、交易费用',
                'language': 'Python',
                'data_requirements': '多交易所实时行情数据',
                'source': '加密货币特有策略',
                'references': 'https://www.coindesk.com/learn/crypto-arbitrage/'
            }
        ]
        
        # 期权策略
        options_strategies = [
            {
                'name': '备兑认购策略',
                'category': 'options',
                'type': '收入策略',
                'complexity': '基础',
                'logic': '持有股票的同时卖出认购期权，获取权利金收入',
                'indicators': '隐含波动率、Delta',
                'language': 'Python',
                'data_requirements': '期权链数据、股票数据',
                'source': '经典期权策略',
                'references': 'https://www.investopedia.com/terms/c/coveredcall.asp'
            },
            {
                'name': '跨式组合策略',
                'category': 'options',
                'type': '波动率交易',
                'complexity': '中级',
                'logic': '同时买入相同行权价和到期日的认购和认沽期权，赌波动率上升',
                'indicators': '隐含波动率、Vega',
                'language': 'Python',
                'data_requirements': '期权链数据',
                'source': '经典期权策略',
                'references': 'https://www.investopedia.com/terms/s/straddle.asp'
            }
        ]
        
        # 添加所有策略
        all_strategies = (
            stock_strategies + 
            futures_strategies + 
            crypto_strategies + 
            options_strategies
        )
        
        for strategy in all_strategies:
            self.add_strategy(strategy)
        
        print(f"已添加 {len(all_strategies)} 个已知策略")


def main():
    """主函数"""
    print("开始搜集量化交易策略...")
    
    # 创建搜集器
    collector = KnownStrategiesCollector(output_dir='.')
    
    # 搜集已知策略
    collector.collect_known_strategies()
    
    # 保存各分类策略
    for category in ['stocks', 'futures', 'crypto', 'options']:
        collector.save_to_json(category)
        collector.save_to_csv(category)
    
    # 更新总目录
    collector.update_catalog()
    
    print("策略搜集完成！")


if __name__ == "__main__":
    main()