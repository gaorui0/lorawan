# encoding: utf-8

from pydoc import describe
import paho.mqtt.client as mqtt
import base64
import struct
import json
import base64


def shangxing_03(c):
    data = struct.unpack_from('ff', bytes.fromhex(c[10:34]),offset=2)
    x = data[0]
    y = data[1]
    print("X 轴相对角度零点为：",x)
    print("Y 轴相对角度零点为：",y)


def shangxing_06_03(c, des):
    x_zhou = struct.unpack_from('b', bytes.fromhex(c[10:16]),offset=2)
    print(des, x_zhou)


def shangxing_06_09(c, des):
    x_zhou = struct.unpack_from('bb', bytes.fromhex(c[10:22]),offset=2)
    print(des,x_zhou)

def shangxing_07(c):
    describes = str(c[4:6])
    data_1 = str(c[10:16])
    data_2 = str(c[16:28])
    data_3 = str(c[28:40])
    data_4 = str(c[40:48])
    data_5 = str(c[48:56])
    data_6 = str(c[56:62])
    # d = '4901'
    # d = '0304da4fc33f'
    # print(d)
    # data_value = struct.unpack('xffhhx', bytes.fromhex(d))
    # data_value = struct.unpack('bffHHb', bytes.fromhex(d), offset=4)[0]     #word(2) H   bytes(1)  b
    #TLV格式 offset 偏移位置开始读取
    gongneng = struct.unpack_from('b', bytes.fromhex(describes))[0]
    print("上行心跳帧：", gongneng)
    data_1_value = struct.unpack_from('b', bytes.fromhex(data_1),offset=2)[0]
    print("产品型号：", data_1_value)
    data_2_value = struct.unpack_from('f', bytes.fromhex(data_2),offset=2)[0]
    print("X 轴角度：", data_2_value)
    data_3_value = struct.unpack_from('f', bytes.fromhex(data_3),offset=2)[0]
    print("Y 轴角度：", data_3_value)
    data_4_value = struct.unpack_from('h', bytes.fromhex(data_4),offset=2)[0]/100
    print("传感器温度：", data_4_value)
    data_5_value = struct.unpack_from('h', bytes.fromhex(data_5),offset=2)[0]/100
    print("供电电压：", data_5_value)
    data_6_value = struct.unpack_from('b', bytes.fromhex(data_6),offset=2)[0]
    print("产品报警处于布防状态：", data_6_value)
    file_neirong = str(gongneng) + "," + str(data_1_value) + "," + str(data_2_value) + "," + str(data_3_value) + "," + str(data_4_value) + "," + str(data_5_value) + "," + str(data_6_value) +"\n"
    with open(r'G:\python文件\mqtt测试\qingjiao.txt', 'a+') as f:
        f.write(file_neirong)


def shangxing_08(c):
    describes = str(c[4:6])
    data_1 = str(c[10:16])
    data_2 = str(c[16:28])
    data_3 = str(c[28:40])
    data_4 = str(c[40:48])
    data_5 = str(c[48:56])
    data_6 = str(c[56:62])
    # d = '4901'
    # d = '0304da4fc33f'
    # print(d)
    # data_value = struct.unpack('xffhhx', bytes.fromhex(d))
    # data_value = struct.unpack('bffHHb', bytes.fromhex(d), offset=4)[0]     #word(2) H   bytes(1)  b
    #TLV格式 offset 偏移位置开始读取
    gongneng = struct.unpack_from('b', bytes.fromhex(describes))[0]
    print("上行报警帧：", gongneng)
    data_1_value = struct.unpack_from('b', bytes.fromhex(data_1),offset=2)[0]
    print("产品型号：", data_1_value)
    data_2_value = struct.unpack_from('f', bytes.fromhex(data_2),offset=2)[0]
    print("X 轴角度：", data_2_value)
    data_3_value = struct.unpack_from('f', bytes.fromhex(data_3),offset=2)[0]
    print("Y 轴角度：", data_3_value)
    data_4_value = struct.unpack_from('h', bytes.fromhex(data_4),offset=2)[0]/100
    print("传感器温度：", data_4_value)
    data_5_value = struct.unpack_from('h', bytes.fromhex(data_5),offset=2)[0]/100
    print("供电电压：", data_5_value)
    data_6_value = struct.unpack_from('b', bytes.fromhex(data_6),offset=2)[0]
    print("产品报警处于布防状态：", data_6_value)
    file_neirong = str(gongneng) + "," + str(data_1_value) + "," + str(data_2_value) + "," + str(data_3_value) + "," + str(data_4_value) + "," + str(data_5_value) + "," + str(data_6_value) +"\n"
    with open(r'G:\python文件\mqtt测试\qingjiao.txt', 'a+') as f:
        f.write(file_neirong)


def jiexi(a):
    # a = 'WgoIGgACAQIDBHmEyj4EBOrkfUEMAqQLDQJzARkBApQh'
    b = base64.b64decode(a)
    c = b.hex()
    print(c)
    describes = str(c[4:6])
    gongneng = struct.unpack_from('b', bytes.fromhex(describes))[0]
    data_len = struct.unpack_from('h', bytes.fromhex(c[6:10]))[0]
    data_ID = c[10:12]
    print("数据长度：", data_len)
    if gongneng == 7:
        shangxing_07(c)
    if gongneng == 8:
        shangxing_08(c)
    if gongneng == 3:
        shangxing_03(c)
    if gongneng == 6:
        if data_len == 3:
            if hex(int(data_ID, 16)) == hex(0x21):
                shangxing_06_03(c, "设置心跳周期返回值：")
            if hex(int(data_ID, 16)) == hex(0x3A):
                shangxing_06_03(c, "设置相对角度测量返回值：")
            if hex(int(data_ID, 16)) == hex(0x25):
                shangxing_06_03(c, "软件重启返回值：")
        if data_len == 9:
            shangxing_06_09(c, "设置报警延时时间、报警角度返回值：")


 
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # client.subscribe("application/1/#")
    client.subscribe("application/1/device/9c65f92106030104/event/up")
 
 
def on_message(client, userdata, msg):
    print(msg.topic+" " + ":" + str(msg.payload))
    print(msg.payload.decode())
    # print(msg.payload.decode(){"data"})
    user_dict = json.loads(msg.payload.decode())
    jiexi(user_dict["data"])
    # on_publish(topic, payload, qos)
    


def on_publish(topic, payload, qos):
    # print(str(payload))
    payloads = json.dumps(payload)
    print("payloads:", payloads)
    print(client.publish(topic, payloads, qos), "123")

 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("ip", 1883, 60)
# on_publish(topic, payload, qos)
client.loop_forever()
