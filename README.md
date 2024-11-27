# minimax_qiming

`minimax_qiming` 是一个方便的 Python 工具包，用于随机生成 **User-Agent** 字符串，支持 PC 和移动端浏览器。

## 功能特性

- 随机选择 **PC 端 User-Agent**。
- 随机选择 **移动端 User-Agent**。
- 适用于爬虫、自动化测试等场景。

## 安装

通过 pip 安装：

```bash
pip install minimax_qiming
```
## 使用方法
```bash
import minimax_qiming

#随机获取移动端 User-Agent
mobile_ua = minimax_qiming.get_mobile_ua()
```
## 数据来源
minimax_qiming 使用内置的 export_file.csv 文件作为 User-Agent 数据源。该文件已随包打包，无需额外配置。