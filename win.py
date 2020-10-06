import os


a = input("请输入产品密钥:")
while True:
    if os.system("slmgr /ipk " + a) !=0:
        a = input("请重新输入产品密钥:")
    else:
        os.system("slmgr /ipk " + a)
        os.system("slmgr /skms kms.03k.org")
        os.system("slmgr /ato")
        break
