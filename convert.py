#!/usr/bin/env python3

# A program that is an alternative to the base64 tool that comes with linux
# The output and usage is similar, however, this tool does not assume that you
# want a newline at the end of your encoded text.
# There is also functionality for printing the binary representation of your
# string

import argparse

B64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# parses any arguments, prints final encoded text
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-b","--binary", help="encode to binary", action="store_true")
	args = parser.parse_args()
	tob = args.binary
	print (encode(input(), tob))

# accepts plaintext and Boolean argument expressing whether or not
# the final product should be binary or base64
# encodes text, and returns final encoded text
def encode(text, tob):
	binary = ""
	for i in text:
		asciiText = ord(i)
		binPoint = findBinPoint(asciiText)
		for i in range(8 - binPoint):
			binary += "0"
		bin = tobin(asciiText, binPoint, "")
		binary += bin
	if tob:
		final = binary
	else:
		final = tob64(binary)
	return final

#takes in an int and returns the number of digits it would take to represent it in binary
def findBinPoint(inpt):
	for i in [(128,8),(64,7),(32,6),(16,5),(8,4),(4,3),(2,2),(0,1)]:
		if inpt >= i[0]:
			return i[1]

# recursive function that takes a number, a binary place, and a
# string to be added onto and returns a string one binary digit longer, with a
# 1 or a 0 added depending on whether or not 2 to the power of the binary place
# can be subtracted by the given number.
def tobin(asciiText, binPoint, soFar):
	if binPoint >= 1:
		subBy = 2 ** (binPoint - 1)
		binPoint = binPoint -1
		if asciiText >= subBy:
			soFar += "1"
			asciiText = asciiText - subBy
		else:
			soFar += "0"
		x = tobin(asciiText, binPoint, soFar)
		return x
	else:
		return soFar

#converts a binary digit into base64
def tob64(binary):
	final = ""
	extras = 0
	if len(binary) % 6 != 0:
		for i in range(6 - len(binary) % 6):
			binary += "0"
			extras += 1
	cnt = 0
	word = ""
	for i in binary:
		word += binary[cnt]
		cnt += 1
		if cnt % 6 == 0:
			wordTotal = 0
			x = 5
			for i in word:
				wordTotal += int(i) * (2 ** x)
				x -= 1
			word = ""
			final += B64[wordTotal]
			x = 6
	for i in range(extras):
		if i % 2 == 1:
			final += '='
	return final

if __name__ == '__main__':
	main()
