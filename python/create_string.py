import sys

length = int(sys.argv[1])

uppercase = [chr(i) for i in range(65,91)]
lowercase = [chr(i) for i in range(97,123)]
numbers = [chr(i) for i in range(48,58)]

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


