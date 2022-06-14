#program to print even nums between a range
start = int(input())
end = int(input())

for i in range(start, end+1):
	if i & 1 == 0:
		print(i)
