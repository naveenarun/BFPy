from __future__ import print_function
import argparse

# TODO: Check validity of parentheses
# TODO: Cache parentheses locations
# TODO: Optimize runtime by condensing 
# TODO: Output Brainfuck as a .py file

parser = argparse.ArgumentParser(description='Interpret a brainfuck program.')
parser.add_argument('-f',type=str,help='Name of file containing brainfuck code',required=True)
args = parser.parse_args()

mystr = ''.join(open(args.f).readlines())

mystr = filter(lambda x: x in '+-><.][,',mystr)
pointer = 0
mem = [0]*1024
read_pos = 0

def find_opener(mystr,mypos):
	counter = 1
	while counter != 0:
		mypos = mypos - 1
		if mystr[mypos] == ']':
			counter += 1
		elif mystr[mypos] == '[':
			counter -= 1
	return mypos

def find_closer(mystr,mypos):
	counter = 1
	while counter != 0:
		mypos = mypos + 1
		if mystr[mypos] == '[':
			counter += 1
		elif mystr[mypos] == ']':
			counter -= 1
	return mypos
while read_pos < len(mystr):
	curr_char = mystr[read_pos]
	if curr_char == '+':
		mem[pointer] += 1
	elif curr_char == '-':
		mem[pointer] -= 1
	elif curr_char == '>':
		pointer += 1
	elif curr_char == '<':
		pointer -= 1
	elif curr_char == '.':
		print(chr(mem[pointer]),end='')
	elif curr_char == ']':
		if mem[pointer] != 0:
			read_pos = find_opener(mystr,read_pos)
	elif curr_char == '[':
		if mem[pointer] == 0:
			read_pos = find_closer(mystr,read_pos)
	elif curr_char == ',':
		mem[pointer] = ord(raw_input())
	read_pos += 1

print('\n')
