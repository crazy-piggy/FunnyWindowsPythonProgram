import os


a = input("请输入产品密钥:")
b = input("请输入kms服务器地址:")
while True:
    if os.system("slmgr /ipk " + a) !=0:
        a = input("请重新输入产品密钥:")
    if os.system("slmgr /skms " + b) != 0:
        b = input("请重新输入kms服务器地址或以管理员身份运行该程序:")
    else:
        os.system("slmgr /ipk " + a)
        os.system("slmgr /skms " + b)
        os.system("slmgr /ato")
        break
