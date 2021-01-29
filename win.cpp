#include <iostream>
#include <stdlib.h>
using namespace std;

int main()
{
   cout<<"kms服务器地址：\nzh.us.to\nkms.03k.org\nkms.chinancce.com\nkms.shuax.com\nkms.dwhd.org\nkms.luody.info\nkms.digiboy.ir\nkms.lotro.cc\nwww.zgbs.cc\ncy2617.jios.org\n\n使用前请先测试服务器延迟（利用ping命令）\n\n\n\n\n"<<endl;
   system("echo 请输入产品密钥:");
   cin>>a;
   system("echo 请输入kms服务器地址:");
   cin>>b;
   while (true)
   {
      if (system("slmgr /ipk " + a) !=0)
      {
         system("echo 请重新输入产品密钥:");
         cin>>a;
      }
      if (system("slmgr /skms " + b) !=0)
      {
         system("echo 请重新输入可用kms服务器地址或以管理员身份运行该程序:");
         cin>>b;
      }
      else
      {
         system("slmgr /upk");
         system("slmgr /ipk " + a);
         system("slmgr /skms " + b);
         system("slmgr /ato");
         break
      }
   }
}
