#!venv/bin/python3
# -*- coding:utf-8 -*-

import argparse
import random

# https://youtu.be/USCBCmwMCDA

def parseArguments():
	parser = argparse.ArgumentParser(description='Create skeleton CSVs')

	parser.add_argument('--random', type=int, default=0, help='How many characters of randomness')
	parser.add_argument('--key', action='store_true', help='Print character to number to binary key')

	return parser.parse_args()


def main():
	args = parseArguments()
	chars = '.-/&49:=?ABCDQWXabcdeghmopstuvwy'
	string = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&'
	binary = []

	if args.random > 0:
		string = ''.join(random.choices(list(chars), k=args.random))

	for char in string:
		# print(char)
		index = chars.index(char)
		binary.append(f'{index:05b}')

	if args.key:
		for char in chars:
			index = chars.index(char)
			print(f'{char}\t{index}\t{index:05b}')
	else:
		print(" ".join(list(binary)))


# Default function is main()
if __name__ == '__main__':
	main()
