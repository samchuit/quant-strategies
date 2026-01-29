# 量化交易策略库

## 项目概述
本仓库系统化搜集、整理和归纳全网量化交易策略，涵盖股票、期货、加密货币和期权四大市场类型。

## 数据来源
- 学术论文平台 (arXiv, SSRN)
- 开源代码库 (GitHub, GitLab)
- 量化社区 (QuantConnect, 聚宽, RiceQuant)
- 技术博客 (Medium, Towards Data Science)
- 专业论坛 (Reddit r/algotrading, Stack Exchange)
- 中文资源 (掘金, CSDN, 知乎量化专栏)

## 目录结构
```
quant_strategies/
├── README.md                    # 项目说明
├── strategies_catalog.md        # 策略总目录
├── stocks/                      # 股票策略
│   ├── README.md
│   ├── trend_following/
│   ├── mean_reversion/
│   └── machine_learning/
├── futures/                     # 期货策略
│   ├── README.md
│   ├── cta_strategies/
│   └── statistical_arbitrage/
├── crypto/                      # 加密货币策略
│   ├── README.md
│   ├── onchain_analysis/
│   └── high_frequency/
├── options/                     # 期权策略
│   ├── README.md
│   ├── volatility_trading/
│   └── exotic_options/
├── common/                      # 通用工具
│   ├── data_fetchers.py
│   ├── backtest_framework.py
│   └── risk_management.py
└── references/                  # 参考文献
    ├── papers/
    ├── blogs/
    └── tutorials/
```

## 搜集标准
每个策略记录包含：
1. 策略名称
2. 核心逻辑描述
3. 技术指标/模型
4. 代码语言 (Python为主)
5. 数据需求
6. 回测表现 (如有)
7. 风险特征
8. 源码链接
9. 论文/文档链接

## 更新计划
- 每日自动搜集新增策略
- 每周整理归纳
- 每月发布版本更新

## 贡献指南
欢迎提交新的策略或改进现有策略实现。

## 免责声明
本仓库仅供研究学习使用，不构成投资建议。量化交易存在风险，请谨慎决策。

---
**创建者:** 卡尔 (Sam的量化研究助理)
**创建时间:** 2025年4月6日
**最后更新:** 2025年4月6日