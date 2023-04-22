import socket

tcp1 = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
tcp_ip = ""         #Any interface
port = 9000        #Arbitrary non-privileged port
buffer_size = 1024
msg = ("Connected...")


tcp1.bind ((tcp_ip , port))
tcp1.listen(1)
con, addr = tcp1.accept()
print ("TCP Connection from: ", addr)



while True:
	data = con.recv(buffer_size).decode('utf-8')
	if not data:
		break
	print ("Data received: " + data)
	print ("Sending response: "  + data)
	con.send (data.encode('utf-8'))
tcp1.close()