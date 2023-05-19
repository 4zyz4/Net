# 安装命令： 
```
sudo bash install_server.sh
```   
> <b>安装后会用红底白字标出服务器信息，请不要忘记。`最好记在一个文件里`</b>
***
# 安装后启动：
```
python server.py
```
***
# 连接服务器
> 需要使用Vscode Desktop连接Codespaces
## 找到之前的服务器信息
例子：
```
Your Server IP        :  20.212.13.247 
Your Server Port      :  16246 
Your Password         :  12345678 
Your Encryption Method:  aes-256-gcm 
```
### 点击Vscode中的`端口`：
![image](https://github.com/4zyz4/Net/assets/133503200/c8a12539-4de1-4850-bec7-9c212082b0f5)
### 点击`添加端口`：
![image](https://github.com/4zyz4/Net/assets/133503200/e46122aa-a764-4858-b087-478c91060286)
### 输入Your Server Port 中的值。
## 下载库中的Shadowsocks.exe(可以直接从Codespaces中拖出来)  
### 启动程序
```
地址填写：127.0.0.1  
端口填写Your Server Port 中的值  
密码填写Your Password 中的值
加密方式选择Your Encryption Method 中的字段
```
其他不用管  
点击`确定`  
关闭窗口

右键托盘中的小飞机  
将鼠标移动到`系统代理`  
点击`全局模式`  
![image](https://github.com/4zyz4/Net/assets/133503200/b8db8771-120b-45ef-837d-036f1c35c3ec)
