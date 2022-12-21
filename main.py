# -*- coding: utf-8 -*-
## 使用有问题请到github.com/ravelloh/RSS提ISSUE
### Author: RavelloH
#### MICENCE: MIT
##### RSS Maker
from urllib.request import urlopen
import re,os
import linecache
import time
from datetime import datetime 

urls = 'https://ip.useragentinfo.com/json?ip='
# 初始化 
startTime = time.localtime()
startDateTime = datetime.now()
print('[初始化进程运行] - '+time.strftime("%H:%M:%S",time.localtime()))

if 'update-info.info' in os.listdir('.'):
    with open(r'./update-info.info','r') as fp:
        l1 = fp.readlines()
        ip1 = l1[0].replace('\n', '')
        ip2 = l1[1].replace('\n', '')
        ip3 = l1[2].replace('\n', '')
        ip4 = l1[3].replace('\n', '')
    print('  检测到已有进程，已载入')
else:
    with open(r"./update-info.info", 'w') as fp:
        ip1='0'
        ip2='0'
        ip3='0'
        ip4='0'
        fp.write(ip1+'\n'+ip2+'\n'+ip3+'\n'+ip4+'\n')
    print('  未检测到已有进程，已创建新进程')
ipN1=ip1
ipN2=ip2
ipN3=ip3
ipN4=ip4
doneNum = 0
print('[初始化进程结束]')

DoneResult = (int(ip1))*256**3+(int(ip2))*256**2+(int(ip3))*256+(int(ip4))
ToDoResult = 256**4 - DoneResult
print(f'[共完成{DoneResult+1}个ip，剩余{ToDoResult-1}个ip，完成约{((DoneResult+1)/256**4)*100}%]')
 
print('[主进程开始，初始ip为:'+ip1+'.'+ip2+'.'+ip3+'.'+ip4+']')

for N1 in range(0,256):
    if N1 < int(ipN1):
        pass
    else:
        ipN1 = 0
        print('\r'+time.strftime("%H:%M:%S",time.localtime())+' N1进度['+'|'*(N1//8)+' '*(32-(N1//8))+']'+str(N1)+'/256  - '+str(round((N1/12.8)*5,2))+'%')
        for N2 in range(0,256):
            if N2 < int(ipN2):
                pass
            else:
                ipN2 = 0
                print('\r'+time.strftime("%H:%M:%S",time.localtime())+' N2进度['+'|'*(N2//8)+' '*(32-(N2//8))+']'+str(N2)+'/256  - '+str(round((N2/12.8)*5,2))+'%')
                for N3 in range(0,256):
                    if N3 < int(ipN3):
                        pass
                    else:
                        ipN3 = 0
                        print('\r'+time.strftime("%H:%M:%S",time.localtime())+' N3进度['+'|'*(N3//8)+' '*(32-(N3//8))+']'+str(N3)+'/256  - '+str(round((N3/12.8)*5,2))+'%' )                        
                        for N4 in range(0,256):
                            if N4 < int(ipN4):
                                pass 
                            else:
                                ipN4 = 0
                                os.makedirs('./ip-list/'+str(N1)+'/'+str(N2)+'/'+str(N3)+'/', exist_ok=True)
                                with open('./ip-list/'+str(N1)+'/'+str(N2)+'/'+str(N3)+'/'+str(N4)+'.json','w',encoding = "utf-8") as fn:
                                    try:
                                        originInfo = urlopen(urls+str(N1)+str(N2)+str(N3)+str(N4))
                                        fn.write(str(originInfo.read().decode('utf-8')).replace(', "code": 200, "desc": "success"',''))
                                    except:
                                        while True:
                                            originInfo = urlopen(urls+str(N1)+str(N2)+str(N3)+str(N4))
                                            if str(originInfo.read().decode('utf-8')).replace(', "code": 200, "desc": "success"','') != '':
                                                fn.write(str(originInfo.read().decode('utf-8')).replace(', "code": 200, "desc": "success"',''))
                                                break
                                    with open(r"./update-info.info", 'w') as fp:
                                        fp.write(str(N1)+'\n'+str(N2)+'\n'+str(N3)+'\n'+str(N4)+'\n')
                                    NowDateTime = datetime.now()
                                    doneNum += 1
                                    doneSec = (NowDateTime - startDateTime).seconds
                                    speed = doneNum / (doneSec+0.001)
                                    remainSec = (ToDoResult-doneNum)/speed
                                    # print('\n'+str(remainSec)+'\n')
                                    print('\r'+time.strftime("%H:%M:%S",time.localtime())+' N4进度['+'|'*(N4//8)+' '*(32-(N4//8))+']'+str(N4)+'/256  - '+str(round((N4/12.8)*5,2))+'% - ' + time.strftime("%H:%M:%S", time.gmtime(remainSec)),end='')
                                    if doneSec > 14400:
                                        exit()
