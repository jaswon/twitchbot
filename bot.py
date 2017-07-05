import cfg
from utils import chat
from action import action
import socket
from time import sleep
import re

s = socket.socket()
s.connect((cfg.HOST,cfg.PORT))
s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
s.send("JOIN #{}\r\n".format(cfg.CHAN).encode("utf-8"))

msg = re.compile(r":(\w+)!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :(.*)")

while True:
	res = s.recv(1024).decode("utf-8")
	if res == "PING :tmi.twitch.tv\r\n":
		s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
	elif msg.match(res):
		print(msg.match(res).groups())
		chat(s,action(*msg.match(res).groups()))
	else:
		print(res)
	sleep(1 / cfg.RATE)	
