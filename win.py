import os


a = input("请输入产品密钥:")
while True:
    if os.system("slmgr /ipk " + a) !=0:
        a = input("请重新输入产品密钥:")
    else:
        os.system("slmgr /ipk " + a)
        os.system("slmgr /skms kms.03k.org") #此命令需要管理员权限才可执行,导致全程序需要以管理员的身份运行
        os.system("slmgr /ato")
        break
