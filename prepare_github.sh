#!/bin/bash
# GitHub仓库准备脚本

echo "=== 量化策略库GitHub部署准备 ==="

# 1. 初始化Git仓库
echo "1. 初始化Git仓库..."
git init
git add .

# 2. 创建.gitignore文件
echo "2. 创建.gitignore文件..."
cat > .gitignore << EOF
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Data files
*.csv
*.json
*.pkl
*.h5
*.feather
*.parquet

# Logs
*.log
logs/

# OS
.DS_Store
Thumbs.db

# Temporary files
*.tmp
*.temp
EOF

git add .gitignore

# 3. 创建初始提交
echo "3. 创建初始提交..."
git commit -m "初始提交: 量化交易策略库 v1.0

包含:
- 9个量化交易策略 (股票3个, 期货2个, 加密货币2个, 期权2个)
- 策略分类文档
- 策略搜集器Python脚本
- 完整的项目结构"

# 4. 显示部署说明
echo ""
echo "=== 部署说明 ==="
echo ""
echo "已准备好Git仓库，接下来需要:"
echo ""
echo "1. 在GitHub创建新仓库:"
echo "   - 访问 https://github.com/new"
echo "   - 仓库名: quant-strategies (或其他名称)"
echo "   - 描述: 量化交易策略库 - 系统化搜集整理全网量化策略"
echo "   - 选择公开或私有"
echo ""
echo "2. 添加远程仓库并推送:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/quant-strategies.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. 可选: 启用GitHub Pages"
echo "   - Settings > Pages > Source: main branch /docs folder"
echo ""
echo "4. 设置自动更新 (可选):"
echo "   - 添加GitHub Actions自动运行策略搜集器"
echo "   - 设置每日/每周自动更新"
echo ""
echo "=== 当前仓库状态 ==="
git status
echo ""
echo "=== 文件统计 ==="
find . -type f -name "*.md" -o -name "*.py" -o -name "*.json" -o -name "*.csv" | wc -l | xargs echo "总文件数:"
find . -type f -name "*.md" | wc -l | xargs echo "Markdown文件:"
find . -type f -name "*.py" | wc -l | xargs echo "Python文件:"
find . -type f -name "*.json" | wc -l | xargs echo "JSON文件:"
find . -type f -name "*.csv" | wc -l | xargs echo "CSV文件:"