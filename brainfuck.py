from __future__ import print_function
import argparse

# TODO: Check validity of parentheses
# TODO: Cache parentheses locations
# TODO: Optimize runtime by condensing 
# TODO: Output Brainfuck as a .py file

# ISSUE: Uses naive parentheses search
# 

HELP_TEXT = 'Interpret a Brainfuck program.'
HELP_FILENAME = 'Name of file containing brainfuck code'
FILE_REQUIRED = True
MEMORY_SIZE = 1024

parser = argparse.ArgumentParser(description = HELP_TEXT)
parser.add_argument('-f', type=str, help = HELP_FILENAME,required=FILE_REQUIRED)
args = parser.parse_args()

mystr = ''.join(open(args.f).readlines())

mystr = filter(lambda x: x in '+-><.][,',mystr)
mem = [0]*MEMORY_SIZE
pointer = 0
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
