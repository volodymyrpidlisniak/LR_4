a = input('Enter string A: ')
b = input('Enter string B: ')

count = 0
i = 0

while i <= len(a) - len(b):
    if a[i : i + len(b)] == b:
        count += 1
    i += 1

print(count)