import socket

sock = socket.socket()
sock.connect(("localhost", 1010))

msg = "Вот дом,\nКоторый построил Джек.\nА это пшеница, /" \
      "\nКоторая в темном чулане хранится\nВ доме, /" \
      "\nКоторый построил Джек.\nА это веселая птица-синица, /" \
      "\nКоторая часто ворует пшеницу, /" \
      "\nКоторая в темном чулане хранится\nВ доме,\nКоторый построил Джек."


msg = msg.encode("utf-8")
sock.send(msg)

data = sock.recv(1024)
uData = data.decode("utf-8")
print("Server > ", uData)

sock.close()
