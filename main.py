#!/usr/bin/env python2

import sys, random, re, time, ast
from errors import CollieErrors

class Dishes:
	def __init__(self):
		self.dishes = {}	# dictionary keys are strings representing dish locations (ex. dish1, dish42)
		self.pattern = re.compile(r'dish[0-9]+')

	def _parse_addr(self, addr):
		if self.addr_is_valid(addr):
			return addr

	def addr_is_valid(self, addr):
		return self.pattern.match(addr)

	def get(self, addr, move):
		val = self.dishes[self._parse_addr(addr)]
		if move: self.dishes[self._parse_addr(addr)] = 0
		return val

	def set(self, addr, val):
		if hasattr(self.dishes, self._parse_addr(addr)):
			val += self.dishes[self._parse_addr(addr)]
		self.dishes[self._parse_addr(addr)] = val

class Floor:
	def __init__(self):
		self.floor = []		# a list of ints, chosen from randomly

	def get(self, move):
		i = random.randint(0, len(self.floor)-1)
		val = self.floor[i]
		if move: del self.floor[i]
		return val

	def put(self, val):
		self.floor.append(val)

	def reset(self):
		self.floor = []

class Collie:
	def __init__(self):
		self.err = CollieErrors()
		self.dishes = Dishes()
		self.floor = Floor()
		self.mouth = 0  # a single value that is in the dog's mouth
		self.cmds = {
			'fetch':  self.fetch,
			'drop':   self.drop,
			'pickup': self.pickup,
			'eat':    self.eat,
			'take':   self.take,
			'show':   self.show,
			'give':   self.give,
			'bark':   self.bark,
			'sit':    self.sit,
			'bed':    self.bed,
		}
		self.tricks = {}
		self.is_being_taught = False
		self.trick_being_taught = ""
		self.asleep = False
		self.line = ""
		self.print_newlines = False

	def eval_num(self, num=0, move=True, noerr=False):
		if type(num) == int or num.isdigit():
			val = int(num)
		elif self.dishes.addr_is_valid(num):
			val = self.dishes.get(num, move)
		elif num == "floor":
			val = self.floor.get(move)
		else:
			if not noerr: self.err.AddressError(self.line, num)
			return False

		if val < 0: val = 0
		return val


	def fetch(self, num=0):
		self.mouth += self.eval_num(num, move=False)

	def drop(self, loc):
		if loc == "floor":
			self.floor.put(self.mouth)
		elif self.dishes.addr_is_valid(loc):
			self.dishes.set(loc, self.mouth)
		self.mouth = 0

	def pickup(self, loc):
		self.mouth += self.eval_num(loc)

	def eat(self, num=0):
		self.mouth -= self.eval_num(num, move=False)

	def take(self):
		try:
			inp = raw_input("> ")
			self.mouth += int(inp)
		except KeyboardInterrupt:
			self.err.KeyboardError(self.line)
		except (SyntaxError, ValueError):
			self.err.InputError(self.line, inp)

	def show(self):
		sys.stdout.write(str(self.mouth))
		if self.print_newlines: sys.stdout.write("\n")

	def give(self):
		self.show()
		self.mouth = 0

	def bark(self, string):
		sys.stdout.write(ast.literal_eval(string))
		if self.print_newlines: sys.stdout.write("\n")

	def sit(self, num=1):
		time.sleep(self.eval_num(num))

	def bed(self):
		self.asleep = True


	def parse_line(self, line):	# call appropriate function with appropriate number value
		if type(line) == list:
			parts = line
		else:
			parts = line.split(" ")

		if not re.match(r'\t', parts[0]):
			self.is_being_taught = False
			self.trick_being_taught = ""

		parts = map(str.strip, parts)
		self.line = " ".join(parts)

		# determine if teaching a trick
		if parts[0] == "teach":
			self.is_being_taught = True
			self.trick_being_taught = parts[1]
			self.tricks[self.trick_being_taught] = []
			return

		# store lines in trick, don't execute them
		if self.is_being_taught:
			self.tricks[self.trick_being_taught].append(parts)
			return

		# execute if cmd is a trick
		if parts[0] in list(self.tricks.keys()):
			for p in self.tricks[parts[0]]:
				if not self.asleep:
					self.parse_line(p)
				else: break
			return

		# match a number at beginning of line
		num = self.eval_num(parts[0], move=False, noerr=True)
		if num is not False:
			if num > 0:
				for i in range(0, num):
					self.parse_line(parts[1:])
			return

		# find argument(s) and execute command
		arg = ' '.join(parts[1:]).strip()
		cmd = parts[0]
		if cmd in list(self.cmds.keys()):
			if arg:
				self.cmds[cmd](arg)
			else:
				self.cmds[cmd]()
		elif cmd is not '' and cmd is not ' ':
			self.err.CommandError(self.line, cmd)


if __name__ == "__main__":
	dog = Collie()
	if len(sys.argv) > 1:
		with open(str(sys.argv[1])) as f:
			for line in f:
				if not dog.asleep:
					dog.parse_line(line)
				else: break
	else:
		dog.err.errors_break = False
		dog.print_newlines = True
		print "Collie 1.2 real-time interpreter"
		while True:
			try:
				line = raw_input(">>> ")
			except KeyboardInterrupt:
				dog.err.KeyboardError("")

			dog.parse_line(line)

			if dog.asleep:
				break
