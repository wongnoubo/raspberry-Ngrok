# 基于Ngrok内网穿刺实现web端控制树莓派IO口。

<a name="6cf24859"></a>
## Ngrok服务

<a name="e4a3fb20"></a>
### 1.1 [参考](https://www.jianshu.com/p/2e1c9a3a5483)
![1.png](https://cdn.nlark.com/yuque/0/2019/png/237720/1551627319957-bc15ddf1-0af7-4824-b4a3-aaf6db882fb6.png#align=left&display=inline&height=321&name=1.png&originHeight=321&originWidth=532&size=7911&status=done&width=532)<br />注册Ngrok账号<br />
![2.png](https://cdn.nlark.com/yuque/0/2019/png/237720/1551627363022-c38ce37a-5b78-48b3-836f-d0efb00443b5.png#align=left&display=inline&height=370&name=2.png&originHeight=370&originWidth=270&size=6835&status=done&width=270)<br />开通隧道，可以选择免费的，也可以付费购买<br />
![3.png](https://cdn.nlark.com/yuque/0/2019/png/237720/1551627388470-d4f01a34-0df7-4ba2-bc96-0bcf9b10cc9c.png#align=left&display=inline&height=561&name=3.png&originHeight=867&originWidth=1153&size=75912&status=done&width=746)<br />购买之后会生成id号<br />
![4.png](https://cdn.nlark.com/yuque/0/2019/png/237720/1551627421388-4def7b5b-78fe-45e7-87e5-2176367a9387.png#align=left&display=inline&height=156&name=4.png&originHeight=390&originWidth=1868&size=83699&status=done&width=746)<br />对于去下载树莓派上使用的服务端<br />
![5.png](https://cdn.nlark.com/yuque/0/2019/png/237720/1551627464742-e380cd4f-a55b-464e-970f-ef5cd0a57f8e.png#align=left&display=inline&height=370&name=5.png&originHeight=901&originWidth=1818&size=70143&status=done&width=746)<br />上传至树莓派上并解压，本文放置路径/home/pi/<br />![6.png](https://cdn.nlark.com/yuque/0/2019/png/237720/1551627555240-86f107c7-08a5-44b6-a05c-fc5ffc2e5393.png#align=left&display=inline&height=88&name=6.png&originHeight=88&originWidth=582&size=22217&status=done&width=582)<br />解压后进入目录，会发现有一个可执行文件——“sunny”,执行命令"./sunny clientid <你的Ngrok隧道id>"进入下面界面，显示在线，说明服务部署成功。此时等到执行后面的index.py文件![7.png](https://cdn.nlark.com/yuque/0/2019/png/237720/1551627652171-f4334639-acd5-4689-ae73-6460997ef17a.png#align=left&display=inline&height=121&name=7.png&originHeight=141&originWidth=868&size=31296&status=done&width=746)

<a name="33f7df9a"></a>
## 2 树莓派本地网页准备
<a name="375e0c14"></a>
### 2.1 代码编写
本文想实现通过web远程控制树莓派，效果图如下：<br />
![index.png](https://cdn.nlark.com/yuque/0/2019/png/237720/1551627760347-09946cab-cf2a-49c2-897e-8bcb417adcc7.png#align=left&display=inline&height=217&name=index.png&originHeight=448&originWidth=1540&size=31057&status=done&width=746)<br />点击函数通过正则表达式筛选出点击的按键，并通过$(post)将请求传至后台脚本index.py

```
 $(function () {

                   $(".btn-trigger").click(function (){

                       var text = $(this).text().replace(/ /g, "").replace(/\n/g, "").replace(/\r/g, "").replace(/\t/g, "");

                       var cmd = "";

                       switch(text){

                           case "空调开":

                               cmd = "空调开";

                               break;

                           case "空调关":

                               cmd = "空调关";

                               break;

                           case "卧室灯开":

                               cmd = "卧室灯开";

                               break;

                           case "卧室灯关":

                               cmd = "卧室灯关";

                               break;

                           case "排气扇开":

                               cmd = "排气扇开";

                               break;

                           case "排气扇关":

                               cmd = "排气扇关";

                               break;

                           case "冰箱开":

                               cmd = "冰箱开";

                               break;

                           case "冰箱关":

                               cmd = "冰箱关";

                               break;

                           case "电饭煲开":

                               cmd = "电饭煲开";

                               break;

                           case "电饭煲关":

                               cmd = "电饭煲关";

                               break;

                           case "加湿器开":

                               cmd = "加湿器开";

                               break;

                           case "加湿器关":

                               cmd = "加湿器关";

                               break;

                           case "窗帘开":

                               cmd = "窗帘开";

                               break;

                           case "窗帘关":

                               cmd = "窗帘关";

                               break;

                           case "电视机开":

                               cmd = "电视机开";

                               break;

                           case "电视机关":

                               cmd = "电视机关";

                               break;

                       }

                       if(confirm("确定要执行该命令吗？")){

   $.post("/cmd",cmd,function(data,status){});

                       }

                   });

               })
```

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bottle import get,post,run,request,template

@get("/")
def index():
    return template("index")
@post("/cmd")
def cmd():
    print ("按下了按钮: "+request.body.read().decode())

    return "OK"
run(host="0.0.0.0")
```

<a name="9ef65e5e"></a>
### 2.2执行
将index.html和index.py上传到树莓派某个文件夹下面，执行python3 index.py

<a name="3ef1ca79"></a>
## 3 运行效果

![test.gif](https://cdn.nlark.com/yuque/0/2019/gif/237720/1551628282123-0b2b6ed2-15a0-4c43-a312-914645bf5830.gif#align=left&display=inline&height=294&name=test.gif&originHeight=702&originWidth=1780&size=285546&status=done&width=746)

<a name="a888816f"></a>
## 4 [完整代码地址](https://github.com/wongnoubo/raspberry-Ngrok)
喜欢的可以给个star鼓励一下~
