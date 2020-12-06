D学习笔记
# 网络分层
## OSI 参考模型
> 理论基础

- 应用层
- 表示层
- 会话层
- 传输层
    
    > TCP/UDP
- 网络层
    
    > 路由
- 数据链路层
    
    > 交换
- 物理层
    
    > 物理硬件

## TCP/IP模型（TCP/IP协议簇）
> 实际编程时的参考模型
- 应用层
    > 对应OSI 的应用层、表示层、会话层
    
    > 实际的服务、应用在这一层中实现
- 传输层
    
    > 对应OSI 的传转层
    >
    > 使用TCP/UDP 进行数据传输
- 网络层
    
    > 对应OSI 的网络层
    >
    > IP/路由 询径
- im网络接口层
    
    > 对应OSI 的数据链路层和物理层

# socket

## socket 通信模型



## socket 编程

 ### socket api

> import socket

- socket()

    >实例化socket对象 socket.socket()
    >
    >> socket.AF_INET   # 使用ipv4地址
    >>
    >> socket.SOCK_STREAM   # 使用TCP进行连接

    ```python
    import socket
    # 客户端
    s = socket.socket(socket.AF_INET, socket.SOCK_STARAM)
    print(s)
    
    s.close() # 关闭
    '''
    输出
    <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 0)>
    
    fd=3   									# socket打开的文件描述符
    family=AddressFamily.AF_INET   			# 使用IPv4 
    type=SocketKind.SOCK_STREAM				# 使用TCP
    proto=0									#
    laddr=('0.0.0.0', 0)					# 客户端监听地址、端口
    
    '''
    ```

- connect

    > 建立连接
    >
    > s.connect(('URL', PORT)

    ```python
    import socket
    # 客户端
    s = socket.socket(socket.AF_INET, socket.SOCK_STARAM)
    s.connect({'www.baidu.com', 80})
    print(s)
    s.close()
    '''
    <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('192.168.111.9', 51605), raddr=('110.242.68.3', 80)>
    
    laddr=('192.168.111.9', 51605)   # 客户端监听的地址和端口
    raddr=('110.242.68.3', 80)		 # 服务端监听的地址和端口
    '''
    ```

- send()

    >  发送数据

    ```python
    import socket
    # 客户端
    s = socket.socket(socket.AF_INET, socket.SOCK_STARAM)
    s.connect({'www.baidu.com', 80})
    s.send(b'GET / HTTP/1.1\r\nHOST:time.geekbang.org\r\nConnection: close\n\r\n)
           
    s.close()
    # 先中要执行的代码 shift+ENTER 执行先中代码
    '''
    >>> s.send(b'GET / HTTP/1.1\r\nHOST:time.geekbang.org\r\nConnection: close\n\r\n')
    60    # 返回字节数
    '''
    ```

- recv()

    > 接收返回的数据

    ```python
    import socket
    # 客户端
    s = socket.socket(socket.AF_INET, socket.SOCK_STARAM)
    s.connect({'www.baidu.com', 80})
    s.send(b'GET / HTTP/1.1\r\nHOST:time.geekbang.org\r\nConnection: close\n\r\n)
    buffer = []    # 接收数据的列表
    while True:
    	data = s.recv(1024)
    	if data:
           buffer.append(data)
        else:
           break
    s.close()
           
    print(buffer)
    '''
    [b'HTTP/1.1 200 OK\r\nAccept-Ranges: bytes\r\nCache-Control: no-cache\r\nContent-Length: 14615\r\nContent-Type: text/html\r\nDate: Sat, 05 Dec 2020 02:52:25 
    ...
    IE=Edge,chrome=1\r\nConnection: close   # 头信息 
    \r\n\r\n     
    <!DOCTYPE html><!--STATUS OK--          # HTML信息
    ....
    new Date(new Date().getTime() + 10*60*1000).toGMTString();</script>\r\n</body></html>\r\n"]
    '''
    res = b''.join(buffer)  				# 
    header, html = res.split(b'\r\n\r\n',1) # 分离header和html
    print(header.decode('utf-8'))           # 打印请求头信息 
    '''
    HTTP/1.1 200 OK
    Accept-Ranges: bytes
    Cache-Control: no-cache
    Content-Length: 14615
    Content-Type: text/html
    Date: Sat, 05 Dec 2020 02:52:25 GMT
    P3p: CP=" OTI DSP COR IVA OUR IND COM "
    P3p: CP=" OTI DSP COR IVA OUR IND COM "
    Pragma: no-cache
    Server: BWS/1.1
    Set-Cookie: BAIDUID=F9F3706A91321991B4B13461386C99EE:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
    Set-Cookie: BIDUPSID=F9F3706A91321991B4B13461386C99EE; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
    Set-Cookie: PSTM=1607136745; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
    Set-Cookie: BAIDUID=F9F3706A913219915A1E22F06CBC3CD0:FG=1; max-age=31536000; expires=Sun, 05-Dec-21 02:52:25 GMT; domain=.baidu.com; path=/; version=1; comment=bd
    Traceid: 160713674523710374507698411051171829077
    Vary: Accept-Encoding
    X-Ua-Compatible: IE=Edge,chrome=1
    Connection: close
    '''
    with open('baidu-index.html', 'wb') as f:   # 将html 信息写信文件
           f.write(html)
    
    ```

    

- bind()

    > 指定socket 绑定到指定主机和端口上

    ```python
    
    ```

    

- listen()

    > 接入的连接数

    ```python
    
    ```

    

- accept()

    > 接入用户端的连接

    ```python
    
    ```

    

- close()

    > 关闭socket

## socket 实现 echo 服务端、客户端

> 分析
>
> 1. server端
>
> > 1. 实例化 socket 
> >
> >     > s = socket.socket(socket.AF_INET, socket.SOCK_STREAM))
> >
> > 2. bint() 绑定ip、port   
> >
> >     > s.bind((host, port))
> >
> > 3. listen() 设置连接数  
> >
> >     >  s.listen(1) 
> >
> > 4. accept()  阻塞等待客户端连接,获取 客户端连接conn ,客户端地址 addr 
> >
> >     > conn, addr = s.accept()
>
> 2. clien端
>
> > a. 实例化 socket
> >
> > > c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
> >
> > b. 连接server端
> >
> > > c.connect((host, port))
> >
> > c. 发送数据
> >
> > > c.sendall(c_data.encode())
>
>  	3. server端接收数
>
> > 5. recv() 接收客户端数据
> >
> >     > c_data = conn.recv(1024)
> >
> > 6. send() 向客户端返回数据
> >
> >     > conn.sendall(c_data)
>
> 4.  client端接收server端数据
>
> > e. 接收服务端数据
> >
> > > s_data = s.recv(1024)
> >
> > f. 处理服务端返回的数据
> >
> > > print(s_data.decode())





