# TicTacToe
这是一个基于Python和博弈树的井字棋人机对弈游戏。
## 目录
- [功能](#功能)
- [使用方法](#使用方法)
  - [下载发布版](#下载发布版)
  - [使用Python运行](#使用Python运行)
  - [自行打包](#自行打包)
- [后续开发思路](#后续开发思路)
## 功能
- 用户先手
- 用户后手
## 使用方法
### 下载发布版
下载[**发布版**](https://github.com/)即可直接使用。
### 使用Python运行
1. 生成棋谱文件
```bash
python train.py
```
> 注：如果无法运行train.py，可将`test/data_compfirst.csv`和`test/data_userfirst.csv`移动到play.py的同一目录下
2. 开始游戏
```bash
python play.py
```
### 自行打包
1. 安装cx_Freeze
```bash
pip install cx_Freeze
```
2. 打包
```bash
python setup.py build
```
## 后续开发思路
- 悔棋操作
- 模拟用户行为，提供不同搜索深度
