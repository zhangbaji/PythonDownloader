from urllib.request import urlopen
#导入http请求类库
url = input("Input Filename:")
#询问链接
filename=url[ url.rindex( '/' ) + 1 : len( url ) ]
#获取文件文件名
with open(filename, "wb") as f:
    #以二进制形式写入下载好的文件
    f.write(urlopen(url).read())
    print("Download Completed Sucessfully.")
