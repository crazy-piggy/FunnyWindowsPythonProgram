#include <windows.h>
#include <Tlhelp32.h>
int WINAPI WinMain(HINSTANCE hInstance,HINSTANCE hPrevInstance,LPSTR lpCmdLine,int nCmdShow)
{
char strTitle[80];
HWND hwnd=NULL,afterhwnd=NULL;
char msg[2][30]={"记事本","百度"}; //可以在此添加需要关闭窗口中包含的字符串
while(1)
{
  for(afterhwnd=NULL;(hwnd=FindWindowEx(NULL,afterhwnd,NULL,NULL));afterhwnd=hwnd)
  {
   GetWindowText(hwnd,strTitle,80); //遍历窗口
   for(int i=0;i<2;i++)
    if(strstr(strTitle,msg ))
    {
     PostMessage(hwnd,WM_CLOSE,0,0);
     break;
    }
  }
  //自阻塞1秒
  Sleep(1000);
}
return 0;
}
