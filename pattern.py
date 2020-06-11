import sys

def create_data():
	uppercase = [chr(i) for i in range(65,91)]
	lowercase = [chr(i) for i in range(97,123)]
	numbers = [chr(i) for i in range(48,58)]

	return uppercase, lowercase, numbers

def argument_check(len):
	if len != 3:
		print("Usage : ")
		print("To create a pattern: \"pattern --length or -l 500\"")
		print("To find the offset: \"pattern --query or -q 0x41424344\"")
		sys.exit(0)

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

	argument_check(len(sys.argv))
	data = create_data()

	if sys.argv[1] == "--length" or sys.argv[1] == "-l":
		length = int(sys.argv[2])
		create_pattern(data[0], data[1], data[2], length)
	elif sys.argv[1] == "query" or sys.argv[1] == "-q":
		query = str(sys.argv[2])
		find_offset(data[0], data[1], data[2], query)
	else:
		print("Usage : ")
		print("To create a pattern: \"pattern --length or -l 500\"")
		print("To find the offset: \"pattern --query or -q 0x41424344\"")
		sys.exit(0)



