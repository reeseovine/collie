"""
- AddressError
- CommandError
- KeyboardError
- InputError
"""

def CollieError(type, line, desc):
	print "Collie "+str(type)+":\n  "+str(line)+"\n"+str(desc)
	quit()

def AddressError(line, addr):
	CollieError("AddressError", line, "Invalid address or number: "+str(addr))

def CommandError(line, cmd):
	CollieError("CommandError", line, "Unknown command or trick: "+str(cmd))

def KeyboardError(line):
	CollieError("KeyboardError", line, "The program was ended by user input.")

def InputError(line, input):
	CollieError("InputError", line, "Unexpected input: "+repr(input))
