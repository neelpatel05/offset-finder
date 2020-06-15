import sys
import argparse

def create_data():
	uppercase = [chr(i) for i in range(65,91)]
	lowercase = [chr(i) for i in range(97,123)]
	numbers = [chr(i) for i in range(48,58)]

	return uppercase, lowercase, numbers

def create_pattern(uppercase, lowercase, numbers, length):
	pattern_u = ''

	for i in uppercase:
		pattern_u += i
		for j in lowercase:
			pattern_u += j
			for k in numbers:
				pattern_u += k
				if len(pattern_u) == length:
					print(pattern_u)
					sys.exit(0)
				elif length - len(pattern_u) == 1:
					pattern_u += i
					print(pattern_u)
					sys.exit(0)
				elif length - len(pattern_u) == 2:
					pattern_u += j
					print(pattern_u)
					sys.exit(0)
				else:
					pattern_u += i+j

def find_offset(uppercase, lowercase, numbers, query):

	length = 20982
	query = query[2:]
	bytes_object = bytearray.fromhex(query)	
	ascii_string = bytes_object.decode("ASCII")
	ascii_string = ascii_string[::-1]

	pattern_u = ''

	for i in uppercase:
		pattern_u += i
		for j in lowercase:
			pattern_u += j
			for k in numbers:
				pattern_u += k
				if len(pattern_u) == length:
					pass
				elif length - len(pattern_u) == 1:
					pattern_u += i
				elif length - len(pattern_u) == 2:
					pattern_u += j
				else:
					pattern_u += i+j

	result = pattern_u.find(ascii_string)
	print("The offset required to overwrite Instruction Pointer is " + str(result))

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description="Finds the offset required to overflow buffer", epilog="Enjoy overflowing buffer, but beware of canaries ;)")

	parser.add_argument("-l","--length", type=int, help="The length of pattern required")
	parser.add_argument("-q","--query", type=str, help="The value of eip when input is the generated pattern")

	args = parser.parse_args()
	args = vars(args)
	data = create_data()

	if len(sys.argv) == 1:
		parser.print_help(sys.stderr)
	elif len(sys.argv) > 1:
		if args["length"] != None:
			length = int(args["length"])
			create_pattern(data[0], data[1], data[2], length)
		if args["query"] != None:
			query = str(args["query"])
			find_offset(data[0], data[1], data[2], query)



