import cfg

def chat(s, msg):
	s.send("PRIVMSG #{} :{}\r\n".format(cfg.CHAN, msg).encode("utf-8"))
