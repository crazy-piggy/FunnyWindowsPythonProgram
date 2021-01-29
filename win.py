import os


print("kms服务器地址：\nzh.us.to\nkms.03k.org\nkms.chinancce.com\nkms.shuax.com\nkms.dwhd.org\nkms.luody.info\nkms.digiboy.ir\nkms.lotro.cc\nwww.zgbs.cc\ncy2617.jios.org\n\n使用前请先测试服务器延迟（利用ping命令）\n\n\n\n\n")
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
