from urllib.request import urlopen
import os
with open('url.para','r') as f:
    ff=f.read()
#导入http请求类库
url = ff
#询问链接
filename=url[ url.rindex( '/' ) + 1 : len( url ) ]
#获取文件文件名
with open(filename, "wb") as f:
    #以二进制形式写入下载好的文件
    f.write(urlopen(url).read())
    print("Download Completed Sucessfully.")
    os.system("pause")
    

