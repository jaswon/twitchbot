import cfg
import utils
import socket
from time import sleep
import re

s = socket.socket()
s.connect((cfg.HOST,cfg.PORT))
s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
s.send("JOIN #{}\r\n".format(cfg.CHAN).encode("utf-8"))
# s.send("CAP REQ :twitch.tv/tags\r\n".encode("utf-8"))

msg = re.compile(r"^:(\w+)!\w+@\w+\.tmi\.twitch\.tv ([A-Z]+) #\w+ :(.*)$")

while True:
	res = s.recv(1024).decode("utf-8")
	if res == "PING :tmi.twitch.tv\r\n":
		s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
	elif msg.match(res):
		m = msg.match(res).groups()
		print(m)
		if m[2].rstrip() in ["hi","hello","hi!","hello!"]:
			utils.chat(s,"hi {}!".format(m[0]))

	else:
		# print(msg.match(res))
		print(res)
	sleep(1 / cfg.RATE)
