# 基金数据爬虫项目

基于Python的网络爬虫项目，用于从东方财富网获取基金公司排名数据和市场管理规模走势数据。

## 项目简介

本项目是一个轻量级的基金数据爬虫工具，旨在帮助投资者和研究者快速获取基金市场的公开数据。通过本项目，您可以：

- 获取基金公司排名列表数据
- 爬取基金市场规模历史走势
- 生成交互式数据可视化图表

## 功能特性

### 核心功能

- **基金公司排名爬取**：自动获取基金公司排名、成立时间、评级、管理规模等关键信息
- **市场规模趋势追踪**：爬取基金市场规模历史数据，追踪行业增长趋势
- **交互式图表展示**：生成支持悬停交互的数据可视化图表
- **数据导出**：支持CSV格式导出，便于后续数据分析

### 技术亮点

- 仅使用Python标准库，无需额外依赖
- 遵守网站robots协议，设置合理请求间隔
- 支持中文数据处理和展示
- 生成的CSV文件采用UTF-8编码，确保兼容性

## 项目结构

```
spider-open-fund/
├── fund_crawler.py              # 爬虫主程序
├── screenshot.py                # 页面截图工具（可选）
├── fund_companies.csv           # 基金公司排名数据
├── fund_market_scale_trend.csv  # 市场规模走势数据
├── fund_market_scale_trend.html # 交互式可视化图表
├── README.md                    # 项目说明文档
├── LICENSE                      # MIT开源许可证
└── .gitignore                   # Git忽略文件配置
```

## 快速开始

### 环境要求

- Python 3.6+
- 网络连接

### 安装步骤

1. **克隆项目**

```bash
git clone https://github.com/yourusername/spider-open-fund.git
cd spider-open-fund
```

2. **确认Python环境**

```bash
python --version
# 确保版本 >= 3.6
```

### 使用方法

#### 运行基金公司数据爬虫

```bash
python fund_crawler.py
```

运行后将自动爬取数据并保存到 `fund_companies.csv` 文件。

#### 查看交互式图表

直接在浏览器中打开 `fund_market_scale_trend.html` 文件即可查看基金市场规模走势图表。

## 数据说明

### 基金公司排名数据

| 字段 | 说明 |
|------|------|
| 序号 | 排名顺序 |
| 基金公司名称 | 公司全称 |
| 基金公司链接 | 公司详情页链接 |
| 成立时间 | 公司注册成立日期 |
| 天项评级 | 天天基金网评级（0-5星） |
| 全部管理规模 | 管理基金总规模（亿元） |
| 全部基金数 | 管理的基金产品数量 |
| 全部经理数 | 基金经理人数 |

### 市场规模走势数据

| 字段 | 说明 |
|------|------|
| 日期 | 统计日期 |
| 管理规模 | 当期基金市场总管理规模（亿元） |

## API接口分析

### 接口1：基金公司排名列表

**URL**: `https://fund.eastmoney.com/company/default.html`

**请求方式**: GET

**参数说明**:
| 参数 | 说明 | 可选值 |
|------|------|--------|
| page | 页码 | 1, 2, 3... |
| sortType | 排序字段 | allScale, fundNum, managerNum |
| sortDirect | 排序方向 | desc, asc |
| feType | 基金类型 | all, 001, 002, 003... |

### 接口2：基金市场规模走势

**URL**: `https://fund.eastmoney.com/Company/home/GetFundTotalScaleForChart`

**请求方式**: GET

**响应格式**: JSON

```json
{
  "x": ["2021-06-30", "2021-09-30", ...],
  "y": [22598107362172.78, 23425615826195.83, ...]
}
```

## 技术栈

- **编程语言**: Python 3
- **HTTP请求**: urllib.request
- **数据解析**: re (正则表达式)
- **数据存储**: csv
- **可视化**: Chart.js
- **版本控制**: Git

## 数据来源

- [东方财富网基金频道](https://fund.eastmoney.com)
- [天天基金网基金公司排名](https://fund.eastmoney.com/company/default.html)

## 注意事项

1. **合规使用**：请遵守目标网站的robots协议和使用条款
2. **请求限制**：程序设置了请求间隔，请勿过度频繁访问
3. **数据时效**：爬取的数据为实时数据，建议根据需要定期更新
4. **编码格式**：CSV文件采用UTF-8-BOM编码，确保Excel中正常显示中文

## 项目预览

### 交互式图表

![基金市场规模走势图](screenshot.png)

### 数据表示例

| 序号 | 基金公司名称 | 成立时间 | 天项评级 | 管理规模 |
|------|-------------|---------|---------|---------|
| 1 | 易方达基金管理有限公司 | 2001-04-17 | 5星 | 23,430亿 |
| 2 | 华夏基金管理有限公司 | 1998-04-09 | 5星 | 19,132亿 |
| 3 | 广发基金管理有限公司 | 2003-08-05 | 5星 | 16,123亿 |

## 贡献指南

欢迎提交Issue和Pull Request！

1. Fork本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建Pull Request

## 版本历史

- **v1.0.0** (2026-06-18)
  - 实现基金公司排名数据爬取
  - 实现市场规模走势数据爬取
  - 添加交互式可视化图表

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 联系方式

- 项目主页：https://github.com/goossduck/spider-open-fund
- 问题反馈：https://github.com/goossduck/spider-open-fund/issues

## 致谢

- 东方财富网提供数据支持
- Chart.js 提供可视化支持
- Python社区提供的优秀标准库

---

如果您觉得这个项目对您有帮助，请给我们一个 Star ⭐️
