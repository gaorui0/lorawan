# 物联网lowanwan协议倾角传感器
## chirpStack添加倾角传感器步骤
* 创建DEV_Profiles
![create_Dev_profiles.jpg](image/create_Dev_profiles.jpg)
![create_dev_name.jpg](image/create_dev_name.jpg)
* 倾角传感器默认OTAA入网
![OTAA.jpg](image/OTAA.jpg)
* 创建APP应用
![create_app.jpg](image/create_app.jpg)
* 创建APP应用下的传感器
![create_app_devices.jpg](image/create_app_devices.jpg)
* 添加OTAA值
![add_OTAA.jpg](image/add_OTAA.jpg)
## 接受上行数据
* 通过chirpStack获取数据
* 通过订阅MQTT主题方式过去数据
## 发送下行数据传感器信息
* 通过chirpStack的Downlink queue下发数据
![lora下行数据.png](image/lora下行数据.png)
* 通过调用chirpStack API发送下行数据
代码文件```send_change_data.py```

