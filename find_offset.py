import sys

length = 20982
query = str(sys.argv[1])
query = query[2:]
bytes_object = bytearray.fromhex(query)
ascii_string = bytes_object.decode("ASCII")
ascii_string = ascii_string[::-1]
print(ascii_string)

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
				pass
                        elif length - len(pattern_u) == 1:
                                pattern_u += i
                        elif length - len(pattern_u) == 2:
                                pattern_u += j
                        else:
                                pattern_u += i+j

result = pattern_u.find(ascii_string)
print(result)
