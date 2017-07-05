import re

# decorator to add functions to actions dict
actions = {}
def add_action(pattern):
	def add_patterned_action(fn):
		actions[pattern] = fn
		return fn
	return add_patterned_action

def action(user,msg):
	for pattern in actions:
		if pattern.match(msg):
			return actions[pattern](user,msg)	
	return ""

#--- actions ---

@add_action(re.compile(r'(hi|hello|hey)!?',re.I))
def hello(user,msg):
	return "hi {}!".format(user)

