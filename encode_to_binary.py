#!venv/bin/python3
# -*- coding:utf-8 -*-

import argparse

# https://youtu.be/USCBCmwMCDA

def parseArguments():
	parser = argparse.ArgumentParser(description='Create skeleton CSVs')

	parser.add_argument('--random', type=int, default=0, help='How many characters of randomness')

	return parser.parse_args()


def main():
	args = parseArguments()
	chars = '.-/049:=?ABCDQWXabcdeghmopstuvwy'

	if args.random > 0:
		# do random
		pass

	else:
		string = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
		binary = []

		for char in string:
			# print(char)
			index = chars.index(char)
			binary.append(f'{index:05b}')

		print(" ".join(binary))


# Default function is main()
if __name__ == '__main__':
	main()
