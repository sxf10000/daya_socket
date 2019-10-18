import socket,struct,json
def send_dic(c,dic):
    dic_json=json.dumps(dic)
    dic_json_length=len(dic_json.encode('utf-8'))
    struct_dic_json_length=struct.pack('q',dic_json_length)
    c.send(struct_dic_json_length)
    c.send(dic_json.encode('utf-8'))
def get_dic(c):
    try:
        dic_length=struct.unpack('q',c.recv(8))[0]
    except:
        return {'msg':'exit'}
    try:
        dic_json=c.recv(dic_length).decode('utf-8')
    except:
        return {'msg':'exit'}
    dic=json.loads(dic_json)
    return dic

import socket
from concurrent.futures import ThreadPoolExecutor
import lib.common
import re

s=socket.socket()
ip_host=('127.0.0.1',8000)
s.bind(ip_host)
s.listen()
#创建一个列表,用来保存客户端及其信息
c_list=[]
def get_send_msg(c,addr,c_list):
    while True:
        tag=False
        dic=lib.common.get_dic(c)
        if dic['msg']=='exit':
            for i in c_list:
                if i['addr']==addr:
                    c_list.remove(i)
            break
        if dic['is_siliao']==True:

            for  i in c_list:

                li=re.findall('(.*?)@%s(.*)'%i['name'],dic['msg'])
                if len(li)!=0:
                    dic['msg']=li[0][0]+li[0][1]
                    lib.common.send_dic(i['client'],dic)
                    tag=True
                    break
        if tag:
            continue
        for i in c_list:
            if i['addr']!=addr:
                lib.common.send_dic(i['client'],dic)
while True:
    print('clinet')
    c,addr=s.accept()
    print('%clinet'%addr[1])
    name=c.recv(1024).decode('utf-8')
    c_dic={'addr':addr,'client':c,'name':name}
    c_list.append(c_dic)
    t=ThreadPoolExecutor()
    t.submit(get_send_msg,c,addr,c_list)
