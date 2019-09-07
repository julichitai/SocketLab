import socket

sock = socket.socket()
sock.connect(("localhost", 1010))

msg = "aa bb cc dd aa, bb, cc, \n aa,bb,bb"
msg = msg.encode("utf-8")
sock.send(msg)

data = sock.recv(1024)
uData = data.decode("utf-8")
print("Server > ", uData)

sock.close()
