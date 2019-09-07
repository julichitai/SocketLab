import socket
from WordsCounter import WordsCounter

sock = socket.socket()
sock.bind(("", 1010))

sock.listen(1)

print("waiting...")
conn, addr = sock.accept()
print("connected: ", addr)

data = conn.recv(1024)
uData = data.decode("utf-8")
print("Client > ", uData)

counter = WordsCounter(uData)

conn.send(counter.count_words().encode("utf-8"))

conn.close()
