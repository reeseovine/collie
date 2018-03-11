"""
- AddressError
- CommandError
- KeyboardError
- InputError
"""

class CollieErrors():
	def __init__(self):
		self.errors_break = True

	def CollieError(self, type, line, desc):
		print "Collie "+str(type)+":"
		if line is not "": print "  "+str(line)
		print str(desc)
		if self.errors_break: quit()

	def AddressError(self, line, addr):
		self.CollieError("AddressError", line, "Invalid address or number: "+str(addr))

	def CommandError(self, line, cmd):
		self.CollieError("CommandError", line, "Unknown command or trick: "+str(cmd))

	def KeyboardError(self, line):
		self.errors_break = True
		self.CollieError("KeyboardError", line, "The program was ended by user input.")

	def InputError(self, line, input):
		self.CollieError("InputError", line, "Unexpected input: "+repr(input))
