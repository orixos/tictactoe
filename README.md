# TicTacToe
这是一个基于Python和博弈树的井字棋人机对弈游戏。
## 目录
- [功能](#功能)
- [使用方法](#使用方法)
  - [下载发布版](#下载发布版)
  - [使用Python运行](#使用Python运行)
  - [自行打包](#自行打包)
- [算法优化](#算法优化)
  - [参数调整](#参数调整)
- [后续开发思路](#后续开发思路)
## 功能
- [x] 人机对战
  - [x] 用户先手
  - [x] 用户后手
## 使用方法
### 下载发布版
下载[**发布版**](https://github.com/orixos/tictactoe)即可直接使用。（发布版将于近期提供）
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
3. 添加棋谱文件
将`data_compfirst.csv`和`data_userfirst.csv`复制到可执行文件的同一目录下

## 算法优化
### 参数调整
如果您对人机对弈的效果感到不满意，可以尝试调整`train.py`中第23行字典的3个Value参数。
## 后续开发思路
- [ ] 优化用户体验
- [ ] 增加悔棋操作
- [ ] 模拟用户行为，提供不同搜索深度
- [ ] 构建接口，便于其它应用程序使用
- [ ] 增加图形界面
- [ ] 增加双人对战功能
