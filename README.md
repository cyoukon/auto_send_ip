# auto_send_ip
监测公网IP，当ip发生变化时自动发送邮件

### 背景
[在一台旧手机上装了个Linux deploy](https://zhuanlan.zhihu.com/p/266585456)，在公网IP不固定的情况下，
想要随时能够连接到这台服务器，就需要知道家里变化过的公网IP。
于是就有了这个程序

### 运行环境
* windows/linux
* python3.X

### 使用方法
* 打开cmd进入到代码所在目录，输入`pip install -r requirements.txt`后回车
* 根据自己实际情况配置config.py文件
* 运行main.py

- [ ] 在Linux上也可以把mian.py配置成服务，并设置开机启动，这样就不用每次都手动运行了/

### 效果图
![效果图](/sample.png)
