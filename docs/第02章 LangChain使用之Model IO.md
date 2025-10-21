# 6、LangChain调用本地模型
## 6.1、Ollama的介绍
Ollama是在Github上的一个开源项目，其项目定位是：一个本地运行大模型的集成框架。目前主要针对主流的LlaMA架构的开源大模型设计，可以实现如 Qwen、Deepseek 等主流大模型的下载、启动和本地运行的自动化部署及推理流程。目前作为一个非常热门的大模型托管平台，已被包括LangChain、Taskweaver等在内的多个热门项目高度集成。

至于为什么要使用本地模型，最主要的是数据安全，企业都格外注重自己的数据安全，使用大模型厂商提供的API，很难避免这些厂商不会用你的这些企业数据来训练大模型。其次对于个人学习，使用国外的模型需要科学上网，并且大模型厂商提供的API接口的使用需要充值token才能使用，有一定的学习成本。

Ollama官方地址：[https://ollama.com/]()

## 6.2、Ollama下载、安装（以Windows为例）
1. 访问官网首页，点击download下载即可！
![[Pasted image 20251021214159.png]]

> [!NOTE] 注意
>需要注意的是拿到ollama安装包后，不要直接点击运行exe安装程序，因为默认会直接给你安装在C盘。
2. 在安装程序所在文件夹位置，打开CMD
![[Pasted image 20251021214526.png]]
3. 输入下面的命令，会将ollama程序安装在你指定的文件位置：
```bash
OllamaSetup.exe /dir="D:\Your\Custom\Path"
```
至此，Ollama就已经成功安装了，在cmd终端输入`ollama -v`，得到如下信息，说明安装成功：
![[Pasted image 20251021214840.png]]
## 6.3、Ollama常见设置
通过下面的命令就会自动下载运行指定名称的模型，但默认这种方式下载的模型文件（8b参数的模型也得5个G）会安装到C盘上。
```
ollama run <model_name>

```
![[Pasted image 20251021215140.png]]
修改ollama设置：在ollama程序的设置中可以自定义模型文件的存放位置：
![[Pasted image 20251021215238.png]]
> [!NOTE] 查看ollama支持的模型
>https://ollama.com/search

对于个人电脑，我们下载使用`deepseek-r1:7b`参数的就够我们学习使用了。
```bash
ollama run deepseek-r1:7b
```
下载成功后，就可以在CMD窗口和模型对话啦：
![[Pasted image 20251021215646.png]]
除了CMD窗口的方式，Ollama客户端工具也支持模型对话：
![[Pasted image 20251021215826.png]]
选择我们刚刚下载成功的本地模型
## 6.4、LangChain调用本地模型
直接调用本地部署的大模型，不需要像调用大模型厂商提供的API一样，apikey、base_url都不需要传递.

```python
from langchain_ollama import ChatOllama  
  
# 调用本地模型服务，不需要传递 base_url 参数  
ollama_llm = ChatOllama(model="deepseek-r1:7b")  
response = ollama_llm.invoke("介绍下你自己吧")  
print(response.content)  
```
但如果ollama是部署在其他服务器上，和langchain客户端不在同一台机器上，那么在创建对话模型时，需要额外传递`base_url`参数。代码如下：
```python
# 如果ollama服务部署在另一台服务器上，那么在创建大模型实例时，需要传递 base_url 参数，通过ip:port的方式指明ollama服务所在位置。  
ollama_llm = ChatOllama(model="deepseek-r1:7b", base_url="http://192.168.31.74:11434")  
response = ollama_llm.invoke("介绍下你自己吧")  
print(response.content)
```
运行效果如下：
![[Pasted image 20251021221547.png]]
## 6.5 常见问题

需要说明的是，Ollama默认是不支持通过IP端口的方式来远程访问其接口的，需要设置环境变量后才支持访问。
### Linux环境
1、首先停止ollama服务：systemctl stop ollama  
2、修改ollama的service文件：/etc/systemd/system/ollama.service  
在[Service]下边增加两行：

```sh
Environment="OLLAMA_HOST=0.0.0.0"
Environment="OLLAMA_ORIGINS=*"
```
或者如果要限制端口就加上软件
```sh
Environment="OLLAMA_HOST=0.0.0.0:11434" 
Environment="OLLAMA_ORIGINS=*"
```
ollama默认启动模型的端口是`11434`
3、重载daemon文件 systemctl daemon-reload  
4、启动ollama服务 systemctl start ollama
### Windows环境
1、首先停止ollama服务的允许。直接点击退出ollama
![[Pasted image 20251021221214.png]]
2、为当前windows系统添加环境变量：电脑-属性-高级系统设置-环境变量  
变量：`OLLAMA_HOST`，值：`0.0.0.0:11434`  
3、重新打开ollama应用即可！
