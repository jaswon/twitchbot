import cfg

def chat(s, msg):
	s.send("PRIVMSG #{} :{}".format(cfg.CHAN, msg))
