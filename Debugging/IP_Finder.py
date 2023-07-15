import socket
import time

# set up Wi-Fi connection
TCP_IP = '192.168.43.196'  # replace this with the IP address of your ESP32
TCP_PORT = 5005  # replace this with the port number you're using on the ESP32
BUFFER_SIZE = 1024
S3 = 1
S4 = 1

while True:
	exec(f"TCP_IP='192.168.{S3}.{S4}'")
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((TCP_IP, TCP_PORT))
		s.send(str(1).encode())
		s.close()
		print('sent')
		print(TCP_IP)
	except:
		print('.')
		if S4 >= 255:
			S4 = 1
			S3 += 1
		elif S3 <= 255:
			S4 += 1

# close Wi-Fi connection
s.close()
